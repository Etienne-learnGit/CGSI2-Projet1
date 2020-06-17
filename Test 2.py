from Programme_Mere import *
from OperationSurFichierSTL import *

#Test ProgrammeMere
chemin, masseboat, listeN, listeF = start()

#Test Operation sur Fichiers STL
objetSTL1 = operationSurLesFacettesEtLesNormales(listeN, listeF, masseboat)

lstCoordonneesDeG = objetSTL1.calculDesCoordonneesDesG()
print("coordonnees de tous les g : ")
print(lstCoordonneesDeG)

forcesDePression = objetSTL1.calculDesForcesDesPressions()
print("Toutes les forces de pressions des facettes immergees : ")
print(forcesDePression)

PA = objetSTL1.pousseeArchimede()
print("pousse Archimede : ")
print(PA)
