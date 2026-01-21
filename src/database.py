import sqlite3


class DatabaseManager :
    def __init__(self, db_name) :
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cree_table()

    def cree_table(self) :
        query = """
        CREATE TABLE IF NOT EXISTS citations (
            citation TEXT NON NULL,
            tags TEXT NON NULL
        )
        """
        self.cursor.execute(query)
        #commit pour enregistrer
        self.conn.commit()

    def insert_citation(self, citation, tags) :
        #enregistrement de la date grâce à datetime et conversion pour ne pas avoir de pb de date à cause du SQL
        try:
            self.cursor.execute("""
                INSERT INTO citations (citation, tags) VALUES (?, ?)
            """, (citation, tags))
            # on commit comme demandé
            self.conn.commit()

        except sqlite3.IntegrityError :
            print(f"Warning : une même citation apparaît deux fois")

    def get_all_citations(self) :
        self.cursor.execute("SELECT * FROM citations")
        #renvoie toutes les données du curseur
        return self.cursor.fetchall()

    def ferme_base(self) :
        self.conn.close()