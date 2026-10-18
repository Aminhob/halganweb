# Unity import guide

1. Back up your target Unity project before integrating any art. Use a separate art branch or staging folder. Existing V1 was left untouched.
2. Use Unity 6000.6.4f1 with URP 17.6.0, or validate compatibility in your own version. Import a family `unity_ready/HALGAN.unitypackage`; the package includes URP/Lit materials, applicable LODs and per-design REF prefabs.
3. Select the manifest-listed design prefab, especially for colour variants and stool components. Direct FBX imports need the exported textures/PBR material configuration and will not reproduce prefabs automatically. GLB was reopened in Blender, but Unity GLB import was not tested and needs a compatible importer.
4. Keep MISSING/NOT_NEEDED entries out of model loading; NOT_NEEDED decal rows include original 2D textures for parent attachment. PARTIAL rows are usable technical baselines with unresolved art requirements, not approved final replacements.
5. Tune pivots, nominal dimensions, LOD distances, texture compression and material instancing for actual cameras, draw distance and Android device. Glass uses transparent URP materials; assess sorting/overdraw. Scalar materials and generated patterns are intentionally simplified.
6. BoxColliders are coarse bounds for static props. Disable/replace them for roads, shelves, usable doors, seats, components, vehicle wheels and any passageways. Openings and named-component prefabs need gameplay-specific collision. No drivable controllers, rigs, skinned clothing, animations or cloth simulation are provided.
7. Test scene lighting, actual asset texture UV density, normals, collision and gameplay. Make an Android build and measure GPU/CPU frame time, memory, draw calls and overdraw on target devices. These steps remain pending.

The aggregate package includes partial baselines as well as approved families. The manifest status is the source of truth. The isolated validation project is evidence/staging, not a replacement HALGAN game. Production scripts save per-family checkpoints in MODEL_RESULTS.json; resume from the manifest and original plan rather than recreating completed exports. Do not rerun the initial plan script blindly, because it records initial pending statuses.

## Approved design package

`HALGAN_APPROVED_DESIGNS.unitypackage` contains all 161 approved design-specific prefabs and their model/material/texture dependencies. Package contents were verified against the manifest; no partial prefab was included. The 161 model-backed designs use 136 distinct model families. Four approved headgear components use isolated Mesh assets copied without geometry changes, excluding the mixed approved/partial FBX dependency. Their package-prefab paths are recorded in the manifest and APPROVED_PACKAGE_MAP.json. Eight audit-supported omission/decal designs are recorded separately. The all-model package remains available for partial baseline review. Package SHA-256 and contents are recorded in `APPROVED_PACKAGE_VERIFICATION.json`.

Use HALGAN_APPROVED_DESIGNS.unitypackage for approved-only import. For REF037/205/206/207, use the Approved package prefab column: isolated prefabs are under Assets/HALGAN_ApprovedComponents and preserve approved geometry while excluding the partial headgear FBX. The canonical Unity prefab column remains the source staging path and is not the package path for those four components. Rigged compatibility/fitting fixtures are separate evidence and excluded from the approved package.

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
