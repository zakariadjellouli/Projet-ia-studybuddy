from database import insert_event, get_events, init_events
from agent import Agent
from database import init_db


def menu():
    print("\n🧠 Bienvenue dans StudyBuddy !")
    print("1. Ajouter un rappel")
    print("2. Afficher les rappels")
    print("3. Poser une question")
    print("4. Quitter")
    print("5. Ajouter un rendez-vous")
    print("6. Voir les rendez-vous")

def main():
    init_db()
    init_events()

    agent = Agent("StudyBuddy")
    
    while True:
        menu()
        choix = input("Votre choix : ")

        if choix == "1":
            texte = input("Entrez le rappel : ")
            date = input("Entrez la date (ex: 2025-07-14) : ")
            agent.ajouter_rappel(texte, date)
            print("✅ Rappel ajouté !")

        elif choix == "2":
            rappels = agent.afficher_rappels()
            if not rappels:
                print("📭 Aucun rappel.")
            else:
                print("📌 Vos rappels :")
                for r in rappels:
                    print(f"- {r[0]} (pour le {r[1]})")

        elif choix == "3":
            question = input("Pose ta question : ")
            reponse = agent.repondre_question(question)
            print(f"🤖 StudyBuddy : {reponse}")

        elif choix == "4":
            print("👋 À bientôt !")
            break

        elif choix == "5":
            titre = input("Titre du rendez-vous : ")
            date = input("Date (ex: anneé-mois-jour ) : ")
            heure = input("Heure (ex: heure:minute am/pm ) : ")
            insert_event(titre, date, heure)
            print("📅 Rendez-vous ajouté avec succès !")

        elif choix == "6":
            events = get_events()
            if not events:
                print("📭 Aucun rendez-vous prévu.")
            else:
                print("📌 Vos rendez-vous à venir :")
                for e in events:
                    print(f"- {e[0]} le {e[1]} à {e[2]}")

        else:
            print("❌ Choix invalide, réessayez.")

if __name__ == "__main__":
    main()
