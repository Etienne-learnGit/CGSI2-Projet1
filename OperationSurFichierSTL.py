import numpy as np

class operationSurLesFacettesEtLesNormales():
    def __init__(self, listeNormales, listeFacettes, masseBateau):
        self.__listeN = listeNormales
        self.__listeF = listeFacettes
        self.__masseBateau = masseBateau

        self.__coodDeG = []
        self.__forcesPression = []

        self.__forceArchimede = 0
        self.__forcePoids = 0

    def calculDesCoordonneesDesG(self):
        x = len(self.__listeF)
        for elt in range(0, x) :
            g = []
            X = (self.__listeF[elt][0][0] + self.__listeF[elt][1][0] + self.__listeF[elt][2][0]) / 3
            Y = (self.__listeF[elt][0][1] + self.__listeF[elt][1][1] + self.__listeF[elt][2][1]) / 3
            Z = (self.__listeF[elt][0][2] + self.__listeF[elt][1][2] + self.__listeF[elt][2][2]) / 3
            g.append(X)
            g.append(Y)
            g.append(Z)
            self.__coodDeG.append(g)
        return self.__coodDeG

    def calculDePressionFacetteImergee(self, indice):
        if self.__coodDeG[indice][2] < 1 :
            rot = 1025
            g = 9.8
            pression = rot*g*self.__coodDeG[indice][2] #coordonnées des GZ
            return pression
        else:
            return 0

    def calculDesForcesDesPressions(self):
        x = len(self.__listeF)
        for elt in range(0, x) :
            AB = np.array([self.__listeF[elt][1][0]-self.__listeF[elt][0][0],self.__listeF[elt][1][1]-self.__listeF[elt][0][1],self.__listeF[elt][1][2]-self.__listeF[elt][0][2]])
            AC = np.array([ self.__listeF[elt][2][0]-self.__listeF[elt][0][0],self.__listeF[elt][2][1]-self.__listeF[elt][0][1],self.__listeF[elt][2][2]-self.__listeF[elt][0][2]])
            vectSurface = np.cross(AB, AC) / 2
            normeSurface = np.vdot(vectSurface, vectSurface)**(1/2)
            forcePression = self.calculDePressionFacetteImergee(elt) * normeSurface
            self.__forcesPression.append(forcePression)
        return self.__forcesPression

    def pousseeArchimede(self):
        PA = 0
        x = len(self.__forcesPression)
        for i in range(0, x):
            PA += self.__forcesPression[i]
        self.__forceArchimede = PA
        return self.__forceArchimede

    def translationDesFacette(self, indiceDeTranslation):
        x = indiceDeTranslation
        for elt in range(0, len(self.__listeF)) :
            for elt2 in range(0, 3):
                self.__listeF[elt][elt2][-1] = self.__listeF[elt][elt2][-1] + x
        print("affichage liste Facettes apres transalation : ")
        print(self.__listeF)
        return self.__listeF

    def calculForcePoids(self):
        self.__forcePoids = int(input("Entrez la masse du Bateau : ")) * 9.8
        return self.__forcePoids
