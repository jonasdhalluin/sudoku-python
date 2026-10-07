
def present_ligne(grille, ligne, nombre):
    if nombre in grille[ligne]:
        return True
    return False

def present_colonne(grille, colonne, nombre):
    for i in grille:
        if nombre == i[colonne]:
            return True
    return False

def present_carre(grille, debut_carre, nombre):
    for i in range(0, 3):
        if nombre in grille[i+debut_carre[0]][debut_carre[1]:debut_carre[1]+3]:
            return True         
    return False

def trouver_case_vide(grille):
    for ligne in range(len(grille)):
        for colonne in range(len(grille)):
            if grille[ligne][colonne] == 0:
                return ligne, colonne

def placement_possible(grille, ligne, colonne, nombre):
    debut_ligne = (ligne // 3) * 3
    debut_colonne = (colonne // 3) * 3
    if present_ligne(grille, ligne, nombre) or present_colonne(grille, colonne, nombre) or present_carre(grille, (debut_ligne, debut_colonne), nombre):
        return False
    else:
        return True

def resoudre(grille):
    position = trouver_case_vide(grille)
    if position is None:
        return True
    ligne, colonne = position
    nombre = 0
    for i in range (0, 9):
        nombre += 1  
        if placement_possible(grille, ligne, colonne, nombre):
            grille[ligne][colonne] = nombre
            if resoudre(grille):
                return True
            grille[ligne][colonne] = 0
    return False



grille = [
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 0, 0],
    [0, 7, 0, 0, 9, 0, 2, 0, 0],
    [0, 5, 0, 0, 0, 7, 0, 0, 0],
    [0, 0, 0, 0, 4, 5, 7, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 3],
    [0, 0, 1, 0, 0, 0, 0, 6, 8],
    [0, 0, 8, 5, 0, 0, 0, 1, 0],
    [0, 9, 0, 0, 0, 0, 4, 0, 0]
]
resoudre(grille)
for ligne in grille:
    print(ligne)


