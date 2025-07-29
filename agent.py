from memoire import Memoire

class Agent:
    def __init__(self, nom):
        self.nom = nom
        self.memoire = Memoire()

    def ajouter_rappel(self, texte, date):
        self.memoire.ajouter(texte, date)

    def afficher_rappels(self):
        return self.memoire.lister()

    def repondre_question(self, question):
        if "motivation" in question.lower():
            return "Tu peux le faire ! N’abandonne jamais 💪"
        else:
            return "Je ne connais pas encore la réponse à cette question."
