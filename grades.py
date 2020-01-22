# coding: utf-8

from allocine import reviewlist, movie

def extractor(journal_code, journal_name):
    """
    Returns the grade as int
    """
    def result(rl):
        r = rl['feed']['review']
        for x in r:
            if x['newsSource']['code'] == journal_code:
                return x['rating']
        raise ValueError('Pas de %s' % journal_name)
    return result
    
def complete_extractor(journal_code, journal_name):
    """
    Returns the grade and review as dict
    """
    def result(rl):
        r = rl['feed']['review']
        for x in r:
            if x['newsSource']['code'] == journal_code:
                return dict(rating=x['rating'], body=x['body'])
        raise ValueError('Pas de %s' % journal_name)
    return result



with open('reviews_codes.json', 'r') as f:
    import json
    liste = json.load(f)
    
extractors = {k['name'] : extractor(int(k['code']), k['name']) for k in liste}
complete_extractors = {k['name'] : complete_extractor(int(k['code']), k['name']) for k in liste}



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



def get_grades_and_reviews(movie_code):
    rl = reviewlist(movie_code)
    try:
        synopsis = movie(movie_code)['movie']['synopsisShort'].replace('\xa0','')
    except:
        synopsis = None
    reviews = dict()
    
    for k,v in complete_extractors.items():
        k = k.split(" ")[0]
        try:
            reviews[k] = v(rl)
        except:
            #raise
            reviews[k] = None
    
    
    return {
        "synopsis": synopsis,
        "reviews": reviews
    }
