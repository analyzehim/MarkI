import requests
import json
'''
import http.client
conn = http.client.HTTPConnection("lectureswww.readthedocs.org")
conn.request("GET", "/ru/latest/")
r1 = conn.getresponse()
print(r1.status)
'''
URL = 'https://api.telegram.org/bot' # HTTP Bot API URL
TOKEN = '119170444:AAGu9QuWoZ7WFAIQS-1q1Az4rhzHQdiFfDk' # My Token
#data1 = json.loads('"text": "Hello","chat_id": 74102915,"reply_markup":{"keyboard":[["0"],["1"]], "one_time_keyboard":true}')


#data = {'chat_id': 74102915, 'text': 1} # Request create

#print data, URL + TOKEN + '/sendMessage'

data = {'text': 1, 'chat_id': 74102915, 'reply_markup':{'keyboard':[ [ "Top Left", "Top Right" ], [ "Bottom Left", "Bottom Right" ] ],'one_time_keyboard':True}}
data1 = json.dumps(data)
data1 = {"text":1, "chat_id": 74102915, "reply_markup":{"keyboard":[["0"],["1"]], "one_time_keyboard":True} }

r =  requests.post(URL + TOKEN + '/sendMessage',json=data1)
print data1
print r.content