from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

@app.route('/')
def index_page():
    candidates_list = []
    for candidate in load_candidates_from_json():
        candidates_list.append(candidate['name'])
    return render_template('list.html', candidates_list=candidates_list)

@app.route('/candidate/<int:id>')
def candidate_page(id):
    return render_template('card.html', candidate=get_candidate(id))

@app.route('/search/<candidate_name>')
def search_name_page(candidate_name):
    return render_template('search.html', candidates=get_candidates_by_name(candidate_name))

@app.route('/skill/<candidate_skill>')
def search_skill_page(candidate_skill):
    return render_template('skill.html', skill=candidate_skill, candidates=get_candidates_by_skill(candidate_skill))

if __name__ == '__main__':
    app.run(debug = True)
