Skip to content
 
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 @hictamenvivit Sign out
0
0 0 hictamenvivit/moutarde1
 Code  Issues 0  Pull requests 0  Projects 0  Wiki  Insights  Settings
moutarde1/horaires/ 
allocine.py
  or cancel
 Indent mode Indent size Line wrap mode
1
import hashlib
2
from base64 import b64encode
3
try: # python3
4
        from urllib.parse import urlencode
5
except: #python2
6
        from urllib import urlencode
7
import requests
8
import time
9
import json
10
from pprint import pprint # for a more readable json output
11
​
12
ALLOCINE_BASE_URL = "http://api.allocine.fr/rest/v3/"
13
ALLOCINE_PARTNER_KEY = '100043982026'
14
ALLOCINE_SECRET_KEY = '29d185d98c984a359e6e6f26a0474269'
15
ANDROID_USER_AGENT = 'Dalvik/1.6.0 (Linux; U; Android 4.2.2; Nexus 4 Build/JDQ39E)'
16
​
17
​
18
def do_request(method, params):
19
    sed = time.strftime("%Y%m%d")
20
    sha1 = hashlib.sha1()
21
    PARAMETER_STRING = "partner=" + ALLOCINE_PARTNER_KEY + "&" + "&".join([k + "=" + params[k] for k in params.keys()]) + "&sed=" + sed
22
    SIG_STRING = bytes(ALLOCINE_SECRET_KEY + PARAMETER_STRING, 'utf-8')
23
    sha1.update(SIG_STRING)
24
    SIG_SHA1 = sha1.digest()
25
    SIG_B64 = b64encode(SIG_SHA1).decode('utf-8')
26
    sig = urlencode({SIG_B64: ''})[:-1]
27
    URL = ALLOCINE_BASE_URL + method + "?" + PARAMETER_STRING + "&sig=" + sig
28
    headers = {'User-Agent': ANDROID_USER_AGENT}
29
    results = requests.get(URL, headers=headers).text
30
    try:
31
        return json.loads(results)
32
    except Exception as e:
33
        return results
34
​
35
​
36
# search :
37
#   q : string to search
38
#   format (optionnal) : returns the result in JSON or XML format ("json" or "xml", default set to JSON)
39
#   filter (optionnal) : filter depending on the result type ("movie", "theater", "person", "news", "tvseries", separated by a comma)
40
#   count (optionnal) : number of results to return (should be an integer)
41
#   page (optionnal) : number of the results page to return (default is 10 results by page)
42
def search(string, format="json", filter=None, count=None, page=None):
43
    data = {'q': str(string), 'format': str(format)}
44
    if filter is not None:
45
        data["filter"] = filter.replace(",", "%2C")
46
    if count is not None:
47
        data["count"] = str(count)
48
    if page is not None:
49
        data["page"] = str(page)
@hictamenvivit
Commit changes
Commit summary 
Update allocine.py
Optional extended description

Add an optional extended description…
  Commit directly to the master branch.
  Create a new branch for this commit and start a pull request. Learn more about pull requests.
 
© 2019 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
Press h to open a hovercard with more details.