import random
import tkinter as tk
from PIL import Image, ImageTk

# Création de la fenêtre principale
fenetre = tk.Tk()
fenetre.title("Pierre - Papier - Ciseaux")
fenetre.configure(bg="#ffc8dd")

# Fonction qui choisi au hasard pour l'ordinateur
def computer_choice():
    choices = ["Pierre", "Papier", "Ciseaux"]
    return random.choice(choices)

# Fonction qui permet de lancer le jeu
def play(user_choice):
    computer = computer_choice() #Fait appel à la fonction qui choisi aléatoirement pour le PC

    # Logique pour déterminer le gagnant
    if user_choice == computer:
        result_var.set("Egalité !")
    elif (
        (user_choice == "Pierre" and computer == "Ciseaux") 
        or (user_choice == "Papier" and computer == "Pierre")
        or (user_choice == "Ciseaux" and computer == "Papier")
        ): 
        result_var.set("Vous avez gagné !")
        player_score_var.set(player_score_var.get() + 1)
    else:
        result_var.set("Vous avez perdu !")
        computer_score_var.set(computer_score_var.get() + 1)
    
    # Charger les images correspondantes aux choix
    user_img_label.config(image=get_image(user_choice))
    computer_img_label.config(image=get_image(computer))

    # Ajouter les choix à l'historique (du plus récent au plus ancien)
    history_listbox.insert(0, f"Vous : {user_choice} - Ordinateur : {computer}")


# Afficher une image en fonction du choix
def get_image(choice):
    if choice == "Pierre":
        return rock_img
    elif choice == "Papier":
        return paper_img
    else:
        return scissors_img
    
# Définition des variables
result_var = tk.StringVar()
player_score_var = tk.IntVar()
computer_score_var = tk.IntVar()
    
# Charger les images
rock_img = ImageTk.PhotoImage(Image.open("./jeu/pierre.gif"))
paper_img = ImageTk.PhotoImage(Image.open("./jeu/papier.gif"))
scissors_img = ImageTk.PhotoImage(Image.open("./jeu/Ciseaux.gif"))

# Création des widget avec les images
user_label = tk.Label(fenetre, text="Choisissez : ", bg="#cdb4db", fg="white", font=("Helvetica", 16, "bold"))
user_label.pack(pady=10)

rock_button = tk.Button(fenetre, image=rock_img, command=lambda : play("Pierre"))
rock_button.pack(side=tk.LEFT, padx=10)
              
paper_button = tk.Button(fenetre, image=paper_img, command=lambda : play("Papier"))
paper_button.pack(side=tk.LEFT, padx=10)

scissors_button = tk.Button(fenetre, image=scissors_img, command=lambda : play("Ciseaux"))
scissors_button.pack(side=tk.LEFT, padx=10)

# Etiqueetes pour afficher les images jouées
user_img_label = tk.Label(fenetre, image=None, bg="#ffc8dd") # Pas d'image de départ
user_img_label.pack(pady=10)

computer_img_label = tk.Label(fenetre, image=None, bg="#ffc8dd") # Pas d'image de départ
computer_img_label.pack(pady=10)

result_label = tk.Label(fenetre, textvariable=result_var, bg="#ffc8dd", fg="white", font=("Helvetica", 16, "bold"))
result_label.pack(pady=20)

# Création d'une frame pour les score
score_frame = tk.Frame(fenetre)
score_frame.configure(bg="#a2d2ff")
score_frame.pack()

player_score_label = tk.Label(score_frame, text="Score J1 :", bg="#a2d2ff", fg="white", font=("Helvetica", 14))
player_score_label.pack(side=tk.LEFT, padx=10)

player_score_display = tk.Label(score_frame, textvariable=player_score_var, bg="#a2d2ff", fg="white", font=("Helvetica", 14))
player_score_display.pack(side=tk.LEFT, padx=10)

computer_score_label = tk.Label(score_frame, text="Score Ordinateur :", bg="#a2d2ff", fg="white", font=("Helvetica", 14))
computer_score_label.pack(side=tk.LEFT, padx=10)

computer_score_display = tk.Label(score_frame, textvariable=computer_score_var, bg="#a2d2ff", fg="white", font=("Helvetica", 14))
computer_score_display.pack(side=tk.LEFT, padx=10)

# Gestion de l'historique et de l'affichage
history_label = tk.Label(fenetre, text="Historique des coups : ", bg="#cdb4db", fg="white", font=("Helvetica", 14))
history_label.pack(pady=10)

history_listbox = tk.Listbox(fenetre, width=50, height=15)
history_listbox.configure(bg="#ffc8dd", fg="white", font=("Helvetica", 14), bd=0)
history_listbox.pack()

fenetre.mainloop()