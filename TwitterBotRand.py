import requests, json, time,sys
from requests_oauthlib import OAuth1
from datetime import datetime
from random import randint
import numpy

query = 'https://api.twitter.com/1.1/search/tweets.json?q=giveaway%20RT%20since%3A2017-09-10%20-filter%3Areplies&count=100'
queryes = 'https://api.twitter.com/1.1/search/tweets.json?q=sorteo%20RT%20since%3A2017-09-10%20-filter%3Areplies&count=100'

retweet = 'https://api.twitter.com/1.1/statuses/retweet/'
follow = 'https://api.twitter.com/1.1/friendships/create.json?user_id='
unfollow = 'https://api.twitter.com/1.1/friendships/destroy.json?user_id='
like = 'https://api.twitter.com/1.1/favorites/create.json?id='
comment = 'https://api.twitter.com/1.1/statuses/update.json?in_reply_to_status_id='
queryfriends = 'https://api.twitter.com/1.1/friends/ids.json'

#Authentication of the app
auth = OAuth1('kYg4claOg0rjgyGJDhvvrrF14', 'jqgDkAKn3aAziYh4sUyAnXsuQTDQ9cOCJt07baLdDSBIsmrVaD',
'918095472212004865-HeZzj5dC7tmuKjohfoZjEdIkBh65rAp', 'bAK4N9m5cuXtTy6Re3jEIyzytcRjCijIeBEZPTSHrqjh6')


r = requests.get(queryfriends, auth=auth)
r = json.loads(r.text)

friends = r['ids']

#filefollowedw = open("usrsfollowed.txt","a")
fileretweetedw = open("tweetsRT.txt","a")

#filefollowed = open("usrsfollowed.txt","r")
#followed = filefollowed.read().split()

fileretweeted = open("tweetsRT.txt","r")
retweeted = fileretweeted.read().split()

while True:

    inp = str(numpy.random.choice(numpy.arange(1, 3),p=[0.7,0.3]))
    print(inp)

    if inp == "1":
        r = requests.get(query, auth=auth)
        print ("Bot launched in ENGLISH")
    if inp == "2":
        r = requests.get(queryes, auth=auth)
        print ("Bot launched in SPANISH")

    r = json.loads(r.text)

    #Tweets resultado de la busqueda
    tweets = r["statuses"]
    n = 1

    for current in tweets:
        print ("------------------------------------------")
        print ("Working on tweet number: "+ str(n))
        print ("------------------------------------------")
        idtweet = current['id_str']
        idtweet = str(idtweet)

        if idtweet not in retweeted:

            #Perfil del poster
            poster = current["user"]["id_str"]
            nombre = current["user"]["screen_name"]
            usuarios = []
            usuarios.append(str(poster))
            nombres = []
            nombres.append(str(nombre))

            #Perfiles mencionados en el tweet
            menciones = current["entities"]["user_mentions"]

            for x in menciones:
                usuar = x["screen_name"]
                nombres.append(str(usuar))
            for perfil in menciones:
                user = perfil['id_str']
                usuarios.append(str(user))
            alr = 0
            for u in usuarios:
                if u not in friends:
                    alr+=1

            if len(friends)>=4975:
                for i in range(0,alr):
                    #us = followed.pop(0)
                    us = friends.pop(0)
                    s = requests.post(unfollow+str(us),auth=auth)
                    print (s)
                    time.sleep(120)
                    print ("Unfollowed user: "+str(us))
            for u in usuarios:
                #if u not in followed:
                if u not in friends:
                    requests.post(follow+u,auth=auth)
                    #filefollowedw.write(u+"\n")
                    #followed.append(u)
                    friends.append(u)
                    print ("Following user: "+u)

                    time.sleep(2)
                else:
                    print ("User: "+ u+" already followed")

            ur = ""
            li=""
            ur = retweet+idtweet+'.json'
            li = like+idtweet

            x = requests.post(ur,auth=auth)
            print (x)
            y = requests.post(li,auth=auth)
            time.sleep(2)


            fileretweetedw.write(idtweet+"\n")
            retweeted.append(idtweet)
            print ("Tweet: "+idtweet+" retweeted")


        else:
            print ("Tweet already retweeted")
        n+=1
    print("Last exec: "+str(datetime.now()))
    time.sleep(10800)
