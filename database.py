import sqlite3


class DatabaseManager :
    def __init__(self, db_name = "database.db") :
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cree_table()

    def cree_table(self) :
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
        self.conn.commit()

    def insere_annonce(self, titre, prix, surface, ville, nb_pieces, url) :
        pass

    def lit_donnees() :
        pass

    def ferme_base(self) :
        self.conn.close()