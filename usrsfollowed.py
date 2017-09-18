import requests, json, time
from requests_oauthlib import OAuth1

f =  open ("usrsfollowed2.txt", "a")
auth = OAuth1('rS0oqkR0xvAZa9oK7KHutlxCW', 'CnsrHUIEbE5JQUud36D4AYy2NXpmitrIBmYc0VbaX2DKTfP01j',
'908736211145158657-CgsniIshTXMLgb1xjCfPW7VGj9uKU8a', 'JbNO8biDz2Q24dUG2y0bFzbYbDdRmkuCMRzYFBfoFlaP3')

query = 'https://api.twitter.com/1.1/friends/ids.json'

r = requests.get(query, auth=auth)
r = json.loads(r.text)

friends = r['ids']

for fr in friends:
    f.write(str(fr)+"\n")
f.close()
