import * as THREE from 'three';
import {GLTFLoader} from 'three/addons/loaders/GLTFLoader.js';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';
const activeViewers=new Set();
export async function createViewer(stage){
 const low=matchMedia('(max-width:700px)').matches||(navigator.deviceMemory&&navigator.deviceMemory<=4);
 const renderer=new THREE.WebGLRenderer({antialias:!low,alpha:false,powerPreference:'low-power'});
 let disposed=false;let observer;let resize;let raf=0;let meshRoot;let visible=true;let expanded=false;
 const canvas=renderer.domElement;canvas.tabIndex=0;canvas.setAttribute('role','img');canvas.setAttribute('aria-label',stage.dataset.name+'. Interactive 3D model. Arrow keys rotate, plus and minus zoom, R resets.');
 renderer.setPixelRatio(Math.min(window.devicePixelRatio||1,low?1:1.5));renderer.outputColorSpace=THREE.SRGBColorSpace;renderer.toneMapping=THREE.ACESFilmicToneMapping;renderer.toneMappingExposure=1.25;renderer.shadowMap.enabled=!low;renderer.shadowMap.type=THREE.PCFSoftShadowMap;
 const scene=new THREE.Scene();scene.background=new THREE.Color('#14161c');scene.fog=new THREE.Fog('#14161c',12,30);
 const camera=new THREE.PerspectiveCamera(36,1,.01,100);camera.position.set(4,2,5);
 const controls=new OrbitControls(camera,canvas);controls.enableDamping=true;controls.dampingFactor=.09;controls.enablePan=false;controls.autoRotate=false;controls.autoRotateSpeed=.65;controls.maxPolarAngle=Math.PI*.54;controls.minPolarAngle=.15;
 canvas.style.touchAction='pan-y';
 scene.add(new THREE.HemisphereLight(0xdce7ff,0x26242d,2.8));
 const key=new THREE.DirectionalLight(0xfff6ef,4.5);key.position.set(3,6,4);key.castShadow=!low;key.shadow.mapSize.set(1024,1024);key.shadow.camera.left=-5;key.shadow.camera.right=5;key.shadow.camera.top=5;key.shadow.camera.bottom=-5;key.shadow.normalBias=.025;scene.add(key);
 const rim=new THREE.DirectionalLight(0x1677e8,2);rim.position.set(-4,2,-3);scene.add(rim);
 const red=new THREE.DirectionalLight(0xe50909,1);red.position.set(4,1,-3);scene.add(red);
 const floor=new THREE.Mesh(new THREE.CircleGeometry(12,low?32:64),new THREE.MeshStandardMaterial({color:0x15171d,roughness:.9,metalness:.1}));floor.rotation.x=-Math.PI/2;floor.position.y=-.025;floor.receiveShadow=!low;scene.add(floor);
 const status=stage.querySelector('.model-status');
 function dispose(){if(disposed)return;disposed=true;renderer.setAnimationLoop(null);cancelAnimationFrame(raf);observer?.disconnect();resize?.disconnect();controls.dispose();renderer.dispose();scene.traverse(obj=>{obj.geometry?.dispose();if(obj.material){const ms=Array.isArray(obj.material)?obj.material:[obj.material];for(const m of ms){for(const v of Object.values(m))if(v?.isTexture)v.dispose();m.dispose()}}});canvas.remove();window.removeEventListener('halgan-motion',motionHandler);document.removeEventListener('visibilitychange',visibilityHandler);stage.classList.remove('loaded');stage.querySelector('.viewer-tools').hidden=true;stage.dataset.loading='false';const b=stage.querySelector('.model-load');b.disabled=false;b.textContent='EXPLORE IN 3D ⤢';activeViewers.delete(dispose);}
 const motionHandler=e=>{if(e.detail.paused){controls.autoRotate=false;const b=stage.querySelector('[data-view="rotate"]');b.setAttribute('aria-pressed','false');b.textContent='AUTO ROTATE'}};
 const visibilityHandler=()=>{if(!document.hidden&&visible&&!disposed){cancelAnimationFrame(raf);last=0;raf=requestAnimationFrame(frame)}};
 let last=0;let cinematicBase=null;let cinematicTarget=null;
 function frame(time){if(disposed)return;if(!visible||document.hidden){raf=0;return;}if(time-last>1000/30){if(cinematicBase&&stage.hasAttribute('data-arena')&&!stage.dataset.userMoved&&!controls.autoRotate&&!document.documentElement.classList.contains('motion-paused')){const rect=stage.getBoundingClientRect();const progress=THREE.MathUtils.clamp((innerHeight*.5-rect.top)/Math.max(rect.height,1),0,1);const offset=cinematicBase.clone().sub(cinematicTarget).applyAxisAngle(new THREE.Vector3(0,1,0),(progress-.5)*.18);camera.position.copy(cinematicTarget).add(offset);}
controls.update();renderer.render(scene,camera);last=time;}raf=requestAnimationFrame(frame)}
 try{
 const gltf=await new GLTFLoader().loadAsync(stage.dataset.model,event=>{if(event.total)status.textContent=`Loading original asset · ${Math.round(event.loaded/event.total*100)}%`;else status.textContent='Loading original HALGAN asset…'});
 if(disposed)return;
 meshRoot=gltf.scene;meshRoot.updateMatrixWorld(true);const original=new THREE.Box3().setFromObject(meshRoot);const size=original.getSize(new THREE.Vector3());if(!Number.isFinite(size.length())||size.length()===0)throw new Error('Empty model bounds');
 const scale=3.5/Math.max(size.x,size.y,size.z);meshRoot.scale.multiplyScalar(scale);meshRoot.updateMatrixWorld(true);const bounds=new THREE.Box3().setFromObject(meshRoot);const center=bounds.getCenter(new THREE.Vector3());meshRoot.position.x-=center.x;meshRoot.position.z-=center.z;meshRoot.position.y-=bounds.min.y;meshRoot.updateMatrixWorld(true);
 meshRoot.traverse(obj=>{if(obj.isMesh){obj.castShadow=!low;obj.receiveShadow=!low;obj.frustumCulled=true}});scene.add(meshRoot);
 const finalBounds=new THREE.Box3().setFromObject(meshRoot),finalSize=finalBounds.getSize(new THREE.Vector3()),target=new THREE.Vector3(0,finalSize.y*.48,0);controls.target.copy(target);
 const isRing=stage.dataset.model.includes('REF072');const radius=Math.max(finalSize.x,finalSize.y,finalSize.z);const startAngle=isRing?.68:.12;
 let resetPosition;function fit(){const aspect=stage.clientWidth/stage.clientHeight;const fov=camera.fov*Math.PI/180;const distance=Math.max(finalSize.y/2/Math.tan(fov/2),Math.max(finalSize.x,finalSize.z)*.55/(Math.tan(fov/2)*Math.min(aspect,1)))*1.45;resetPosition=new THREE.Vector3(Math.sin(startAngle)*distance,target.y+distance*(isRing?.65:.08),Math.cos(startAngle)*distance);camera.position.copy(resetPosition);controls.target.copy(target);controls.minDistance=radius*.55;controls.maxDistance=distance*2.3;controls.update();cinematicBase=resetPosition.clone();cinematicTarget=target.clone();}
 stage.append(canvas);function setSize(){if(disposed)return;renderer.setSize(stage.clientWidth,stage.clientHeight,false);camera.aspect=stage.clientWidth/stage.clientHeight;camera.updateProjectionMatrix();}
 fit();setSize();resize=new ResizeObserver(()=>{setSize();if(!stage.dataset.userMoved)fit()});resize.observe(stage);
 controls.addEventListener('start',()=>stage.dataset.userMoved='true');
 
 function rotate(delta){const offset=camera.position.clone().sub(controls.target);offset.applyAxisAngle(new THREE.Vector3(0,1,0),delta);camera.position.copy(controls.target).add(offset);stage.dataset.userMoved='true';controls.update()}
 function zoom(factor){stage.dataset.userMoved='true';const offset=camera.position.clone().sub(controls.target).multiplyScalar(factor);const distance=THREE.MathUtils.clamp(offset.length(),controls.minDistance,controls.maxDistance);offset.setLength(distance);camera.position.copy(controls.target).add(offset);controls.update()}
 const tools=stage.querySelector('.viewer-tools');tools.hidden=false;
 for(const button of tools.querySelectorAll('button')){button.onclick=async()=>{switch(button.dataset.view){case'left':rotate(-.25);break;case'right':rotate(.25);break;case'in':zoom(.85);break;case'out':zoom(1.18);break;case'reset':controls.autoRotate=false;fit();delete stage.dataset.userMoved;tools.querySelector('[data-view="rotate"]').setAttribute('aria-pressed','false');break;case'rotate':if(document.documentElement.classList.contains('motion-paused')){status.textContent='Resume motion using the page controls to enable auto rotation.';return}controls.autoRotate=!controls.autoRotate;button.setAttribute('aria-pressed',String(controls.autoRotate));break;case'full':try{if(document.fullscreenElement===stage)await document.exitFullscreen();else if(stage.requestFullscreen)await stage.requestFullscreen();else throw new Error('Fullscreen unavailable')}catch{status.textContent='Fullscreen is unavailable. Rotate and zoom in the embedded viewer.'}break;}}}
 canvas.addEventListener('keydown',e=>{if(['ArrowLeft','ArrowRight','ArrowUp','ArrowDown','+','=','-','r','R'].includes(e.key)){e.preventDefault();if(e.key==='ArrowLeft')rotate(-.15);else if(e.key==='ArrowRight')rotate(.15);else if(['ArrowUp','+','='].includes(e.key))zoom(.9);else if(['ArrowDown','-'].includes(e.key))zoom(1.1);else fit()}});
 canvas.addEventListener('webglcontextlost',e=>{e.preventDefault();dispose();status.textContent='The 3D session ended. The original image remains available.'});
 observer=new IntersectionObserver(([entry])=>{visible=entry.isIntersecting;if(visible&&!document.hidden&&!disposed){cancelAnimationFrame(raf);last=0;raf=requestAnimationFrame(frame)}},{threshold:.05});observer.observe(stage);
 window.addEventListener('halgan-motion',motionHandler);document.addEventListener('visibilitychange',visibilityHandler);
 // Keep at most two WebGL contexts active on lower-end devices.
 if(activeViewers.size>=2)activeViewers.values().next().value();activeViewers.add(dispose);
 stage.classList.add('loaded');stage.dataset.loading='false';status.textContent='Drag to rotate · Scroll or pinch to zoom · Arrow keys supported';raf=requestAnimationFrame(frame);canvas.focus({preventScroll:true});
 }catch(error){dispose();throw error;}
 return dispose;
}
