import requests
import json
#Основа


api='https://api.vk.com/method/'
token='token'
payload={'access_token':token, 'v':'5.60'}
selfid=222692489



#посты на стену

def wallpost(owner_id, message):
	payload['message']=str(message) #загоняем сообщение в пейлоад
	payload['owner_id']=str(owner_id) #загоняем id в пейлоад
	requests.post(api+'wall.post', payload)
	return 'successfully posted to id ' + str(owner_id) + ': ' + str(message)
	

#личное сообщение

def sendmessage(id, message, attachment):
	if attachment != 0:
		payload['attachment']=str(attachment)
	payload['message']=str(message)
	payload['id']=int(id)
	requests.post(api+'messages.send', payload)
	return 'successfully sent to id ' + str(id)+': '+str(message)
		
#Прикрепление к сообщению
		
def attach(type, owner_id, media_id, access_key):
	if access_key == 0:
		access_key=''
	type=str(type)
	owner_id=str(owner_id)
	media_id='_'+str(media_id)
	return str(type+owner_id+media_id+access_key)
	
#Получение сообщения

def getmessage(out, count):
	payload['out']=str(out)
	payload['count']=str(count)
	return json.loads(requests.get(api+'messages.get', payload).text)['response']['items'][0]
	
#Разложение сообщения

def messageanalysis(message):
	m=message
	mes={
	'date':m['date'],
	'id':m['id'],
	'user_id':m['user_id'],
	'body':m['body']}
	return mes

	
		
