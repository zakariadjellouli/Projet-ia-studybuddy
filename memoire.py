from database import insert_rappel, get_rappels

class Memoire:
    def ajouter(self, texte, date):
        insert_rappel(texte, date)

    def lister(self):
        return get_rappels()
