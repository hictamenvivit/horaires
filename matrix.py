# coding: utf-8
from main import Allosession
from grades import get_grades

def access_key_or_zero(key, dico):
    return dico[key] if dico[key] else 0

def get_positif_cdc_grades():
    a = Allosession()
    resss = list()
    for x in a.all_films:
        resss.append({**x, **get_grades(x['code'])})

    positif_cdc_grades = [{
        "name": j["name"],
        "Positif": access_key_or_zero("Positif", j),
        "CdC": access_key_or_zero("Cahiers du cinéma", j)
    } for j in resss]


    return [
        [[film['name'] for film in positif_cdc_grades if film["Positif"] == n and film["CdC"] == m] for m in range(6)]
    for n in range(6)]




    #
    # y = [j["Positif"] if j["Positif"] else 0 for j in resss]
    # c= "Cahiers du cinéma"
    # x = [j[c] if j[c] else 0 for j in resss]
