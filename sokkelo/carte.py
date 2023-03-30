import pyxel
import labyrinthe

map1 = labyrinthe.Labyrinthe(8,8) #On créer la première carte de taille 8 case x 8 case
map1.creer()

map2 = labyrinthe.Labyrinthe(8,8) #On créer la deuxième carte de taille 8 case x 8 case
map2.creer()

map3 = labyrinthe.Labyrinthe(16,16) #On créer la troisième carte de taille 16 case x 16 case
map3.creer()

map4 = labyrinthe.Labyrinthe(16,16) #On créer la quatrième carte de taille 16 case x 16 case
map4.creer()

map5 = labyrinthe.Labyrinthe(32,32) #On créer la cinquième carte de taille 32 case x 32 case
map5.creer()

def level_1(laby):
    """Transforme le labyrinthe en argument de taille 8x8 sur pyxel"""
    pyxel.load("assets/map.pyxres")
    for i in range (len(laby.tab)):
        for j in range (len(laby.tab[i])):
            if laby.tab[i][j].N and laby.tab[i][j].S and laby.tab[i][j].W and laby.tab[i][j].E: #chemin dans les 4 directions
                pyxel.blt(32*j, 32*i, 0, 32, 192, 32, 32)
            elif laby.tab[i][j].N and laby.tab[i][j].S and not laby.tab[i][j].W and laby.tab[i][j].E: #pas de chemin vers la gauche
                pyxel.blt(32*j, 32*i, 0, 32, 160, 32, 32)
            elif laby.tab[i][j].N and not laby.tab[i][j].S and laby.tab[i][j].W and laby.tab[i][j].E: #pas de chemin vers le bas
                pyxel.blt(32*j, 32*i, 0, 32, 128, 32, 32)
            elif laby.tab[i][j].N and laby.tab[i][j].S and laby.tab[i][j].W and not laby.tab[i][j].E: #pas de chemin vers la droite
                pyxel.blt(32*j, 32*i, 0, 0, 224, 32, 32)
            elif not laby.tab[i][j].N and laby.tab[i][j].S and laby.tab[i][j].W and laby.tab[i][j].E: #pas de chemin vers le haut
                pyxel.blt(32*j, 32*i, 0, 0, 192, 32, 32)
            elif not laby.tab[i][j].N and not laby.tab[i][j].S and laby.tab[i][j].W and laby.tab[i][j].E: #chemin vers la gauche et vers la droite
                pyxel.blt(32*j, 32*i, 0, 0, 160, 32, 32)
            elif not laby.tab[i][j].N and laby.tab[i][j].S and not laby.tab[i][j].W and laby.tab[i][j].E: #chemin vers le bas et vers la droite
                pyxel.blt(32*j, 32*i, 0, 0, 128, 32, 32)
            elif not laby.tab[i][j].N and laby.tab[i][j].S and laby.tab[i][j].W and not laby.tab[i][j].E: #chemin vers le bas et vers la gauche
                pyxel.blt(32*j, 32*i, 0, 32, 96, 32, 32)
            elif laby.tab[i][j].N and not laby.tab[i][j].S and not laby.tab[i][j].W and laby.tab[i][j].E: #chemin vers le haut et la droite
                pyxel.blt(32*j, 32*i, 0, 32, 64, 32, 32)
            elif laby.tab[i][j].N and not laby.tab[i][j].S and laby.tab[i][j].W and not laby.tab[i][j].E: #chemin vers le haut et la gauche
                pyxel.blt(32*j, 32*i, 0, 32, 32, 32, 32)
            elif laby.tab[i][j].N and laby.tab[i][j].S and not laby.tab[i][j].W and not laby.tab[i][j].E: #chemin vers le haut et le bas
                pyxel.blt(32*j, 32*i, 0, 32, 0, 32, 32)
            elif not laby.tab[i][j].N and not laby.tab[i][j].S and not laby.tab[i][j].W and laby.tab[i][j].E: #chemin vers la droite
                pyxel.blt(32*j, 32*i, 0, 0, 96, 32, 32)
            elif not laby.tab[i][j].N and not laby.tab[i][j].S and laby.tab[i][j].W and not laby.tab[i][j].E: #chemin vers la gauche
                pyxel.blt(32*j, 32*i, 0, 0, 64, 32, 32)
            elif not laby.tab[i][j].N and laby.tab[i][j].S and not laby.tab[i][j].W and not laby.tab[i][j].E: #chemin vers le bas
                pyxel.blt(32*j, 32*i, 0, 0, 32, 32, 32)
            elif laby.tab[i][j].N and not laby.tab[i][j].S and not laby.tab[i][j].W and not laby.tab[i][j].E: #chemin vers le haut
                pyxel.blt(32*j, 32*i, 0, 0, 0, 32, 32)

def level_2(laby):
    """Transforme le labyrinthe en argument de taille 16x16 sur pyxel"""
    pyxel.load("assets/map.pyxres")
    for i in range (len(laby.tab)):
        for j in range (len(laby.tab[i])):
            if laby.tab[i][j].N and laby.tab[i][j].S and laby.tab[i][j].W and laby.tab[i][j].E:
                pyxel.blt(16*j, 16*i, 0, 64, 224, 16, 16)
            elif laby.tab[i][j].N and laby.tab[i][j].S and not laby.tab[i][j].W and laby.tab[i][j].E:
                pyxel.blt(16*j, 16*i, 0, 64, 208, 16, 16)
            elif laby.tab[i][j].N and not laby.tab[i][j].S and laby.tab[i][j].W and laby.tab[i][j].E:
                pyxel.blt(16*j, 16*i, 0, 64, 192, 16, 16)
            elif laby.tab[i][j].N and laby.tab[i][j].S and laby.tab[i][j].W and not laby.tab[i][j].E:
                pyxel.blt(16*j, 16*i, 0, 64, 176, 16, 16)
            elif not laby.tab[i][j].N and laby.tab[i][j].S and laby.tab[i][j].W and laby.tab[i][j].E:
                pyxel.blt(16*j, 16*i, 0, 64, 160, 16, 16)
            elif not laby.tab[i][j].N and not laby.tab[i][j].S and laby.tab[i][j].W and laby.tab[i][j].E:
                pyxel.blt(16*j, 16*i, 0, 64, 80, 16, 16)
            elif not laby.tab[i][j].N and laby.tab[i][j].S and not laby.tab[i][j].W and laby.tab[i][j].E:
                pyxel.blt(16*j, 16*i, 0, 64, 64, 16, 16)
            elif not laby.tab[i][j].N and laby.tab[i][j].S and laby.tab[i][j].W and not laby.tab[i][j].E: 
                pyxel.blt(16*j, 16*i, 0, 64, 144, 16, 16)
            elif laby.tab[i][j].N and not laby.tab[i][j].S and not laby.tab[i][j].W and laby.tab[i][j].E:
                pyxel.blt(16*j, 16*i, 0, 64, 128, 16, 16)
            elif laby.tab[i][j].N and not laby.tab[i][j].S and laby.tab[i][j].W and not laby.tab[i][j].E:
                pyxel.blt(16*j, 16*i, 0, 64, 112, 16, 16)
            elif laby.tab[i][j].N and laby.tab[i][j].S and not laby.tab[i][j].W and not laby.tab[i][j].E:
                pyxel.blt(16*j, 16*i, 0, 64, 96, 16, 16)
            elif not laby.tab[i][j].N and not laby.tab[i][j].S and not laby.tab[i][j].W and laby.tab[i][j].E:
                pyxel.blt(16*j, 16*i, 0, 64, 48, 16, 16)
            elif not laby.tab[i][j].N and not laby.tab[i][j].S and laby.tab[i][j].W and not laby.tab[i][j].E:
                pyxel.blt(16*j, 16*i, 0, 64, 32, 16, 16)
            elif not laby.tab[i][j].N and laby.tab[i][j].S and not laby.tab[i][j].W and not laby.tab[i][j].E:
                pyxel.blt(16*j, 16*i, 0, 64, 16, 16, 16)
            elif laby.tab[i][j].N and not laby.tab[i][j].S and not laby.tab[i][j].W and not laby.tab[i][j].E:
                pyxel.blt(16*j, 16*i, 0, 64, 0, 16, 16)

def level_3(laby):
    """Transforme le labyrinthe en argument de taille 32x32 sur pyxel"""
    pyxel.load("assets/map.pyxres")
    for i in range (len(laby.tab)):
        for j in range (len(laby.tab[i])):
            if laby.tab[i][j].N and laby.tab[i][j].S and laby.tab[i][j].W and laby.tab[i][j].E:
                pyxel.blt(8*j, 8*i, 0, 80, 112, 8, 8)
            elif laby.tab[i][j].N and laby.tab[i][j].S and not laby.tab[i][j].W and laby.tab[i][j].E:
                pyxel.blt(8*j, 8*i, 0, 80, 88, 8, 8)
            elif laby.tab[i][j].N and not laby.tab[i][j].S and laby.tab[i][j].W and laby.tab[i][j].E:
                pyxel.blt(8*j, 8*i, 0, 80, 96, 8, 8)
            elif laby.tab[i][j].N and laby.tab[i][j].S and laby.tab[i][j].W and not laby.tab[i][j].E:
                pyxel.blt(8*j, 8*i, 0, 80, 104, 8, 8)
            elif not laby.tab[i][j].N and laby.tab[i][j].S and laby.tab[i][j].W and laby.tab[i][j].E:
                pyxel.blt(8*j, 8*i, 0, 80, 80, 8, 8)
            elif not laby.tab[i][j].N and not laby.tab[i][j].S and laby.tab[i][j].W and laby.tab[i][j].E:
                pyxel.blt(8*j, 8*i, 0, 80, 40, 8, 8)
            elif not laby.tab[i][j].N and laby.tab[i][j].S and not laby.tab[i][j].W and laby.tab[i][j].E:
                pyxel.blt(8*j, 8*i, 0, 80, 32, 8, 8)
            elif not laby.tab[i][j].N and laby.tab[i][j].S and laby.tab[i][j].W and not laby.tab[i][j].E: 
                pyxel.blt(8*j, 8*i, 0, 80, 72, 8, 8)
            elif laby.tab[i][j].N and not laby.tab[i][j].S and not laby.tab[i][j].W and laby.tab[i][j].E:
                pyxel.blt(8*j, 8*i, 0, 80, 64, 8, 8)
            elif laby.tab[i][j].N and not laby.tab[i][j].S and laby.tab[i][j].W and not laby.tab[i][j].E:
                pyxel.blt(8*j, 8*i, 0, 80, 56, 8, 8)
            elif laby.tab[i][j].N and laby.tab[i][j].S and not laby.tab[i][j].W and not laby.tab[i][j].E:
                pyxel.blt(8*j, 8*i, 0, 80, 48, 8, 8)
            elif not laby.tab[i][j].N and not laby.tab[i][j].S and not laby.tab[i][j].W and laby.tab[i][j].E:
                pyxel.blt(8*j, 8*i, 0, 80, 24, 8, 8)
            elif not laby.tab[i][j].N and not laby.tab[i][j].S and laby.tab[i][j].W and not laby.tab[i][j].E:
                pyxel.blt(8*j, 8*i, 0, 80, 16, 8, 8)
            elif not laby.tab[i][j].N and laby.tab[i][j].S and not laby.tab[i][j].W and not laby.tab[i][j].E:
                pyxel.blt(8*j, 8*i, 0, 80, 8, 8, 8)
            elif laby.tab[i][j].N and not laby.tab[i][j].S and not laby.tab[i][j].W and not laby.tab[i][j].E:
                pyxel.blt(8*j, 8*i, 0, 80, 0, 8, 8)