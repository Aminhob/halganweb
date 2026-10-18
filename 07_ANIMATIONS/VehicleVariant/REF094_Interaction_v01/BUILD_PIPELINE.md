# Rebuild provenance

The editable final variant is REF094_Interaction_v01.blend. Its verified FBX and Unity prefab are linked in the animation manifest and isolated validation project. Ordinary motion editing should use the retained Working/*.blend versions.

For a fresh geometry rebuild from the preserved approved original, run these Blender scripts in order, once each: Reports/Tools/build_ref094_interaction.py, raise_variant_headroom.py, refine_door_hinge.py. The first resets to the original; the next two are measured local geometry corrections and must not be applied repeatedly to the final native file. Revalidate after edits. Steering placement and its low-poly column are incorporated into the build script. Previous geometry is retained in Baseline and Blender backup revisions.

Validation scripts: qc_vehicle_variant.py (reopen/topology/hinge/original hash), qc_variant_self_detail.py (open door/body and steering clearance), HalganVariantFit20261018.cs (exact Noob CPU meshes, anchors and separate door motions), check_actual_vehicle_mesh.py (all-frame actual-geometry intersections). Character and vehicle poses are in CHARACTER_VEHICLE_ANCHORS.json / REF094_VARIANT.json; use their documented root-anchor contract. Android remains pending.
