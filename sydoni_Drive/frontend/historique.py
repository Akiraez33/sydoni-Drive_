import tkinter as tk
from tkinter import ttk
from backend.trajets import get_historique_utilisateur # Importation de la fonction du backend pour récupérer l'historique

class HistoriqueFrame(tk.Frame):
    """
    Cadre (Frame) pour afficher l'historique détaillé des trajets d'un utilisateur.
    Cet écran permet de visualiser les trajets effectués, leur statut, les points gagnés (pour les automobilistes)
    et la note moyenne reçue, dans un format tabulaire (Treeview).
    """
    def __init__(self, parent, controller):
        """
        Initialise le cadre de l'historique des trajets.

        Args:
            parent (tk.Tk ou tk.Frame): Le widget parent (généralement la fenêtre principale de l'application).
            controller (object): L'objet contrôleur (SydoniDriveApp) pour la navigation entre les pages.
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.user_email = None # L'email de l'utilisateur sera défini via set_user_email

        # Configuration de la mise en page pour que le Treeview puisse s'étendre
        self.grid_rowconfigure(0, weight=0) # Titre
        self.grid_rowconfigure(1, weight=1) # Treeview (extensible)
        self.grid_rowconfigure(2, weight=0) # Boutons
        self.grid_columnconfigure(0, weight=1)

        # Titre de la page d'historique
        self.label = ttk.Label(self, text="Historique de vos trajets", font=("Helvetica", 16, "bold"))
        self.label.grid(row=0, column=0, pady=10, sticky="n")

        # Création du Treeview pour afficher les données tabulaires
        # Définition des colonnes : id, universite, depart (heure), etat, role, points, note moyenne
        self.tree = ttk.Treeview(self, columns=("id", "universite", "depart", "etat", "role", "points", "note"), show="headings")
        
        # Définition des en-têtes de colonnes
        self.tree.heading("id", text="ID")
        self.tree.heading("universite", text="Université")
        self.tree.heading("depart", text="Heure Départ")
        self.tree.heading("etat", text="État")
        self.tree.heading("role", text="Rôle")
        self.tree.heading("points", text="Points")
        self.tree.heading("note", text="Note Moyenne")
        
        # Configuration des largeurs de colonnes (pour un meilleur affichage)
        self.tree.column("id", width=50, anchor="center")
        self.tree.column("universite", width=150)
        self.tree.column("depart", width=100, anchor="center")
        self.tree.column("etat", width=100, anchor="center")
        self.tree.column("role", width=80, anchor="center")
        self.tree.column("points", width=80, anchor="center")
        self.tree.column("note", width=100, anchor="center")

        self.tree.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        # Barre de défilement pour le Treeview si nécessaire
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.grid(row=1, column=1, sticky="ns")

        # Boutons d'action
        button_frame = ttk.Frame(self)
        button_frame.grid(row=2, column=0, pady=10)

        # Bouton d'actualisation
        ttk.Button(button_frame, text="Actualiser l'historique", command=self.afficher_historique).pack(side="left", padx=5)

        # Bouton de retour à l'écran précédent (par exemple, l'interface automobiliste ou passager)
        # La destination de retour dépendra du contexte d'où cette frame est appelée.
        # Pour l'instant, nous allons retourner à la page de connexion/inscription par défaut si l'email n'est pas défini.
        # Idéalement, on pourrait passer le nom de la frame de retour en paramètre.
        ttk.Button(button_frame, text="Retour", command=self.retour_precedent).pack(side="left", padx=5)

    def set_user_email(self, email):
        """
        Définit l'email de l'utilisateur pour cette frame.
        Cette méthode est appelée par le contrôleur (SydoniDriveApp) lors de la navigation.
        Args:
            email (str): L'email de l'utilisateur connecté.
        """
        self.user_email = email

    def afficher_historique(self):
        """
        Charge et affiche l'historique des trajets de l'utilisateur dans le Treeview.
        Cette méthode est appelée lors de l'affichage de la frame et lors de l'actualisation.
        """
        # Effacer les entrées précédentes pour éviter les doublons lors de l'actualisation
        for i in self.tree.get_children():
            self.tree.delete(i)

        if not self.user_email:
            self.tree.insert("", "end", values=("", "", "", "", "", "", ""))
            self.tree.insert("", "end", values=("", "", "", "Veuillez vous connecter pour voir l'historique.", "", "", ""))
            return

        # Récupérer l'historique des trajets via la fonction du backend
        historique = get_historique_utilisateur(self.user_email)
        
        if historique:
            for trajet in historique:
                # Insérer chaque trajet comme une nouvelle ligne dans le Treeview
                self.tree.insert("", "end", values=(
                    trajet.get("id", "N/A"),
                    trajet.get("universite", "N/A"),
                    trajet.get("heure_depart", "N/A"),
                    trajet.get("etat", "N/A"),
                    trajet.get("role", "N/A"),
                    trajet.get("points", "N/A"),
                    trajet.get("notes_moyenne", "N/A")
                ))
        else:
            # Message si aucun historique n'est disponible
            self.tree.insert("", "end", values=("", "", "", "", "", "", "")) 
            self.tree.insert("", "end", values=("", "", "", "Aucun historique disponible.", "", "", ""))

    def retour_precedent(self):
        """
        Gère le retour à la page précédente.
        Pour l'instant, retourne à la page de connexion/inscription.
        Idéalement, cette fonction devrait naviguer vers la page d'où elle a été appelée
        (par exemple, InterfaceAutomobilisteFrame ou InterfacePassagerFrame).
        Ceci peut être géré en passant un paramètre à show_frame ou en stockant la page précédente.
        """
        self.controller.show_frame("LoginRegisterFrame") # Retour par défaut

    def show(self):
        """
        Affiche ce cadre et s'assure qu'il est au premier plan.
        Cette méthode est appelée par le contrôleur chaque fois que cette frame doit être affichée.
        """
        self.afficher_historique() # S'assurer que l'historique est à jour à chaque affichage
        self.tkraise()


