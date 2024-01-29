import trimesh
import numpy as np

def calculate_shape_similarity(a_ply_file, b_ply_file, num_vertices=100000):
    # Load PLY files using trimesh
    a_mesh = trimesh.load(a_ply_file)
    b_mesh = trimesh.load(b_ply_file)

    # Resample meshes to have the same number of vertices
    a_vertices = a_mesh.sample(num_vertices)
    b_vertices = b_mesh.sample(num_vertices)

    # Perform the calculation
    differences = np.linalg.norm(a_vertices - b_vertices, axis=1)

    # Calculate the similarity metric (e.g., mean differences)
    similarity = np.mean(differences)

    return similarity

if __name__ == "__main__":
    a_ply_file = "a18.ply"
    b_ply_file = "18.ply"

    similarity = calculate_shape_similarity(a_ply_file, b_ply_file)
    print("Shape Similarity:", similarity)
