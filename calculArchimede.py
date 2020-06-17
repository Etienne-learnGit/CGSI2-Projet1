import numpy
from Programme_Mere import *

def calculForcePression(N, F):
    rot = 1025
    g = 9.8
    AB = numpy.array([F[1][0]-F[0][0], F[1][1]-F[0][1],F[1][2]-F[0][2]])
    AC = numpy.array([F[2][0]-F[0][0], F[2][1]-F[0][1], F[2][2]-F[0][2]])
    normale = numpy.array([N[0], N[1], N[2]])
    produitVectoriel = numpy.cross(AB, AC)
    dS = numpy.linalg.norm(produitVectoriel) / 2
    zG = (F[0][2] + F[1][2] + F[2][2]) / 3
    FPression = -rot*g*dS*normale*zG
    return FPression

def pousseeArchimede(lstN, lstF):
    PA = [0,0,0]
    for i in range(0, len(lstF)):
        zG = (lstF[i][0][2] + lstF[i][1][2] + lstF[i][2][2]) / 3
        if zG < 1:
            PA[0] += calculForcePression(lstN[i], lstF[i])[0]
            PA[1] += calculForcePression(lstN[i], lstF[i])[1]
            PA[2] += calculForcePression(lstN[i], lstF[i])[2]
    print("Force d'Archimede : ", PA)
    return PA

def forcePoids(masseBateau):
    print("Force du poids : ", masseBateau*9.8)
    return masseBateau*9.8

chemin, masseboat, listN, listF = start()
pousseeArchimede(listN, listF)
forcePoids(masseboat)


"""NTriangle = [-0, 0.70710678118654746, -0.70710678118654746]
FTriangle = [[4, 0, 0], [0, 1, 1], [4, 1, 1]]

NRectangle = [0, -1, -0]
FRectangle = [[0, -1, 0], [2, -1, 0], [2, -1, 1]]

print(calculForcePression(NTriangle,FTriangle))
print(calculForcePression(NRectangle,FRectangle))"""

