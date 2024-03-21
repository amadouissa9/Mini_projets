from ListePersone import ListePersonnes as p

class MenuListePersonnes:
    def __init__(self):
        self.liste_personnes = p(host="localhost", user="root", password="", database="mini_projet")

    def afficher_menu(self):
        while True:
            print("\n Menu des tâches :")
            print("1. Ajouter une personne")
            print("2. Afficher les personnes")
            print("3. Quitter")
            choix = input("Entrez votre choix : ")

            if choix == "1":
                numListe = input("Entrez le Numéro de la personne : ")
                nom = input("Entrez le nom de la personne : ")
                age = int(input("Entrez l'âge de la personne : "))
                self.liste_personnes.ajouter_personne(numListe, nom, age)
            elif choix == "2":
                self.liste_personnes.charger_et_afficher_personnes()
            elif choix == "3":
                print("Au revoir !")
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

if __name__ == "__main__":
    menu = MenuListePersonnes()
    menu.afficher_menu()
