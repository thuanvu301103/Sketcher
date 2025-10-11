import bpy
import numpy as np
import bmesh
import os

# Load numpy file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MESH_DIR = os.path.join(BASE_DIR, "mesh.npy")
meshes = np.load(MESH_DIR, allow_pickle=True)

if isinstance(meshes, np.ndarray):
    meshes = meshes.tolist()
    print(meshes[0])

print("Loaded", len(meshes), "meshes")

def create_face(name, verts_np, faces_np=None):
    """
    Create a Face Object in Blender from vertex data.
    If no face indices are provided, automatically connect all vertices in order.

    Args:
        name (str):
            The name of the face object to create in Blender.

        verts_np (np.ndarray):
            A 2D NumPy array of shape (N, 3) containing vertex coordinates.
            Each row represents one vertex: [x, y, z].
            Example:
                [[0, 0, 0],
                 [1, 0, 0],
                 [1, 1, 0],
                 [0, 1, 0]]

        faces_np (np.ndarray | None, optional):
            A 2D NumPy array of shape (M, K) containing vertex indices
            that define each face. Each row lists vertex indices for one face.
            If not provided, one polygon face will be created
            connecting all vertices in order.

    Returns:
        bpy.types.Object:
            The Blender Object containing the created face(s),
            linked to the current scene collection.

    Example:
        >>> verts = np.array([[0,0,0],[1,0,0],[1,1,0],[0,1,0]])
        >>> obj = create_face("auto_face", verts)
    """

    verts = [tuple(v.tolist()) for v in verts_np]

    if faces_np is None:
        faces = [tuple(range(len(verts)))]
    else:
        faces = [tuple(map(int, f)) for f in faces_np]

    mesh = bpy.data.meshes.new(name + "_mesh")
    obj = bpy.data.objects.new(name, mesh)

    bpy.context.collection.objects.link(obj)

    mesh.from_pydata(verts, [], faces)
    mesh.update()

    return obj

# Delete all objects that have name started with "mesh_"
for obj in list(bpy.data.objects):
    if obj.name.startswith("mesh_"):
        bpy.data.objects.remove(obj, do_unlink=True)

for i, m in enumerate(meshes):  # i: index; m: vertices
    name = f"mesh_{i}"
    if isinstance(m, (list, np.ndarray)) and np.array(m).ndim == 2:
        create_face(name, np.array(m))
    elif isinstance(m, dict) and "vertices" in m:
        create_face(name, np.array(m["vertices"]), np.array(m.get("faces", None)))
    else:
        print(f"Can not process format of mesh[{i}] -> {type(m)}")

print("✅ Meshed are created")
