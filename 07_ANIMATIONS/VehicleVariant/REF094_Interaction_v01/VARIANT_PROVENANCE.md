# REF094 interaction-ready working variant

Source: manifest-approved REF094_HATCH_FINAL447 working/HALGAN.blend and unity_ready/HALGAN_LOD0.fbx. Original model and licence records are preserved. Original SHA256: 46bcfd2e087dd43a89ec322aa91debc465746822ca5880606b42e6144731a6f0. Retained licence restrictions include no standalone asset-pack resale. No new external assets or paid services used.

The variant extracts the original driver exterior into a rigid hinged door and cuts a real opening. Added low-poly seat, cushion, backrest/headrest, footwell, sill, trim, wheel and column. The upper cabin/window frame and matching door have a smooth high-roof reprofile (initial 90mm plus 120mm local headroom refinement). Total 83,081 triangles, largely inherited exterior; authored interior about 752 triangles. Android performance is untested.

Native metres: +X driver side, -Y forward, Z up. Unity XYZ=(-nativeX,nativeZ,-nativeY), so LHD driver is Unity -X. Native hinge (.89,-1.18,.77) opens -90deg around Z; imported hinge Unity(-.89,.77,1.18) opens +90deg around Y. Exact anchors and hashes: Reports/Preparation/Completion/REF094_VARIANT.json. Geometry reopening, topology and hinge checks: VARIANT_GEOMETRY_QC.json. Current approval is determined by Approved/APPROVED_MANIFEST.json and the two meshfit_Car_*.json reports, not this provenance note.

DoorMotion holds four editable Unity .anim assets and rotation-validation reports. Enter: hold initial standing pose during a 0.667s pre-roll open, then play entry and its closing curve. Exit: play seated-to-standing and its opening curve, then hold final standing pose during a 0.667s post-roll close. Full held-character door sweeps and complete body transitions are checked against actual geometry.

At enter-to-exit handoff, restore actor rotation to the original vehicle-anchor frame and translate actor root to preserve outgoing world hip position. Use vehicle-anchor rotation when rotated, rather than identity. See handoff_Car_Enter_Car_Exit.json. Original-position curves retain authored offsets, so direct uncorrected swaps are not approved. Neutral seated hands are not certified driving-wheel grip. Other vehicles need separate fitting. Production gameplay/controllers were not changed or integrated.

Final hinge refinement preserves closed geometry, moves the pivot to the outer front edge, and adds 4mm lower-edge / 3mm rear-edge clearance. Sampled open-door sweep has zero coachwork intersections; all steering parts clear coachwork/glass. All four wheel minima are exactly ground Z=0. Evidence: VARIANT_SELF_QC.json.
