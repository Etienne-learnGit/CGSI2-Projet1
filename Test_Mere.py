from Programme_Mere import *
from OperationSurFichierSTL import *

#Test ProgrammeMere
chemin, masseboat, listeN, listeF = start()

#Test Operation sur STL
B1 = operationSurLesFacettesEtLesNormales(listeN, listeF, masseboat)
#print("coordonnees des g : ",B1.calculDesCoordonneesDesG())
#print("Les forces de pressions : ", B1.calculDesForcesDesPressions())
print(B1.calculDesForcesDesPressions())
print("pousse Archimede : ", B1.pousseeArchimede())
print("Hauteur maximal : ", B1.getHauteurMax())
print("Niveau Eau : ", B1.getNiveauEau())
print("Force Poids : ", B1.getForcePoids()) #4000 kg pour le rectangle
