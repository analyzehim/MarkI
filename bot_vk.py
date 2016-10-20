# -*- coding: cp1251 -*-
import os
import sys
import vkontakte
import time
import unicodedata
import datetime
from bot_const import *


def delete_mes(count1, offset1):
    del_mes=0
    vk = vkontakte.API(token=VK_ACCES_TOKEN)
    print "Connecting"
    try:
        messages = vk.messages.get(count=count1, offset=offset1)
        print datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
        for m in messages:
            if (type(m)==dict):
                try:
                    #print m["body"],m["uid"]
                    if (m["chat_id"]==CHAT_ID):
                        #print m["uid"]
                        if (str(m["uid"]) in VK_DEL):
                            m["attachments"][0]['photo']
                            print VK_USERS[str(m["uid"])]+' '+ str(datetime.datetime.fromtimestamp(m["date"]).strftime('%Y-%m-%d %H:%M:%S'))
                            vk.messages.delete(message_ids=m["mid"])
                            del_mes+=1
                            time.sleep(1)
                                    
                                    
                except KeyError:
                    if (sys.exc_info()[1][0]=='attachments'):
                        if not("http" in m["body"]) :
                            try:
                                k=m["body"].encode('cp1251')
                            except:
                                k=m["body"].encode('utf-8')
                        if ("жен" in k) or ("Жен" in k) or ("Раев" in k) or ("раев" in k):
                            continue
                        print VK_USERS[str(m["uid"])]+' '+ str(datetime.datetime.fromtimestamp(m["date"]).strftime('%Y-%m-%d %H:%M:%S'))
                        vk.messages.delete(message_ids=m["mid"])
                        del_mes+=1
                        time.sleep(1)      
                except:
                    print sys.exc_info()
        return del_mes

    except KeyboardInterrupt:
        return del_mes
    except:      
        print sys.exc_info()
        return del_mes