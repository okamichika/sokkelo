import pyxel
import random

class Personnage:
    def __init__(self, direction="right"):
        """constructeur de la classe personnage"""
        self.speed = 1
        self.direction = direction
        self.x = 8
        self.y = 8
        self.level = 1
    
    def drawPerso (self):
        """affichage du personnage sur l'écran du jeu"""
        pyxel.load("assets/skin.pyxres")
        if self.direction == "right":
            if self.level == 1 or self.level == 2:
                pyxel.blt(self.x, self.y, 0, 0, 48, 16, 16, 0)
            elif self.level == 3 or self.level == 4:
                pyxel.blt(self.x, self.y, 0, 0, 0, 8, 8, 0)
            elif self.level == 5:
                pyxel.blt(self.x, self.y, 0, 2, 42, 4, 4, 0)
        elif self.direction == "up":
            if self.level == 1 or self.level == 2:
                pyxel.blt(self.x, self.y, 0, 0, 64, 16, 16, 0)
            elif self.level == 3 or self.level == 4:
                pyxel.blt(self.x, self.y, 0, 0, 8, 8, 8, 0)
            elif self.level == 5:
                pyxel.blt(self.x, self.y, 0, 10, 42, 4, 4, 0)
        elif self.direction == "left":
            if self.level == 1 or self.level == 2:
                pyxel.blt(self.x, self.y, 0, 16, 64, 16, 16, 0)
            elif self.level == 3 or self.level == 4:
                pyxel.blt(self.x, self.y, 0, 8, 8, 8, 8, 0)
            elif self.level == 5:
                pyxel.blt(self.x, self.y, 0, 10, 34, 4, 4, 0)
        elif self.direction == "down":
            if self.level == 1 or self.level == 2:
                pyxel.blt(self.x, self.y, 0, 16, 48, 16, 16, 0)
            elif self.level == 3 or self.level == 4:
                pyxel.blt(self.x, self.y, 0, 8, 0, 8, 8, 0)
            elif self.level == 5:
                pyxel.blt(self.x, self.y, 0, 2, 34, 4, 4, 0)
        
    def collision(self):
        """vérifie la colision avec les murs"""
        dx = 0
        dy = 0
        if self.direction == "right":
            if self.level == 1 or self.level == 2:
                dx = self.x + 16
                dy = self.y + 16
            elif self.level == 3 or self.level == 4:
                dx = self.x + 8
                dy = self.y + 8
            else:
                dx = self.x + 4
                dy = self.y + 4
            for i in range (self.y, dy):
                if pyxel.pget(dx, i) == 1:
                    return True
        elif self.direction == "left":
            dx = self.x - 1
            if self.level == 1 or self.level == 2:
                dy = self.y + 16
            elif self.level == 3 or self.level == 4:
                dy = self.y + 8
            else:
                dy = self.y + 4
            for i in range (self.y, dy):
                if pyxel.pget(dx, i) == 1:
                    return True
        elif self.direction == "up":
            dy = self.y - 1
            if self.level == 1 or self.level == 2:
                dx = self.x + 16
            elif self.level == 3 or self.level == 4:
                dx = self.x + 8
            else:
                dx = self.x + 4
            for i in range (self.x, dx):
                if pyxel.pget(i, dy) == 1:
                    return True
        elif self.direction == "down":
            if self.level == 1 or self.level == 2:
                dx = self.x + 16
                dy = self.y + 16
            elif self.level == 3 or self.level == 4:
                dx = self.x + 8
                dy = self.y + 8
            else:
                dx = self.x + 4
                dy = self.y + 4
            for i in range (self.x, dx):
                if pyxel.pget(i, dy) == 1:
                    return True
        return False
    
    def mouvement (self):
        """fonction de déplacement du personnage"""
        self.drawPerso()
        if pyxel.btn(pyxel.KEY_Z):
            self.direction = "up"
            if not self.collision():
                self.y = self.y - self.speed
            
        elif pyxel.btn(pyxel.KEY_S):
            self.direction = "down"
            if not self.collision():
                self.y = self.y + self.speed
            
        elif pyxel.btn(pyxel.KEY_D):
            self.direction = "right"
            if not self.collision():
                self.x += self.speed
        
        elif pyxel.btn(pyxel.KEY_Q):
            self.direction = "left"
            if not self.collision():
                self.x -= self.speed


class Ennemi:
    def __init__(self, direction="right"):
        """constructeur de la classe ennemi"""
        self.speed = 1
        self.direction = direction
        self.x = random.randint(0, 7)*32+16
        self.y = random.randint(0, 7)*32+16
        self.level = 1
    
    def drawEnnemi (self):
        """affichage de l'ennemi à l'écran"""
        pyxel.load("assets/skin.pyxres")
        if self.direction == "right":
            if self.level == 1:
                pyxel.blt(self.x, self.y, 0, 32, 48, 16, 16)
            elif self.level == 3:
                pyxel.blt(self.x, self.y, 0, 32, 0, 8, 8)
            elif self.level == 5:
                pyxel.blt(self.x, self.y, 0, 34, 42, 4, 4)
        elif self.direction == "up":
            if self.level == 1:
                pyxel.blt(self.x, self.y, 0, 32, 64, 16, 16)
            elif self.level == 3:
                pyxel.blt(self.x, self.y, 0, 32, 8, 8, 8)
            elif self.level == 5:
                pyxel.blt(self.x, self.y, 0, 42, 42, 4, 4)
        elif self.direction == "left":
            if self.level == 1:
                pyxel.blt(self.x, self.y, 0, 48, 64, 16, 16)
            elif self.level == 3:
                pyxel.blt(self.x, self.y, 0, 40, 8, 8, 8)
            elif self.level == 5:
                pyxel.blt(self.x, self.y, 0, 40, 34, 4, 4)
        elif self.direction == "down":
            if self.level == 1:
                pyxel.blt(self.x, self.y, 0, 48, 48, 16, 16)
            elif self.level == 3:
                pyxel.blt(self.x, self.y, 0, 40, 0, 8, 8)
            elif self.level == 5:
                pyxel.blt(self.x, self.y, 0, 42, 34, 4, 4)
        
    def collision(self):
        """vérification de la collision avec les murs"""
        dx = 0
        dy = 0
        if self.direction == "right":
            if self.level == 1 or self.level == 2:
                dx = self.x + 16
                dy = self.y + 16
            elif self.level == 3 or self.level == 4:
                dx = self.x + 8
                dy = self.y + 8
            else:
                dx = self.x + 4
                dy = self.y + 4
            for i in range (self.y, dy):
                if pyxel.pget(dx, i) == 1:
                    return True
        elif self.direction == "left":
            dx = self.x - 1
            if self.level == 1 or self.level == 2:
                dy = self.y + 16
            elif self.level == 3 or self.level == 4:
                dy = self.y + 8
            else:
                dy = self.y + 4
            for i in range (self.y, dy):
                if pyxel.pget(dx, i) == 1:
                    return True
        elif self.direction == "up":
            dy = self.y - 1
            if self.level == 1 or self.level == 2:
                dx = self.x + 16
            elif self.level == 3 or self.level == 4:
                dx = self.x + 8
            else:
                dx = self.x + 4
            for i in range (self.x, dx):
                if pyxel.pget(i, dy) == 1:
                    return True
        elif self.direction == "down":
            if self.level == 1 or self.level == 2:
                dx = self.x + 16
                dy = self.y + 16
            elif self.level == 3 or self.level == 4:
                dx = self.x + 8
                dy = self.y + 8
            else:
                dx = self.x + 4
                dy = self.y + 4
            for i in range (self.x, dx):
                if pyxel.pget(i, dy) == 1:
                    return True
        return False
    
    def mouvement(self):
        """mouvement de l'ennemi"""
        n = random.randint(0, 3)
        for i in range (10):
            if n == 0:
                self.direction = "up"
                if not self.collision():
                    self.y = self.y - self.speed
            elif n == 1:
                self.direction = "down"
                if not self.collision():
                    self.y = self.y + self.speed
            elif n == 2:
                self.direction = "left"
                if not self.collision():
                    self.x = self.x + self.speed
            elif n == 3:
                self.direction = "right"
                if not self.collision():
                    self.x = self.x + self.speed
