import rhinoscriptsyntax as rs
import Rhino
import System
import math

def merge_coplanar_mesh_faces():
    """
    1) Select multiple mesh objects.
    2) Combine them into one mesh and weld them fully.
    3) Prompt user for angle tolerance (in degrees) for merging.
    4) Call AddPlanarNgons(...) to merge coplanar faces into n-gons.
    (Requires Rhino 7+)
    """
    # 1) Select mesh objects
    mesh_ids = rs.GetObjects("Select mesh(es) to merge coplanar faces", rs.filter.mesh)
    if not mesh_ids:
        return

    # 2) Prompt for angle tolerance in degrees
    angle_deg = rs.GetReal("Angle tolerance (deg) for merging faces", 0.0, 0.0)
    if angle_deg is None:
        return
    angle_rad = math.radians(angle_deg)

    doc = Rhino.RhinoDoc.ActiveDoc

    # Combine selected meshes into one
    combined_mesh = Rhino.Geometry.Mesh()
    for mid in mesh_ids:
        rhobj = doc.Objects.Find(mid)
        if not rhobj: 
            continue
        mesh_geo = rhobj.Geometry
        if not isinstance(mesh_geo, Rhino.Geometry.Mesh):
            continue
        # Append it to combined
        combined_mesh.Append(mesh_geo)

    # If the combined_mesh is empty or invalid
    if combined_mesh.Faces.Count == 0:
        print("No valid mesh faces found.")
        return

    # 3) Weld the mesh to unify edges (180 degrees => fully weld)
    combined_mesh.Weld(math.pi)  # pi radians ~ 180 degrees

    # 4) AddPlanarNgons merges adjacent coplanar faces
    # This modifies the mesh so that sets of coplanar triangles/quads become n-gons
    combined_mesh.Ngons.AddPlanarNgons(angle_rad)

    # 5) Replace or create new mesh in doc
    # Option A: add a new mesh object to doc and remove old ones
    new_id = doc.Objects.AddMesh(combined_mesh)
    for mid in mesh_ids:
        rs.DeleteObject(mid)

    doc.Views.Redraw()
    print("Merged coplanar faces on the combined mesh with angle tolerance {} deg.".format(angle_deg))

def main():
    merge_coplanar_mesh_faces()

if __name__ == "__main__":
    main()
