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
            return "Tu peux réussir ! Continue à travailler 💪"
        else:
            return "Je n’ai pas encore la réponse à cette question."
