# coding: utf-8

from allocine import reviewlist

def extractor(journal_code, journal_name):
    def result(rl):
        r = rl['feed']['review']
        for x in r:
            if x['newsSource']['code'] == journal_code:
                return x['rating']
        raise ValueError('Pas de %s' % journal_name)
    return result


with open('reviews_codes.json', 'r') as f:
    import json
    liste = json.load(f)
    
extractors = {k['name'] : extractor(int(k['code']), k['name']) for k in liste}

def get_grades(movie_code):
    rl = reviewlist(movie_code)
    res = dict()
    for k,v in extractors.items():
        try:
            res[k] = v(rl)
        except:
            #raise
            res[k] = None
    return res

