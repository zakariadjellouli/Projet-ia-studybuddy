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
        st.markdown(f"🗒️ **{r[1]}** — {r[2]}")
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
