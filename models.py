from datetime import datetime as dt
import json
from allocine import *



def get_formatted_showtimes(theaters_dict, jour_choisi=dt.strftime(dt.today(),"%Y-%m-%d")):
    theaters_codes = ','.join(theaters_dict.keys())
    
    stimes = showtimelist(theaters=theaters_codes)

    theaterstimes = stimes['feed']['theaterShowtimes']

    result = list()
    for cinema in theaterstimes:
        code_cine = cinema['place']['theater']['code']
        nom_cine = theaters_dict[code_cine]
        liste_films = []
        films = cinema['movieShowtimes']
        for film in films:
            if 'scr' not in film.keys():
                continue
            scr = film['scr'][0]
            date = scr['d']
            if date == jour_choisi:
                ce_film = {
                    'titre': film['onShow']['movie']['title'],
                    'horaires':[i['$'] for i in scr['t'] ],
                    'directors': film['onShow']['movie']['castingShort']['directors'],
                    'code': film['onShow']['movie']['code']
                }
                ce_film['join_horaires'] = ' | '.join(ce_film['horaires'])
                liste_films.append(ce_film)
        result.append(dict(theater_name=nom_cine, movies_list=liste_films))
    return result
    
noms_simples = {
'C0020':'La Filmo',
'C0054':"L'Arlequin",
'C0073':'Le Champo',
'C0074':'Reflet Médicis',
'W7510':'Le Louxor',
'C0089':'Max Linder',
'C0102':'UGC Danton',
'C0104':'UGC Odéon',
'C0097':'MK2 Odéon (St Germain)',
'C0092':'MK2 Odéon (St Michel)',
'C0103':'UGC Montparnasse',
'C0105':'UGC Rotonde',
}



