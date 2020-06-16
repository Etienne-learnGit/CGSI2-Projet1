from PySide2.QtWidgets import *
import matplotlib as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasAgg as FigureCanvas
from TracerDessinAvecFacette import *
from stl import mesh
from mpl_toolkits import mplot3d

class BoatIHM(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Boat sinking interface")
        #self.setMinimumSize(500,300)
        self.layout1 = QHBoxLayout()
        self.layout2 = QHBoxLayout()
        self.layoutF = QVBoxLayout()

        self.button1 = QPushButton("Load 3D Model")
        self.button2 = QPushButton("Load Image")
        self.button3 = QPushButton("Compute")

        self.layout1.addWidget(self.button1)
        self.layout1.addWidget(self.button2)
        self.layout1.addWidget(self.button3)

        self.image = test()
        self.text = QTextEdit("computation started...")

        self.layout2.addWidget(self.image)
        self.layout2.addWidget(self.text)

        self.layoutF.addLayout(self.layout1)
        self.layoutF.addLayout(self.layout2)

        self.setLayout(self.layoutF)

class test(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.fig = plt.figure()
        self.canvas = FigureCanvas(self.fig)
        ax = plt.axes(projection='3d')

        self.affichageStructure('Maillage\Rectangular_HULL.stl')

        self.canvas.draw()

        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        self.setlayout(layout)

    def affichageStructure(self, chemin):
        figure = plt.figure()
        axes = mplot3d.Axes3D(figure)
        your_mesh = mesh.Mesh.from_file(chemin)
        axes.add_collection3d(mplot3d.art3d.Poly3DCollection(your_mesh.vectors))

        scale = your_mesh.points.flatten("C")
        axes.auto_scale_xyz(scale, scale, scale)

if __name__ == "__main__":
   app = QApplication([])
   win = BoatIHM()
   win.show()
   app.exec_()
