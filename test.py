from OperationSurFichierSTL import *

chemin = r"Maillage\V_HULL.stl"
STL1 = extractionSTL(chemin)
listeN, listeF = STL1.extractionDesListes()
#print(listeN)
#print(listeF)

objetSTL1 = operationSurLesFacettesEtLesNormales(listeN, listeF, 1500)

lstCoordonneesDeG = objetSTL1.calculDesCoordonneesDesG()
print("coordonnees de tous les g : ")
print(lstCoordonneesDeG)

forcesDePression = objetSTL1.calculDesForcesDesPressions()
print("Toutes les forces de pressions des facettes immergees : ")
print(forcesDePression)

PA = objetSTL1.pousseeArchimede()
print("pousse Archimede : ")
print(PA)
