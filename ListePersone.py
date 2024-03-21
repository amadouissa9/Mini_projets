import mysql.connector as mysql

class ListePersonnes:
    def __init__(self, host, user, password, database):
        self.personnes = []
        self.connection = mysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def ajouter_personne(self, numListe, nom, age):
        try:
            self.cursor.execute("INSERT INTO liste (Num_liste, nom, age) VALUES (%s, %s, %s)", (numListe, nom, age))
            self.connection.commit()
            print("Opération effectuée avec succès !")
            self.charger_et_afficher_personnes()
        except mysql.Error as err:
            print("Erreur lors de l'ajout de la personne :", err)

    def charger_et_afficher_personnes(self):
        self.personnes = []
        self.cursor.execute("SELECT * FROM liste")
        rows = self.cursor.fetchall()
        if not rows:
            print("Aucune personne à afficher.")
        else:
            print("Liste des personnes :")
            for row in rows:
                Num_liste, nom, age = row
                self.personnes.append({'Num_liste': Num_liste, 'nom': nom, 'age': age})
                print(f"Numéro de liste: {Num_liste}, Nom: {nom}, Âge: {age}")