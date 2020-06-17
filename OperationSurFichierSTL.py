import numpy as np

class operationSurLesFacettesEtLesNormales():
    def __init__(self, listeNormales, listeFacettes, masseBateau):

        self.__listeN = listeNormales
        self.__listeF = listeFacettes
        self.__masseBateau = masseBateau
        self.__forcePoids = self.__masseBateau * 9.8
        self.__forceArchimede = 0

        self.__coodDeG = []
        self.__forcesPression = []
        self.__niveauEau = 1
        self.__tirantEau = 0

    def getForcePoids(self):
        return self.__forcePoids
    def getForceArchimede(self):
        return self.__forceArchimede
    def getMassBateau(self):
        return self.__masseBateau
    def getNiveauEau(self):
        return self.__niveauEau
    def getTirantEau(self):
        return self.__tirantEau

    def setMasse(self, masse):
        self.__forcePoids = masse * 9.8
    def setNiveauEau(self, niveau):
        self.__niveauEau = niveau

    def pousseeArchimede(self):
        self.calculDesCoordonneesDesG()
        self.calculDesForcesDesPressions()
        self.tirantEau()
        PA = 0
        x = len(self.__forcesPression)
        for i in range(0, x):
            PA += self.__forcesPression[i]
        self.__forceArchimede = PA
        return self.__forceArchimede

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

    def calculDePressionFacetteImergee(self, indice):
        if self.__coodDeG[indice][2] < self.__niveauEau :
            rot = 1025
            g = 9.8
            pression = rot*g*self.__coodDeG[indice][2] #coordonnées des GZ
            return pression
        else:
            return 0

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

    def translationDesFacette(self, indiceDeTranslation):
        x = indiceDeTranslation
        for elt in range(0, len(self.__listeF)) :
            for elt2 in range(0, 3):
                self.__listeF[elt][elt2][-1] = self.__listeF[elt][elt2][-1] + x
        self.__tirantEau += x
        return self.__listeF

    def tirantEau(self):
        lst = []
        for i in range(0, len(self.__listeF)):
            for elt in range(0, 3):
                lst.append(self.__listeF[i][elt][2])
        pointLePlusBas = min(lst)
        return self.__niveauEau - pointLePlusBas
