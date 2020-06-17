from PySide2.QtWidgets import *
import matplotlib as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from TracerDessinAvecFacette import *
from stl import mesh
from mpl_toolkits import mplot3d

class boatIHM(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Boat sinking interface")
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layoutF = QVBoxLayout()

        self.button1 = QPushButton("Load 3D Model")
        self.button2 = QPushButton("Load Image")
        self.button3 = QPushButton("Compute")

        self.layout1.addWidget(self.button1)
        self.layout1.addWidget(self.button2)
        self.layout1.addWidget(self.button3)

        self.image = graph()
        self.image2 = courbe()

        self.layout2.addWidget(self.image)
        self.layout2.addWidget(self.image2)

        self.layoutF.addLayout(self.layout1)
        self.layoutF.addLayout(self.layout2)

        self.setLayout(self.layoutF)

class graph(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        self.ax = plt.axes(projection='3d')
        self.affichageStructure('Maillage\Rectangular_HULL_Normals_Outward.stl')
        self.canvas.draw()

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def affichageStructure(self, chemin):
        your_mesh = mesh.Mesh.from_file(chemin)
        self.ax.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

        scale = your_mesh.points.flatten("C")
        self.ax.auto_scale_xyz(scale, scale, scale)
        return

class courbe(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        self.ax = plt.axes(projection='3d')

        self.affichageCourbe('Maillage\Rectangular_HULL_Normals_Outward.stl')
        self.canvas.draw()

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setLayout(layout)

    def affichageCourbe(self, chemin):
        your_mesh = mesh.Mesh.from_file(chemin)
        self.ax.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

        scale = your_mesh.points.flatten("C")
        self.ax.auto_scale_xyz(scale, scale, scale)
        return

if __name__ == "__main__":
   app = QApplication([])
   win = boatIHM()
   win.show()
   app.exec_()
