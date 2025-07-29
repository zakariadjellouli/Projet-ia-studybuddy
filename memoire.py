from database import insert_rappel, get_rappels, insert_event, get_events

class Memoire:
    def ajouter(self, texte, date):
        insert_rappel(texte, date)

    def lister(self):
        return get_rappels()

    def ajouter_evenement(self, titre, date, heure):
        insert_event(titre, date, heure)

    def lister_evenements(self):
        return get_events()
