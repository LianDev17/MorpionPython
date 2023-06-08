import random
import os

# Cases de jeu
cases = [0, 0, 0,
         0, 0, 0,
         0, 0, 0]

#Joueur choisi "aléatoirement" 
current_player = random.randint(1, 2) 
isGameFinished = False


#On affiche le morpion dans la console
def board():
    board = ""
    length = 0
    for case in cases:
        board += "| " + str(case) + " |"     
        if length == 2:
            length = 0
            board += "\n"
        else:
            length = length + 1
    return board
               

# Vérifie si un joueur gagne grâce aux possibilités (8 "principalement")
def checkForWin(player):
    if (cases[0] == player and cases[1] == player and cases[2] == player) or \
       (cases[3] == player and cases[4] == player and cases[5] == player) or \
       (cases[6] == player and cases[7] == player and cases[8] == player) or \
       (cases[0] == player and cases[3] == player and cases[6] == player) or \
       (cases[1] == player and cases[4] == player and cases[7] == player) or \
       (cases[2] == player and cases[5] == player and cases[8] == player) or \
       (cases[0] == player and cases[4] == player and cases[8] == player) or \
       (cases[6] == player and cases[4] == player and cases[2] == player):
        return True
    else:
        return False

board()

#Boucle principale du jeu.
#Si la partie n'est pas terminée le code de la boucle est exécuté.
while isGameFinished != True: 
    case = input("Au joueur " + str(current_player) + " de jouer: ")
     
   #On vérifie que l'utilisateur donne bien un chiffre et que celui ci soit compris entre 1 et 9.      
    if case.isdigit():
        case = int(case)
        if case < 1 or case > 9 or cases[case - 1] != 0:
            print("Case inexistante ou déjà utilisée. La case doit être comprise entre 1 et 9 inclus et non jouée.")          
        else:
            cases[case - 1] = current_player
            os.system('clear')          
            print(board())
            #On vérifie si il y a une combinaison de victoire
            if checkForWin(current_player):
                print("Le joueur " + str(current_player) + " a gagné !")
                isGameFinished = True
            else: 
                #On change de joueur             
                if current_player == 1:
                    current_player = 2 
                else:
                    current_player = 1             
    else:
        print("Ce n\'est pas un chiffre. La case doit être un chiffre.")                                               