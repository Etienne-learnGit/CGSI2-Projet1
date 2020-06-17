from Programme_Mere import *

#Test ProgrammeMere
chemin, masseboat, listeN, listeF = start()

#Test Operation sur STL
B1 = operationSurLesFacettesEtLesNormales(listeN, listeF, masseboat)
#print("coordonnees des g : ",B1.calculDesCoordonneesDesG())
#print("Les forces de pressions : ", B1.calculDesForcesDesPressions())
print("pousse Archimede : ", B1.pousseeArchimede())
