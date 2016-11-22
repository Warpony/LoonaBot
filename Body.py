#Функции бота
import Basemethods
import time
import Answers
import json
import requests
from Answers import *

work = True
count = 0

while (work == True):

    m=Basemethods.messageanalysis(Basemethods.getmessage(0,1))
    
    for i in Answers.stop:
        if i in m['body']:
                if m['user_id']==222692489:
                    work = False
                    print('Программа завершена по коду в сообщении')
                    break
            
    else:
        print('User_id: '+str(m['user_id'])+'\nMessage: '+str(m['body'])+'\n')
        print(1)
        count+=1

        body=m['body'].split()
        print(body)
        
        for word in body:
            if word in hello:
                Basemethods.sendmessage(m['user_id'], 'Привет', 0)
            elif word in goodbye:
                Basemethods.sendmessage(m['user_id'], 'Пока', 0)
            elif word in stat:
                Basemethods.sendmessage(m['user_id'], 'Статистика пока не настроена:(', 0)
        
            
    time.sleep(0.15)
    
