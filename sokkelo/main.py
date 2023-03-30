import pyxel
import carte
import menu
import character

def est_vide(liste):
    return liste == []

class App:
    def __init__(self):
        """Constructeur de l'application du jeu"""
        pyxel.init(256, 256, title="Sokkelo shooter")
        self.personnage = character.Personnage()
        self.ennemis = []
        pyxel.run(self.update, self.draw)
    
    def trape(self):
        """Affichage du passage au niveau suivant"""
        pyxel.load("assets/skin.pyxres")
        u = 0
        if est_vide(self.ennemis):
            if self.personnage.level == 1 or self.personnage.level == 2:
                pyxel.blt(232, 232, 0, 0, 16, 16, 16)
                u = 232
            elif self.personnage.level == 3 or self.personnage.level == 4:
                pyxel.blt(244, 244,0, 16, 16, 8, 8)
                u = 244
            elif self.personnage.level == 5:
                pyxel.blt(250, 250, 0, 18, 26, 4 ,4)
                u = 250
        if u != 0:
            if pyxel.btnp(pyxel.KEY_E):
                if self.personnage.level == 1 or self.personnage.level == 2:
                    dx = self.personnage.x + 16
                    dy = self.personnage.y + 16
                elif self.personnage.level == 3 or self.personnage.level == 4:
                    dx = self.personnage.x + 8
                    dy = self.personnage.y + 8
                elif self.personnage.level == 5:
                    dx = self.personnage.x + 4
                    dy = self.personnage.y + 4
                for i in range (self.personnage.x, dx):
                    for j in range (self.personnage.y, dy):
                        if i == u and j == u:
                            if self.personnage.level == 1:
                                self.personnage.x = 8
                                self.personnage.y = 8
                                self.personnage.level = 2
                            elif self.personnage.level == 2:
                                self.personnage.x = 4
                                self.personnage.y = 4
                                self.personnage.level = 3
                            elif self.personnage.level == 3:
                                self.personnage.x = 4
                                self.personnage.y = 4
                                self.personnage.level = 4
                            elif self.personnage.level == 4:
                                self.personnage.x = 2
                                self.personnage.y = 2
                                self.personnage.level = 5
                            elif self.personnage.level == 5:
                                self.personnage.level = 6
                            if not self.personnage.level == 6:
                                self.jeu()
                            else:
                                self.ecranFin()
                                
    def ecranFin(self):
        """Affichage de l'écran de fin du jeu"""
        pyxel.load("assets/ecrantitre.pyxres")
        pyxel.blt(0, 0, 2, 0, 0, 256, 256)
    
    def jeu (self):
        """Changement de niveau avec affichage"""
        if self.personnage.level == 1:
            pyxel.cls(0)
            carte.level_1(carte.map1)
        elif self.personnage.level == 2:
            carte.level_1(carte.map2)
        elif self.personnage.level == 3:
            carte.level_2(carte.map3)
        elif self.personnage.level == 4:
            carte.level_2(carte.map4)
        elif self.personnage.level == 5:
            carte.level_3(carte.map5)
        self.trape()
        self.personnage.drawPerso()
    
    
    def update(self):
        self.personnage.mouvement()
        self.trape()
    
    def draw(self):
        if not menu.page == "jeu":
            menu.affichage()
        else:
            self.jeu()

            
App()