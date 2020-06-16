import matplotlib.pyplot as plt
from stl import mesh
from mpl_toolkits import mplot3d

def affichageStructure(chemin):
    figure = plt.figure()
    axes = mplot3d.Axes3D(figure)
    your_mesh = mesh.Mesh.from_file(chemin)
    axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

    scale = your_mesh.points.flatten("C")
    axes.auto_scale_xyz(scale, scale, scale)
    plt.show()

#affichageStructure('Maillage\Rectangular_HULL.stl')
