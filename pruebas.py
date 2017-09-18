import requests, json, time
from requests_oauthlib import OAuth1

follow = 'https://api.twitter.com/1.1/application/rate_limit_status.json?resources=friends'

"""
#Este es el 1 para los archivos
auth = OAuth1('Nx9rVLQQsnxd8mFOTW1UoW72E', 'AY6OgZM9vKYgFXmtXkmdesOjQmTQ08flsysN4P1donnNj4Jsus',
'904738341723275265-idfFp3jVQoDsePceeQ36DaxQrIGp0MM', 'llR5WLOlSq1M1EQqNFVFzitKb74YM2QiVdQEI28ditdGJ')
"""
#Este es el 2 para los archivos

auth = OAuth1('LQ1XZNJAfrDTiFHy4hbbUpiit', 'OW06q0yH12OhpDCSB6HPmsVMafUXMHLyR6mKnuS2lR5cUS3qyj',
'908321269640257536-czMN5xmNtDXWcPchTttXlh3UJQM9LR6', 'EQdMIztXUiIQpQpEp0od1LUjoYlmSSpsL0d0vOxCHxML2')

#print r["statuses"]["/statuses/retweets/:id"]
f = open('tweetsRT2.txt','r')
r = f.read().split()
print len(r)
