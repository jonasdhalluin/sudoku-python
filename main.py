
def present_ligne(grille, ligne, nombre):
    if nombre in grille[ligne]:
        print("T")
        return True
    else:
        print("F")
        return False

def present_colonne(grille, colonne, nombre):
    for i in grille:
        if nombre == i[colonne]:
            print("T")
            return True
    return False

def present_carre(grille, debut_carre, nombre):
    for i in range(0, 3):
        print (grille[i+debut_carre[0]][debut_carre[1]:debut_carre[1]+3])
        if nombre in grille[i+debut_carre[0]][debut_carre[1]:debut_carre[1]+3]:
            print("Trouvé")
            return True         
    else:
        print("Non trouvé")
        return False



grille = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


        
present_ligne(grille, 3, 6)
present_colonne(grille, 0, 7)
present_carre(grille, (3, 3), 9)


