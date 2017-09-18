import requests, json, time
from requests_oauthlib import OAuth1

query4 = 'https://api.twitter.com/1.1/search/tweets.json?q=sorteo%20participar%20RT%20since%3A2017-09-10%20-filter%3Areplies&count=100'
query5 = 'https://api.twitter.com/1.1/search/tweets.json?q=giveaway%20RT%20since%3A2017-09-10%20-filter%3Areplies&count=100'

retweet = 'https://api.twitter.com/1.1/statuses/retweet/'
follow = 'https://api.twitter.com/1.1/friendships/create.json?user_id='
unfollow = 'https://api.twitter.com/1.1/friendships/destroy.json?user_id='
like = 'https://api.twitter.com/1.1/favorites/create.json?id='



#Este es el 1 para los archivos

auth = OAuth1('LQ1XZNJAfrDTiFHy4hbbUpiit', 'OW06q0yH12OhpDCSB6HPmsVMafUXMHLyR6mKnuS2lR5cUS3qyj',
'908321269640257536-czMN5xmNtDXWcPchTttXlh3UJQM9LR6', 'EQdMIztXUiIQpQpEp0od1LUjoYlmSSpsL0d0vOxCHxML2')


filefollowed = open("usrsfollowed1.txt","r")
followed = filefollowed.read().split()

fileretweeted = open("tweetsRT1.txt","r")
retweeted = fileretweeted.read().split()

filefollowedw = open("usrsfollowed1.txt","a")
fileretweetedw = open("tweetsRT1.txt","a")

r = requests.get(query5, auth=auth)
r = json.loads(r.text)

#Tweets resultado de la busqueda
tweets = r["statuses"]

for tweetprin in tweets:

    #Perfil del poster
    poster = tweetprin["user"]["id_str"]
    usuarios = []
    usuarios.append(poster)
    #follow = follow+poster
    #requests.post(str(follow),auth=auth)
    #Perfiles mencionados en el tweet
    menciones = tweetprin["entities"]["user_mentions"]
    for perfil in menciones:
        user = perfil['id_str']
        usuarios.append(user)

    if len(followed)>=5000:
        for user in usuarios:
            us = followed.pop(0)
            f3=""
            f3 = unfollow+us
            requests.post(str(f3),auth=auth)
            print "Unfollowed user: "+us

    for u in usuarios:
        if str(u) not in followed:
            f2=""
            f2 = follow+u
            requests.post(str(f2),auth=auth)
            filefollowedw.write(str(u)+"\n")
            followed.append(str(u))
            print "Following user: "+u

            time.sleep(0.5)
        else:
            print "User: "+ u+" already followed"

    idtweet = tweetprin["id_str"]
    if str(idtweet) not in retweeted:
        ur = ""
        li=""
        ur = str(retweet+idtweet+'.json')
        li = like+str(idtweet)
        x = requests.post(ur,auth=auth)
        y = requests.post(li,auth=auth)
        fileretweetedw.write(idtweet+"\n")
        retweeted.append(idtweet)
        print "Tweet: "+idtweet+" retweeted"
    else:
        print "Tweet "+idtweet+" already retweeted"

    time.sleep(1)
filefollowedw.close()
fileretweetedw.close()
