import sqlite3
import datetime


class DatabaseManager :
    def __init__(self, db_name = "database.db") :
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cree_table()

    def cree_table(self) :
        #on intègre à la demonade url TEXT UNIQUE, la condition de la section XI
        query = """
        CREATE TABLE IF NOT EXISTS annonces (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            prix INTEGER NOT NULL,
            surface INTEGER,
            ville TEXT NOT NULL,
            nb_pieces INTEGER,
            url TEXT UNIQUE,
            date_scraping TEXT NOT NULL
        )
        """
        self.cursor.execute(query)
        #commit pour enregistrer
        self.conn.commit()

    def insert_annonce(self, titre, prix, surface, ville, nb_pieces, url) :
        #enregistrement de la date grâce à datetime et conversion pour ne pas avoir de pb de date à cause du SQL
        date_actuelle = datetime.now().strftime("%Y-%M-%D %H:%M:%S")
        try:
            self.cursor.execute("""
                INSERT INTO annonces (titre, prix, surface, ville, nb_pieces, url, date_scraping
            """, (titre, prix, surface, ville, nb_pieces, url, date_actuelle))
            # on commit comme demandé
            self.conn.commit()

        except sqlite3.IntegrityError :
            print(f"Warning : une même annonce apparaît deux fois")

    def get_all_annonces(self) :
        self.cursor.execute("SELECT * FROM annonces")
        #renvoie toutes les données du curseur
        return self.cursor.fetchall()

    def ferme_base(self) :
        self.conn.close()