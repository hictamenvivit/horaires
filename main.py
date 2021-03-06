from allocine import *

from datetime import datetime as dt



class Allosession():

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
    
    choix_l = noms_simples.keys()
    
    choix = ','.join(choix_l)
    dico = {}
    total = showtimelist(theaters=choix)
    stimes = total['feed']['theaterShowtimes']
    
    def __init__(self, jour_choisi=dt.strftime(dt.today(),"%Y-%m-%d")):
        for cinema in self.stimes:
            code_cine = cinema['place']['theater']['code']
            nom_cine = self.noms_simples[code_cine]
            liste_films = []
            films = cinema['movieShowtimes']
            for film in films:
                if 'scr' not in film.keys():
                    continue
                scr = film['scr'][0]
                date = scr['d']
                if date == jour_choisi:
                    try:
                        directors = film['onShow']['movie']['castingShort']['directors']
                    except KeyError:
                        directors = "Directors not found"
                    ce_film = {
                        'titre': film['onShow']['movie']['title'],
                        'code': film['onShow']["movie"]["code"],
                        'horaires':[i['$'] for i in scr['t'] ],
                        'directors': directors
                    }
                    ce_film['join_horaires'] = ' | '.join(ce_film['horaires'])
                    liste_films.append(ce_film)
            self.dico[nom_cine] = liste_films

    @property
    def all_films(self):
        liste = [{"name":film["titre"], "code":film["code"]} for x in self.dico.keys() for film in self.dico[x]]
        result = []
        for x in liste:
            if not x in result:
                result.append(x)
        return result
    
    def str_dico(self):
        resultat = ''
        for nom_cinema in self.dico.keys():
            resultat += nom_cinema + '\n'
            liste_films = self.dico[nom_cinema]
            for film in liste_films:
                horaires = ' | '.join(film['horaires'])
                titre = "{0} ({1})".format(film['titre'], film['directors'])
                resultat += "    {0}    {1}\n".format(titre,horaires)
            resultat += '\n\n'
        return resultat

    def ecrire_horaires(self):
        fichier = open('horaires','w+')
        fichier.write(self.str_dico())
        fichier.close()

a = Allosession()
