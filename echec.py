from tkinter import *
from random import *
import string
# librairie qui permet de gerer la redimension image
from PIL import Image
from PIL import ImageTk

# definition du plateau de jeux avec contour du plateua
def initPlato():
    global plato
    plato = [['M', 'MA', 'MB', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'M'],
             ['M1', 'tourBlanc', 'cavalierBlanc', 'fouBlanc', 'roiBlanc', 'reineBlanc', 'fouBlanc', 'cavalierBlanc',
              'tourBlanc', 'M1'],
             ['M2', 'pionBlanc', 'pionBlanc', 'pionBlanc', 'pionBlanc', 'pionBlanc', 'pionBlanc', 'pionBlanc',
              'pionBlanc', 'M2'],
             ['M3', '', '', '', '', '', '', '', '', 'M3'],
             ['M4', '', '', '', '', '', '', '', '', 'M4'],
             ['M5', '', '', '', '', '', '', '', '', 'M5'],
             ['M6', '', '', '', '', '', '', '', '', 'M6'],
             ['M7', 'pionNoir', 'pionNoir', 'pionNoir', 'pionNoir', 'pionNoir', 'pionNoir', 'pionNoir', 'pionNoir',
              'M7'],
             ['M8', 'tourNoir', 'cavalierNoir', 'fouNoir', 'reineNoir', 'roiNoir', 'fouNoir', 'cavalierNoir',
              'tourNoir', 'M8'],
             ['M', 'MA', 'MB', 'MC', 'MD', 'ME', 'MF', 'MG', 'MH', 'M']]


def createCasePlato(indiceLigne, indiceColonne):
    # colonnepaire
    if (indiceColonne % 2) == 0:
        couleurEmplacement = couleurCasePaire
    else:
        couleurEmplacement = couleurCaseImpaire

    canevas.create_polygon(indiceColonne * tailleCase, indiceLigne * tailleCase, (indiceColonne + 1) * tailleCase,
                           indiceLigne * tailleCase, (indiceColonne + 1) * tailleCase, (indiceLigne + 1) * tailleCase,
                           indiceColonne * tailleCase, (indiceLigne + 1) * tailleCase, fill=couleurEmplacement,
                           outline=bordureMur)


def constitutionCouleur(indiceLigne):
    # lignepaire
    global couleurCaseImpaire
    global couleurCasePaire
    if (indiceLigne % 2) == 0:
        couleurCasePaire = "white"
        couleurCaseImpaire = "black"
    # ligneimpaire
    if (indiceLigne % 2) == 1:
        couleurCasePaire = "black"
        couleurCaseImpaire = "white"


# création graphique du plateau
def creatPlato():
    for indiceLigne in range(0, nbLigne):
        constitutionCouleur(indiceLigne)
        for indiceColonne in range(0, nbColonnes):
            if plato[indiceLigne][indiceColonne][:1] == etatMur:
                canevas.create_polygon(indiceColonne * tailleCase, indiceLigne * tailleCase,
                                       (indiceColonne + 1) * tailleCase, indiceLigne * tailleCase,
                                       (indiceColonne + 1) * tailleCase, (indiceLigne + 1) * tailleCase,
                                       indiceColonne * tailleCase, (indiceLigne + 1) * tailleCase, fill=couleurMur,
                                       outline=bordureMur)
                if not len(str(plato[indiceLigne][indiceColonne])) == 1:
                    text = plato[indiceLigne][indiceColonne][1:]
                    canevas.create_text(indiceColonne * tailleCase + tailleCase / 2,
                                        indiceLigne * tailleCase + tailleCase / 2, text=text, fill='black')
            else:
                createCasePlato(indiceLigne, indiceColonne)


def creatPiece():
    for indiceLigne in range(0, nbLigne):
        for indiceColonne in range(0, nbColonnes):
            idImagePiece = ""
            if plato[indiceLigne][indiceColonne] == 'cavalierBlanc':
                idImagePiece = canevas.create_image(indiceColonne * tailleCase + tailleCase / 2,
                                                    indiceLigne * tailleCase + tailleCase / 2,
                                                    image=imageTkCavalierBlanc)

            if plato[indiceLigne][indiceColonne] == 'pionBlanc':
                idImagePiece = canevas.create_image(indiceColonne * tailleCase + tailleCase / 2,
                                                    indiceLigne * tailleCase + tailleCase / 2, image=imageTkPionBlanc)

            if plato[indiceLigne][indiceColonne] == 'roiBlanc':
                idImagePiece = canevas.create_image(indiceColonne * tailleCase + tailleCase / 2,
                                                    indiceLigne * tailleCase + tailleCase / 2, image=imageTkRoiBlanc)

            if plato[indiceLigne][indiceColonne] == 'reineBlanc':
                idImagePiece = canevas.create_image(indiceColonne * tailleCase + tailleCase / 2,
                                                    indiceLigne * tailleCase + tailleCase / 2, image=imageTkReineBlanc)

            if plato[indiceLigne][indiceColonne] == 'fouBlanc':
                idImagePiece = canevas.create_image(indiceColonne * tailleCase + tailleCase / 2,
                                                    indiceLigne * tailleCase + tailleCase / 2, image=imageTkFouBlanc)

            if plato[indiceLigne][indiceColonne] == 'tourBlanc':
                idImagePiece = canevas.create_image(indiceColonne * tailleCase + tailleCase / 2,
                                                    indiceLigne * tailleCase + tailleCase / 2, image=imageTkTourBlanc)

            if plato[indiceLigne][indiceColonne] == 'cavalierNoir':
                idImagePiece = canevas.create_image(indiceColonne * tailleCase + tailleCase / 2,
                                                    indiceLigne * tailleCase + tailleCase / 2,
                                                    image=imageTkCavalierNoir)

            if plato[indiceLigne][indiceColonne] == 'pionNoir':
                idImagePiece = canevas.create_image(indiceColonne * tailleCase + tailleCase / 2,
                                                    indiceLigne * tailleCase + tailleCase / 2, image=imageTkPionNoir)

            if plato[indiceLigne][indiceColonne] == 'roiNoir':
                idImagePiece = canevas.create_image(indiceColonne * tailleCase + tailleCase / 2,
                                                    indiceLigne * tailleCase + tailleCase / 2, image=imageTkRoiNoir)

            if plato[indiceLigne][indiceColonne] == 'reineNoir':
                idImagePiece = canevas.create_image(indiceColonne * tailleCase + tailleCase / 2,
                                                    indiceLigne * tailleCase + tailleCase / 2, image=imageTkReineNoir)

            if plato[indiceLigne][indiceColonne] == 'fouNoir':
                idImagePiece = canevas.create_image(indiceColonne * tailleCase + tailleCase / 2,
                                                    indiceLigne * tailleCase + tailleCase / 2, image=imageTkFouNoir)

            if plato[indiceLigne][indiceColonne] == 'tourNoir':
                idImagePiece = canevas.create_image(indiceColonne * tailleCase + tailleCase / 2,
                                                    indiceLigne * tailleCase + tailleCase / 2, image=imageTkTourNoir)

            if not idImagePiece == "":
                plato[indiceLigne][indiceColonne] = plato[indiceLigne][indiceColonne] + "_" + str(idImagePiece)


def validationPieceABouger(*args):
    isSaisieErrone = False
    valeurPieceABouger = reponsePieceABouger.get();
    print(valeurPieceABouger)
    if (len(valeurPieceABouger)) != 2:
        print("saisie invalide, trop de charactere")
        isSaisieErrone = True
    else:
        if (valeurPieceABouger[:1]) not in listeLettreAutorise:
            print("Saisie invalide: lettre interdite")
            isSaisieErrone = True

        if (valeurPieceABouger[1]) not in listeChiffreAutorise:
            print("Saisie invalide: chiffre interdit")
            isSaisieErrone = True

    if not isSaisieErrone:
        # todo autoriser la saisie de la cible choisie
        print("Veuillez procéder à la saisie de la case ciblé")
        reponsePieceCible.config(state=NORMAL)
        boutonAide.config(state=NORMAL)
        reponsePieceCible.focus()

def changeJoueur():
    global couleurAdverse
    if couleurAdverse == "Noir":
        couleurAdverse = "Blanc"
    else:
        couleurAdverse = "Noir"


def bougePiece(coordoneeSource, coordonerCible):
    print("Je bouge de", coordoneeSource, "a", coordonerCible)
    # todo recupérer l'indice colonne source, récupérer indice ligne source
    colonneSource = coordoneeSource[:1]
    colonneCible = coordonerCible[:1]
    ligneSource = coordoneeSource[1:]
    ligneCible = coordonerCible[1:]

    indiceColonneSource = alphabet.find(colonneSource)
    indiceColonneCible = alphabet.find(colonneCible)
    vecteurX = indiceColonneCible - indiceColonneSource
    vecteurY = int(ligneCible) - int(ligneSource)
    pieceABouger = plato[int(ligneSource)][indiceColonneSource + 1]
    indiceUnderscore = pieceABouger.find("_")
    idImageABouger = pieceABouger[(indiceUnderscore + 1):]
    canevas.move(idImageABouger, vecteurX * tailleCase, vecteurY * tailleCase)

    plato[int(ligneSource)][indiceColonneSource + 1] = ""
    plato[int(ligneCible)][indiceColonneCible + 1] = pieceABouger
    print(plato)
    changeJoueur()


def filigrane(x, y):
    id = canevas.create_image(x, y, image=imageFiligrane)
    listeFiligraneASupprimer.append(id)


def simulationCavalier(indiceLigne, indiceColonne, couleurAdverse):
    indiceCase = indiceLigne * 10 + indiceColonne
    print(indiceCase)
    liste = []

    for i in deplacementCavalier:
        positionPossible = indiceCase + i
        colonnePossible = positionPossible % 10
        lignePossible = positionPossible // 10
        if (plato[int(lignePossible)][int(colonnePossible)] == "" or (
        plato[int(lignePossible)][int(colonnePossible)]).find(couleurAdverse) > -1):
            liste.append((lignePossible, colonnePossible))
    return liste


def simulationTour(indiceLigne, indiceColonne, couleurAdverse):
    indiceCase = indiceLigne * 10 + indiceColonne
    print(indiceCase)
    liste = []
    for k in deplacementTour:
        j = 1
        while TRUE:
            positionPossible = indiceCase + (k * j)
            colonnePossible = positionPossible % 10
            lignePossible = positionPossible // 10

            if plato[lignePossible][colonnePossible] == "" or plato[lignePossible][colonnePossible].find(
                    couleurAdverse) > -1:
                liste.append((lignePossible, colonnePossible))
                if plato[lignePossible][colonnePossible].find(couleurAdverse) > -1:
                    break
            else:
                break
            j = j + 1
    return liste


def simulationFou(indiceLigne, indiceColonne, couleurAdverse):
    indiceCase = indiceLigne * 10 + indiceColonne
    print(indiceCase)
    liste = []
    for k in deplacementFou:
        j = 1
        while True:
            positionPossible = indiceCase + (k * j)
            colonnePossible = positionPossible % 10
            lignePossible = positionPossible // 10

            if plato[lignePossible][colonnePossible] == "" or plato[lignePossible][colonnePossible].find(
                    couleurAdverse) > -1:
                liste.append((lignePossible, colonnePossible))
                if plato[lignePossible][colonnePossible].find(couleurAdverse) > -1:
                    break


            else:
                break
            j = j + 1
    return liste


def simulationReine(indiceLigne, indiceColonne, couleurAdverse):
    listeFou = simulationFou(indiceLigne, indiceColonne, couleurAdverse)
    listeTour = simulationTour(indiceLigne, indiceColonne, couleurAdverse)
    return listeFou + listeTour


def simulationPion(indiceLigne, indiceColonne, couleurAdverse):
    indiceCase = indiceLigne * 10 + indiceColonne
    print(indiceCase)
    liste = []

    if (couleurAdverse == "Noir"):
        couleurJoueur = "Blanc"
    else:
        couleurJoueur = "Noir"
    # pion noir
    if couleurJoueur == 'Noir':

        # todo gestion promo
        # gestion depart pion
        if indiceLigne == 7:
            # If the 2 upper squares are empty
            positionPossible = indiceCase - 10
            colonnePossible = positionPossible % 10
            lignePossible = positionPossible // 10

            positionPossibleB = indiceCase - 20
            colonnePossibleB = positionPossibleB % 10
            lignePossibleB = positionPossibleB // 10

            # Gestion possible coup + 2 lignes
            if plato[lignePossibleB][colonnePossibleB] == "" and plato[lignePossible][colonnePossible] == "":
                liste.append((lignePossibleB, colonnePossibleB))
                liste.append((lignePossible, colonnePossible))
        else:
            positionPossible = indiceCase - 10
            colonnePossible = positionPossible % 10
            lignePossible = positionPossible // 10
            # Gestion possible coup + 1 lignes
            if plato[lignePossible][colonnePossible] == "":
                liste.append((lignePossible, colonnePossible))

        # Prise  diagonale Gauche
        positionPossible = indiceCase - 11
        colonnePossible = positionPossible % 10
        lignePossible = positionPossible // 10
        # faire la gestion des en passant
        if plato[lignePossible][colonnePossible].find("Blanc") > -1:
            # gestion promotion à faire
            liste.append((lignePossible, colonnePossible))

        # Prise  diagonale Droite
        positionPossible = indiceCase - 9
        colonnePossible = positionPossible % 10
        lignePossible = positionPossible // 10
        # faire la gestion des en passant
        if plato[lignePossible][colonnePossible].find("Blanc") > -1:
            # gestion promotion à faire
            liste.append((lignePossible, colonnePossible))


    # Pion blanc ---------------------------------------------------
    else:
        # todo gestion promo
        # gestion depart pion
        if indiceLigne == 2:

            positionPossible = indiceCase + 10
            colonnePossible = positionPossible % 10
            lignePossible = positionPossible // 10

            positionPossibleB = indiceCase + 20
            colonnePossibleB = positionPossible % 10
            lignePossibleB = positionPossibleB // 10

            # Gestion possible coup + 2 lignes
            if plato[lignePossibleB][colonnePossibleB] == "" and plato[lignePossible][colonnePossible] == "":
                liste.append((lignePossibleB, colonnePossibleB))
                liste.append((lignePossible, colonnePossible))
        else:
            positionPossible = indiceCase + 10
            colonnePossible = positionPossible % 10
            lignePossible = positionPossible // 10

            # Gestion possible coup + 1 lignes
            if plato[lignePossible][colonnePossible] == "":
                liste.append((lignePossible, colonnePossible))

        # Prise  diagonale Gauche
        positionPossible = indiceCase + 11
        colonnePossible = positionPossible % 10
        lignePossible = positionPossible // 10
        # faire la gestion des en passant
        if plato[lignePossible][colonnePossible].find("Noir") > -1:
            # gestion promotion à faire
            liste.append((lignePossible, colonnePossible))

        # Prise  diagonale Droite
        positionPossible = indiceCase + 9
        colonnePossible = positionPossible % 10
        lignePossible = positionPossible // 10
        # faire la gestion des en passant
        if plato[lignePossible][colonnePossible].find("Noir") > -1:
            # gestion promotion à faire
            liste.append((lignePossible, colonnePossible))

    return liste


def suppressionImageFiligrane():
    for idImage in listeFiligraneASupprimer:
        canevas.delete(idImage)


def simulation():
    suppressionImageFiligrane()
    liste = []
    valeurPieceABouger = reponsePieceABouger.get();
    colonneSource = valeurPieceABouger[:1]
    ligneSource = valeurPieceABouger[1:]
    indiceColonneSource = int(alphabet.find(colonneSource)) + 1
    piece = plato[int(ligneSource)][int(indiceColonneSource)]
    # si la valeur -1 est renvoyer par find alors il na pas trouver la chaine de charactère
    if piece.find("cavalier") > -1:
        liste = simulationCavalier(int(ligneSource), indiceColonneSource, couleurAdverse)

    if piece.find("tour") > -1:
        liste = simulationTour(int(ligneSource), indiceColonneSource, couleurAdverse)

    if piece.find("fou") > -1:
        liste = simulationFou(int(ligneSource), indiceColonneSource, couleurAdverse)

    if piece.find("reine") > -1:
        liste = simulationReine(int(ligneSource), indiceColonneSource, couleurAdverse)

    if piece.find("pion") > -1:
        liste = simulationPion(int(ligneSource), indiceColonneSource, couleurAdverse)

    return liste


def validationCible(*args):
    isSaisieErrone = False
    valeurPieceCible = reponsePieceCible.get();
    print(valeurPieceCible)
    if (len(valeurPieceCible)) != 2:
        print("Saisie invalide: trop de charactère")
        isSaisieErrone = True
    else:

        if (valeurPieceCible[:1]) not in listeLettreAutorise:
            print("Saisie invalide: lettre interdite")
            isSaisieErrone = True

        if (valeurPieceCible[1]) not in listeChiffreAutorise:
            print("Saisie invalide: chiffre interdit")
            isSaisieErrone = True

    if not isSaisieErrone:
        colonneCible = valeurPieceCible[:1]
        ligneCible = valeurPieceCible[1:]
        indiceColonneCible = int(alphabet.find(colonneCible)) + 1
        coordonneeCible = ((int(ligneCible), indiceColonneCible))
        listePossible = simulation()
        if coordonneeCible in listePossible:
            print("Deplacement piece")
            bougePiece(reponsePieceABouger.get(), valeurPieceCible)


def aide():
    liste = simulation()
    if not liste == "":
        for coordonnee in liste:
            abscice = coordonnee[1]
            ordonnee = coordonnee[0]
            x = tailleCase * abscice + tailleCase / 2
            y = tailleCase * ordonnee + tailleCase / 2
            filigrane(x, y)


# todo VALIDATION COULEUR ,Validation case jouable


deplacementCavalier = (-12, -21, -19, -8, 12, 21, 19, 8)
deplacementFou = (-11, -9, 11, 9)
deplacementTour = (-10, 10, -1, 1)

# nombre colonne = 10 car 8 demander plus 2 liserer du plateau
nbColonnes = 10
# nombre lignes = 10 dont  8 demander plus 2 liserer du plateau
nbLigne = 10
# creation de la fenetre principale
maFenetre = Tk()
maFenetre.title = ("Les echecs")
# couleur de fond
maFenetre['bg'] = 'black'
# creation d'un caanevas
tailleCase = 60
largeur = tailleCase * nbColonnes
hauteur = tailleCase * nbLigne
canevas = Canvas(maFenetre, width=largeur, height=hauteur, bg='white')
canevasJoueur = Canvas(maFenetre, width=200, height=hauteur, bg="white")
# positionnement
canevas.grid(row=0, column=0)
canevasJoueur.grid(row=0, column=1)
canevasJoueur.create_text(30, 50, text="Score: ", fill="black")
score = 0
identifiantScore = canevasJoueur.create_text(50, 50, text=score, fill="black")
# zone de saisie piece a bouger
listeLettreAutorise = ("A", "B", "C", "D", "E", "F", "G", "H")
listeChiffreAutorise = ("1", "2", "3", "4", "5", "6", "7", "8")
labelPieceABouger = Label(canevasJoueur, text="Pièce:")
labelPieceABouger.place(x=30, y=70)

reponsePieceABouger = Entry(canevasJoueur, width=3)
reponsePieceABouger.place(x=150, y=70)
reponsePieceABouger.bind("<Return>", validationPieceABouger)

labelPieceCible = Label(canevasJoueur, text="Pièce ciblé:")
labelPieceCible.place(x=30, y=170)

reponsePieceCible = Entry(canevasJoueur, width=3, state=DISABLED)
reponsePieceCible.place(x=150, y=170)
reponsePieceCible.bind("<Return>", validationCible)

boutonAide = Button(canevasJoueur, text="Aide", command=aide)
boutonAide.config(state=DISABLED)
boutonAide.place(x=150, y=300)

couleurAdverse = "Noir"
couleurCaseImpaire = ""
couleurCasePaire = ""
# b signifie que la case est un bord
etatMur = "M"
couleurEmplacementPiece1 = 'white'
couleurMur = "brown"
bordureMur = "blue"

# surface de jeu
plato = []

initPlato()
creatPlato()

# chargement graphique des image
# cavalier blanc
##
imagePilCavaBlanc = Image.open('piece blanc/cavablanc.png')
imagePilCavaBlanc = imagePilCavaBlanc.resize((int(tailleCase / 2), int(tailleCase / 2)), Image.ANTIALIAS)
imageTkCavalierBlanc = ImageTk.PhotoImage(imagePilCavaBlanc)
# pionblanc
imagePilPionBlanc = Image.open('piece blanc/pionblanc.png')
imagePilPionBlanc = imagePilPionBlanc.resize((int(tailleCase / 2), int(tailleCase / 2)), Image.ANTIALIAS)
imageTkPionBlanc = ImageTk.PhotoImage(imagePilPionBlanc)

# roiblanc
imagePilRoiBlanc = Image.open('piece blanc/roi blanc.png')
imagePilRoiBlanc = imagePilRoiBlanc.resize((int(tailleCase / 2), int(tailleCase / 2)), Image.ANTIALIAS)
imageTkRoiBlanc = ImageTk.PhotoImage(imagePilRoiBlanc)

# reineblanc
imagePilReineBlanc = Image.open('piece blanc/reineblanc.png')
imagePilReineBlanc = imagePilReineBlanc.resize((int(tailleCase / 2), int(tailleCase / 2)), Image.ANTIALIAS)
imageTkReineBlanc = ImageTk.PhotoImage(imagePilReineBlanc)

# foublanc
imagePilFouBlanc = Image.open('piece blanc/foublanc.png')
imagePilFouBlanc = imagePilReineBlanc.resize((int(tailleCase / 2), int(tailleCase / 2)), Image.ANTIALIAS)
imageTkFouBlanc = ImageTk.PhotoImage(imagePilFouBlanc)

# tourblanc
imagePilTourBlanc = Image.open('piece blanc/tourblanc.png')
imagePilTourBlanc = imagePilTourBlanc.resize((int(tailleCase / 2), int(tailleCase / 2)), Image.ANTIALIAS)
imageTkTourBlanc = ImageTk.PhotoImage(imagePilTourBlanc)

# cavlier noir
imagePilCavaNoir = Image.open('piece noir/cavanoir.png')
imagePilCavaNoir = imagePilCavaNoir.resize((int(tailleCase / 2), int(tailleCase / 2)), Image.ANTIALIAS)
imageTkCavalierNoir = ImageTk.PhotoImage(imagePilCavaNoir)

# roi noir
imagePilRoiNoir = Image.open("piece noir/roinoir.png")
imagePilRoiNoir = imagePilRoiNoir.resize((int(tailleCase / 2), int(tailleCase / 2)), Image.ANTIALIAS)
imageTkRoiNoir = ImageTk.PhotoImage(imagePilRoiNoir)

# pion noir
imagePilPionNoir = Image.open('piece noir/pionnoir.png')
imagePilPionNoir = imagePilPionNoir.resize((int(tailleCase / 2), int(tailleCase / 2)), Image.ANTIALIAS)
imageTkPionNoir = ImageTk.PhotoImage(imagePilPionNoir)

# reine noir
imagePilReineNoir = Image.open('piece noir/reinenoir.png')
imagePilReineNoir = imagePilReineNoir.resize((int(tailleCase / 2), int(tailleCase / 2)), Image.ANTIALIAS)
imageTkReineNoir = ImageTk.PhotoImage(imagePilReineNoir)

# tour noir
imagePilTourNoir = Image.open('piece noir/tournoir.png')
imagePilTourNoir = imagePilTourNoir.resize((int(tailleCase / 2), int(tailleCase / 2)), Image.ANTIALIAS)
imageTkTourNoir = ImageTk.PhotoImage(imagePilTourNoir)

# fou noir
imagePilFouNoir = Image.open('piece noir/founoir.png')
imagePilFouNoir = imagePilFouNoir.resize((int(tailleCase / 2), int(tailleCase / 2)), Image.ANTIALIAS)
imageTkFouNoir = ImageTk.PhotoImage(imagePilFouNoir)

alphabet = "ABCDEFGH"

alpha = int(0.5 * 255)
fill = maFenetre.winfo_rgb('blue') + (alpha,)

listeFiligraneASupprimer = []

imageFiligrane = Image.new('RGBA', (tailleCase, tailleCase), fill)
imageFiligrane = ImageTk.PhotoImage(imageFiligrane)

creatPiece()

maFenetre.mainloop()
