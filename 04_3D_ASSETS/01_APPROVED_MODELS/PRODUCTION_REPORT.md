# HALGAN free-model production report

Production pass covers all **206** current Category 2/3 provisional designs: **169 resolved for this preparation stage**, **37 remaining** (8 partial exports and 29 missing usable models). This is not a claim that all 206 final assets are finished. REF labels remain audit inspection references; no original numbered IDs were invented.

## Design counts

| Category | Designs | Unity tested | Shared model | Ready import only | No separate mesh needed | Partial | Missing |
|---|---:|---:|---:|---:|---:|---:|---:|
| CATEGORY 2 | 116 | 59 | 17 | 0 | 8 | 3 | 29 |
| CATEGORY 3 | 90 | 77 | 8 | 0 | 0 | 5 | 0 |

There are **142 distinct prepared model families**: **14 licensed source families** and **128 original local families**. Multiple GLB, FBX, LOD, Blender and Unity prefab files are exports/variants, not additional acquired models. **136 model families** have at least one approved design. **25 resolved designs** reuse a preceding model family (SHARED_MODEL); **27 additional design mappings** reuse geometry when partial variants are included. Shared families spanning categories reside in `_SHARED_MODELS`. Each design remains traceable in the manifest.

Eight audit-supported no-separate-mesh decisions comprise six hidden internal component omissions and two supplied original decal candidates. These are conditional: restore hidden geometry if gameplay exposes internals; attach/bake decals to the appropriate parent. No glove/headgear fitted assembly or rig is falsely claimed. Stool seat/frame use named parts of one assembled model. Repeated static geometry is joined for lower renderer counts; not every repeated piece remains an editable linked instance.

## Delivered preparation

Metric nominal dimensions and useful ground/centre pivots; applied transforms, cleaned static geometry, reduced renderer count and embedded GLB textures. Local models generally use scalar PBR materials, with original detail maps where appropriate. Source textures capped at 1024px. LOD1/LOD2 generated for higher-detail models; thresholds require scene tuning. Wheel parts of the prepared pickup retain separate geometry pivots; there is no vehicle controller or driving test. All models are static and unrigged. Realistic characters and fitted clothing remain blocked rather than replaced with primitive humanoids.

Editable `.blend` files, export evidence JSON, previews, FBX/GLB and Unity packages reside within family folders. Downloaded originals and license evidence are retained separately. Source silhouettes were checked against reference/model sheets. Simplified generic background shapes were accepted for mobile use; complex or materially mismatched designs remain PARTIAL/MISSING with explicit per-design work. Reference photographs do not establish exact dimensions.

## Verification and limits

Blender successfully reopened all **142 GLB and FBX** LOD0 exports with nonempty finite geometry and resolving texture paths. Isolated Unity **6000.6.4f1 / URP 17.6.0** editor imports: **142/142 passed**. Checks include triangle count, metre-scale bounds, PBR texture assignment, URP/Lit materials, prefab and applicable LODGroup creation. Detailed failures, if any, are in `FINAL_VERIFICATION.json`. **UNITY_TESTED means these editor import checks only.** It does not mean Android, in-game rendering, animation, cloth deformation, collision interaction or driving passed.

All **240 currently existing organized reference images** match the audit SHA-256 hashes, including all **218 Category 2/3 inputs** and Category 1. One out-of-scope audited review image is absent; see the discrepancy below. All 63 completed downloaded payload files match their original recorded hashes. Category 1/review folders, original image bytes and existing V1 game projects were not modified. Validation used the separate `_REPORTS/UNITY_VALIDATION_PROJECT`. No money or paid AI credits were used.

## Import and remaining work

Use the per-family `HALGAN.unitypackage` and the design-specific REF prefab listed in the manifest. The aggregate `HALGAN_PREPARED_MODELS.unitypackage` contains both approved and partial baselines; consult the manifest before using a partial. FBX alone will not supply Unity URP materials, colour variants or LOD prefabs. Import instructions and remaining validation are in `UNITY_IMPORT_GUIDE.md`.

Remaining clothed NPCs, garments/shoes and partial protective equipment, vehicles and tree have per-design blockers in `MISSING_ASSETS.md`. The mannequin and pressure washer are already validated. The completed oak baseline replaces the failed Jacaranda attempt but remains subject to its own reference-fit assessment. No unverified availability claim is made. Suitable human/outfit bases need license, fit, deformation and art review; source candidates which were too stylized or paid were rejected. Some environment/cloth baselines need authored surface, layout and drape work. Each row carries its concrete remaining work.

## Audit/source discrepancy

The audit references a Needs Review image whose path is absent. The entire `04_NEEDS_REVIEW` folder is absent from the current source tree. No production operation recreated, moved or deleted it; the audit path was used as a read-only verification reference. This prevents a claim that all 241 audited images currently exist. Its absence does not change the 206 scoped design rows.

- Missing audited path: `C:\Users\pc\Documents\HALGAN ASSETS\image-to-3D assets\04_NEEDS_REVIEW\Minimalist Crimson Framed Panel\Minimalist Crimson Framed Panel.png`; expected SHA-256 `a9475197c85753e985a0237e757838613b0c3eeb0129a2eddeb645a3995336a9`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 161 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 161 model-backed designs use 136 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 162 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 162 model-backed designs use 137 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 164 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 164 model-backed designs use 139 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 169 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 169 model-backed designs use 144 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 172 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 172 model-backed designs use 147 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 175 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 175 model-backed designs use 150 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 175 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 175 model-backed designs use 150 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 176 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 176 model-backed designs use 151 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 179 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 179 model-backed designs use 154 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 181 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 181 model-backed designs use 156 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 183 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 183 model-backed designs use 158 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 185 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 185 model-backed designs use 160 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 189 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 189 model-backed designs use 164 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 192 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 192 model-backed designs use 167 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 193 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 193 model-backed designs use 168 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 194 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 194 model-backed designs use 169 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 195 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 195 model-backed designs use 170 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 196 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 196 model-backed designs use 171 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 197 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 197 model-backed designs use 172 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 198 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 198 model-backed designs use 173 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.
