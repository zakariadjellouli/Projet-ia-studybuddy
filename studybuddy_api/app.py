from flask import Flask, request, render_template, redirect, url_for
from agent import Agent
from database import init_db, init_events, get_rappels, get_events, insert_rappel, insert_event

app = Flask(__name__)
agent = Agent("StudyBuddy")

init_db()
init_events()

@app.route('/')
def index():
    rappels = get_rappels()
    events = get_events()
    return render_template("index.html", rappels=rappels, events=events)

@app.route('/add_rappel', methods=['POST'])
def add_rappel():
    texte = request.form.get('texte')
    date = request.form.get('date')
    insert_rappel(texte, date)
    return redirect(url_for('index'))

@app.route('/add_event', methods=['POST'])
def add_event():
    titre = request.form.get('titre')
    date = request.form.get('date')
    heure = request.form.get('heure')
    insert_event(titre, date, heure)
    return redirect(url_for('index'))

@app.route('/ask', methods=['POST'])
def ask():
    question = request.form.get('question')
    reponse = agent.repondre_question(question)
    return render_template("index.html", rappels=get_rappels(), events=get_events(), reponse=reponse)

if __name__ == '__main__':
    app.run(debug=True)
