import requests, json, time
from requests_oauthlib import OAuth1

auth = OAuth1('WH4IyxFDHtg6o4Yknk427mciJ', 'xKAitAvUTsI9GifC6V4omSRanenG781G8hiwu7UCk1VmJTjjT3',
'904738341723275265-8ojjyg43cWg0qE49lcCsxnaO7uSbKRn', 'kklNhm6fXvV5p29t04OQzCzWa3M959iPvEqafP5CZx7sa')

query = 'https://api.twitter.com/1.1/friends/ids.json'
unfollow = 'https://api.twitter.com/1.1/friendships/destroy.json?user_id='
credentials = 'https://api.twitter.com/1.1/account/verify_credentials.json'

r = requests.get(query, auth=auth)
r = json.loads(r.text)

friends = r['ids']

for f in friends:
    que=""
    que = unfollow+str(f)
    print(que)
    ans = requests.post(que,auth=auth)
    if ans==f:
        print "Unfollow of user: "+str(f)+" successful"
    else:
        print ans
    time.sleep(1)
