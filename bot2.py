import requests, json, time
from requests_oauthlib import OAuth1

query4 = 'https://api.twitter.com/1.1/search/tweets.json?q=sorteo%20participar%20RT%20since%3A2017-09-10%20-filter%3Areplies&count=100'
query5 = 'https://api.twitter.com/1.1/search/tweets.json?q=giveaway%20RT%20since%3A2017-09-10%20-filter%3Areplies&count=100'

retweet = 'https://api.twitter.com/1.1/statuses/retweet/'
follow = 'https://api.twitter.com/1.1/friendships/create.json?user_id='
unfollow = 'https://api.twitter.com/1.1/friendships/destroy.json?user_id='
like = 'https://api.twitter.com/1.1/favorites/create.json?id='

#Este es el 2 paea los archivos
auth = OAuth1('rS0oqkR0xvAZa9oK7KHutlxCW', 'CnsrHUIEbE5JQUud36D4AYy2NXpmitrIBmYc0VbaX2DKTfP01j',
'908736211145158657-CgsniIshTXMLgb1xjCfPW7VGj9uKU8a', 'JbNO8biDz2Q24dUG2y0bFzbYbDdRmkuCMRzYFBfoFlaP3')


filefollowed = open("usrsfollowed2.txt","r")
followed = filefollowed.read().split()

fileretweeted = open("tweetsRT2.txt","r")
retweeted = fileretweeted.read().split()

filefollowedw = open("usrsfollowed2.txt","a")
fileretweetedw = open("tweetsRT2.txt","a")

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
