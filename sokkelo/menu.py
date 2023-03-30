import pyxel

page = "regle"

def affichage():
    '''Les changements d'écran sur la page du jeu'''
    pyxel.load("assets/ecrantitre.pyxres")
    global page
    if page == "regle":
        pyxel.blt(0, 0, 1, 0, 0, 256, 256)
        if pyxel.btnp(pyxel.KEY_H):
            page = "commande"
            pyxel.blt(0, 0, 0, 0, 0, 256, 256)
        
        elif pyxel.btnp(pyxel.KEY_P):
            page = "jeu"
    
    elif page == "commande":
        pyxel.blt(0, 0, 0, 0, 0, 256, 256)
        
        if pyxel.btnp(pyxel.KEY_H):
            page = "regle"
            pyxel.blt(0, 0, 1, 0, 0, 256, 256)
            
    elif page == "jeu":
        return page