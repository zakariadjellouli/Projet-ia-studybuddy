# Projet-ia-studybuddy

# 🎓 StudyBuddy – Agent Intelligent Étudiant (POO + Streamlit)

Un assistant personnel intelligent 100% Python conçu pour aider les étudiants à mieux organiser leurs journées grâce à une gestion intelligente des rappels, des rendez-vous et des interactions de motivation.


# 🎯 Objectifs du projet

- Appliquer les principes de la programmation orientée objet (POO) en Python  
- Offrir une interface moderne avec Streamlit  
- Fournir une interaction intelligente via un agent  
- Gérer les rappels et événements à l’aide d’une base SQLite  
- Créer un outil simple, utile et adapté à la vie étudiante  



# 🏗️ Architecture du projet

```

┌────────────────────┐      ┌────────────────────┐
│    Interface Web   │◄────►│   Agent Intelligent │
│   (Streamlit/Flask)│      │   (Logique Python)  │
└────────────────────┘      └────────────────────┘
│                              │
▼                              ▼
┌────────────────────┐      ┌────────────────────┐
│    Mémoire (POO)   │      │    Base SQLite     │
└────────────────────┘      └────────────────────┘

```

# 📁 Structure du projet

```
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
```

# 🔧 Fonctionnalités principales

- 📝 Ajout de rappels personnalisés (texte + date)  
- 📅 Planification d’événements (titre + date + heure)  
- 💬 Interaction avec l’agent (réponses de motivation)  
- 📋 Affichage chronologique des rappels et événements  
- 💾 Stockage local avec SQLite  
- 🖥️ Interface Web : Flask + Streamlit


# 💻 Couche Data Manager (JSON) (`main.py`)

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
# 💻 Classe Agent 

```python
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

````
# 💻 Classe Memoire 

```python
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

````
# 💻 Classe Rappel 

```python
class Rappel:
    def __init__(self, texte, date):
        self.texte = texte
        self.date = date

````
# 💻 Classe Database 

```python
import sqlite3

def init_db():
    conn = sqlite3.connect("studybuddy.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS rappels (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texte TEXT NOT NULL,
            date TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_rappel(texte, date):
    conn = sqlite3.connect("studybuddy.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO rappels (texte, date) VALUES (?, ?)", (texte, date))
    conn.commit()
    conn.close()

def get_rappels():
    conn = sqlite3.connect("studybuddy.db")
    cursor = conn.cursor()
    cursor.execute("SELECT texte, date FROM rappels")
    rappels = cursor.fetchall()
    conn.close()
    return rappels

def init_events():
    conn = sqlite3.connect("studybuddy.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS evenements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            date TEXT NOT NULL,
            heure TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def insert_event(titre, date, heure):
    conn = sqlite3.connect("studybuddy.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO evenements (titre, date, heure) VALUES (?, ?, ?)", (titre, date, heure))
    conn.commit()
    conn.close()

def get_events():
    conn = sqlite3.connect("studybuddy.db")
    cursor = conn.cursor()
    cursor.execute("SELECT titre, date, heure FROM evenements ORDER BY date, heure")
    events = cursor.fetchall()
    conn.close()
    return events

````
# 🖼️ Interface Web
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

# Initialisation de l’agent
agent = Agent("StudyBuddy")

st.set_page_config(page_title="StudyBuddy - Agent Intelligent", page_icon="🧠")
st.title("🧠 StudyBuddy - Assistant Étudiant")

st.sidebar.header("Ajouter un élément")

# --- Ajouter un rappel ---
st.sidebar.subheader("📌 Ajouter un rappel")
texte_rappel = st.sidebar.text_input("Contenu du rappel")
date_rappel = st.sidebar.date_input("Date", datetime.date.today())

if st.sidebar.button("Ajouter le rappel"):
    if texte_rappel:
        agent.ajouter_rappel(texte_rappel, str(date_rappel))
        st.sidebar.success("✅ Rappel ajouté avec succès !")
    else:
        st.sidebar.error("❌ Veuillez entrer un texte.")

# --- Ajouter un événement ---
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

# --- Poser une question ---
st.subheader("💬 Poser une question à l’agent")
question = st.text_input("Ex : Donne-moi de la motivation")

if st.button("Poser la question"):
    if question:
        reponse = agent.repondre_question(question)
        st.success(reponse)
    else:
        st.warning("❗ Veuillez écrire une question.")

# --- Affichage des rappels ---
st.subheader("📋 Vos rappels")
rappels = agent.afficher_rappels()
if rappels:
    for r in rappels:
        st.markdown(f"🗒️ **{r[0]}** — {r[1]}")
else:
    st.info("Aucun rappel enregistré.")

# --- Affichage des événements ---
st.subheader("📅 Vos événements")
events = agent.memoire.lister_evenements()
if events:
    for e in events:
        st.markdown(f"📌 **{e[0]}** — {e[1]} à {e[2]}")
else:
    st.info("Aucun événement enregistré.")

```
# ✅ Accès
-Interface Streamlit : http://localhost:8501
-API REST : http://127.0.0.1:5000 


# 📊 Métriques du projet

| Fichier                 | Lignes |
| ----------------------- | ------ |
| agent.py                | 18     |
| memoire.py              | 14     |
| database.py             | 58     |
| interface\_streamlit.py | 65     |

> ✅ Résultat : un code plus clair, maintenable et évolutif !

# 🎓 Avantages Pédagogiques

* Apprentissage de la POO en Python
* Utilisation d’une base SQLite pour la persistance
* Développement de deux interfaces (Terminal + Web)
* Projet utile et réaliste pour les étudiants
* Bon point de départ pour les projets plus complexes

---




