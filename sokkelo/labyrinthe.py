import random
#import matplotlib.pyplot as plt


class Pile:
    """ définition d'une pile à l'aide de la classe List """
    def __init__(self):
        """constructeur de la classe Pile : cree une pile vide"""
        self.lst = []

    def est_vide(self):
        """renvoie un booleen indiquant si la pile est vide ou non """
        return self.lst == []

    def empiler(self, x):
        """empile x sur la pile"""
        self.lst.append(x)

    def depiler(self):
        """depile et renvoie l'élément au sommet de la pile"""
        if self.est_vide():
            raise ValueError("pile vide")
        return self.lst.pop()


class Case:
    def __init__(self):
        self.N = False
        self.W = False
        self.S = False
        self.E = False


class Labyrinthe:
    def __init__(self, p, q):
        self.nb_lignes = p
        self.nb_colonnes = q
        self.tab = [[Case() for j in range(q)] for i in range(p)]        
        
    def creer(self):
        pile = Pile()
        dejavu = [[False for j in range(self.nb_colonnes)] for i in range(self.nb_lignes)]
        i, j = random.randint(0,self.nb_lignes-1), random.randint(0,self.nb_colonnes-1)
        pile.empiler((i, j))
        dejavu[i][j] = True
        while not pile.est_vide():
            (i, j) = pile.depiler()
            v = []
            if j < self.nb_colonnes-1 and not dejavu[i][j+1]:
                v.append('E')
            if i > 0 and not dejavu[i-1][j]:
                v.append('N')
            if j > 0 and not dejavu[i][j-1]:
                v.append('W')
            if i < self.nb_lignes-1 and not dejavu[i+1][j]:
                v.append('S')
            if len(v) > 1:
                pile.empiler((i, j))
            if len(v) > 0:
                c = v[random.randint(0,len(v)-1)]
                if c == 'N':
                    self.tab[i][j].N = True
                    self.tab[i-1][j].S = True
                    dejavu[i-1][j] = True
                    pile.empiler((i-1, j))
                elif c == 'W':
                    self.tab[i][j].W = True
                    self.tab[i][j-1].E = True
                    dejavu[i][j-1] = True
                    pile.empiler((i, j-1))
                elif c == 'S':
                    self.tab[i][j].S = True
                    self.tab[i+1][j].N = True
                    dejavu[i+1][j] = True
                    pile.empiler((i+1, j))
                else:
                    self.tab[i][j].E = True
                    self.tab[i][j+1].W = True
                    dejavu[i][j+1] = True
                    pile.empiler((i, j+1))