import json, random


def load_candidates_from_json():    # возвращает список всех кандидатов
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)


def get_candidate(ids):  #возвращает одного кандидата по его id
    id_candidate = load_candidates_from_json()
    return id_candidate[ids - 1]


def get_candidates_by_name(candidate_name): #возвращает кандидатов по имени
    result=[]
    for candidate in load_candidates_from_json():
        if candidate_name in candidate['name']:
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name):    #возвращает кандидатов по навыку
    result=[]
    for candidate in load_candidates_from_json():
        if skill_name.lower() in candidate['skills'].lower():
            result.append(candidate)
    return result
