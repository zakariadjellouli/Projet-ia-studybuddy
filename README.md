# Projet-ia-studybuddy
Voici un fichier `README.md` **complet**, prêt à être copié-collé dans ton dépôt GitHub `Projet-ia-studybuddy` :

---

```markdown
# 🎓 StudyBuddy – Agent Intelligent Étudiant (POO + Streamlit)

Un assistant personnel intelligent 100% Python conçu pour aider les étudiants à mieux organiser leurs journées grâce à une gestion intelligente des rappels, des rendez-vous et des interactions de motivation.

---

## 🎯 Objectifs du projet

- Appliquer les principes de la programmation orientée objet (POO) en Python  
- Offrir une interface moderne avec Streamlit  
- Fournir une interaction intelligente via un agent  
- Gérer les rappels et événements à l’aide d’une base SQLite  
- Créer un outil simple, utile et adapté à la vie étudiante  

---

## 🏗️ Architecture du projet



┌────────────────────┐      ┌────────────────────┐
│    Interface Web   │◄────►│   Agent Intelligent │
│   (Streamlit/Flask)│      │   (Logique Python)  │
└────────────────────┘      └────────────────────┘
│                              │
▼                              ▼
┌────────────────────┐      ┌────────────────────┐
│    Mémoire (POO)   │      │    Base SQLite     │
└────────────────────┘      └────────────────────┘



## 📁 Structure du projet

studybuddy/
├── agent.py                 # Classe Agent (logique principale)
├── memoire.py              # Classe Mémoire (accès base de données)
├── rappel.py               # Classe Rappel (modèle)
├── database.py             # Fonctions SQLite (CRUD)
├── app.py                  # Interface web Flask
├── interface\_streamlit.py  # Interface web avec Streamlit
├── templates/
│   └── index.html          # Template HTML pour Flask
├── studybuddy.db           # Base de données SQLite (auto-créée)
└── README.md               # Documentation du projet


## 🔧 Fonctionnalités principales

- 📝 Ajout de rappels personnalisés (texte + date)  
- 📅 Planification d’événements (titre + date + heure)  
- 💬 Interaction avec l’agent (réponses de motivation)  
- 📋 Affichage chronologique des rappels et événements  
- 💾 Stockage local avec SQLite  
- 🖥️ Interface Web : Flask + Streamlit

---

## 💻 Couche Data Manager (JSON) (`main.py`)

```python
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
            date = input("Date (ex: année-mois-jour) : ")
            heure = input("Heure (ex: heure:minute am/pm) : ")
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
````

---

## 🖼️ Interface Web
## Version Flask
- Formulaires pour :
- Ajouter des rappels
- Ajouter des événements
- Poser une question à l’agent
- Affichage dynamique de tous les événements et rappels
## Version Streamlit
- Interface plus moderne avec widgets
- Interaction directe avec la classe Agent
- Résultats affichés en temps réel (via st.markdown, st.success, etc.)

```python
import streamlit as st
from agent import Agent
import datetime

agent = Agent("StudyBuddy")

st.set_page_config(page_title="StudyBuddy - Agent Intelligent", page_icon="🧠")
st.title("🧠 StudyBuddy - Assistant Étudiant")

st.sidebar.header("Ajouter un élément")

st.sidebar.subheader("📌 Ajouter un rappel")
texte_rappel = st.sidebar.text_input("Contenu du rappel")
date_rappel = st.sidebar.date_input("Date", datetime.date.today())

if st.sidebar.button("Ajouter le rappel"):
    if texte_rappel:
        agent.ajouter_rappel(texte_rappel, str(date_rappel))
        st.sidebar.success("✅ Rappel ajouté avec succès !")
    else:
        st.sidebar.error("❌ Veuillez entrer un texte.")

st.sidebar.subheader("📅 Ajouter un événement")
titre_event = st.sidebar.text_input("Titre de l’événement")
date_event = st.sidebar.date_input("Date de l’événement", datetime.date.today())
heure_event = st.sidebar.time_input("Heure", datetime.time(12, 0))

if st.sidebar.button("Ajouter l’événement"):
    if titre_event:
        agent.memoire.ajouter_evenement(titre_event, str(date_event), str(heure_event))
        st.sidebar.success("✅ Événement ajouté avec succès !")
    else:
        st.sidebar.error("❌ Veuillez entrer un titre.")

st.subheader("💬 Poser une question à l’agent")
question = st.text_input("Ex : Donne-moi de la motivation")

if st.button("Poser la question"):
    if question:
        reponse = agent.repondre_question(question)
        st.success(reponse)
    else:
        st.warning("❗ Veuillez écrire une question.")

st.subheader("📋 Vos rappels")
rappels = agent.afficher_rappels()
if rappels:
    for r in rappels:
        st.markdown(f"🗒️ **{r[1]}** — {r[2]}")
else:
    st.info("Aucun rappel enregistré.")

st.subheader("📅 Vos événements")
events = agent.memoire.lister_evenements()
if events:
    for e in events:
        st.markdown(f"📌 **{e[0]}** — {e[1]} à {e[2]}")
else:
    st.info("Aucun événement enregistré.")
```

---

## 📊 Métriques du projet

| Fichier                 | Lignes |
| ----------------------- | ------ |
| agent.py                | 18     |
| memoire.py              | 14     |
| database.py             | 58     |
| interface\_streamlit.py | 65     |

> ✅ Résultat : un code plus clair, maintenable et évolutif !

---

## 🎓 Avantages Pédagogiques

* Apprentissage de la POO en Python
* Utilisation d’une base SQLite pour la persistance
* Développement de deux interfaces (Terminal + Web)
* Projet utile et réaliste pour les étudiants
* Bon point de départ pour les projets plus complexes

---




