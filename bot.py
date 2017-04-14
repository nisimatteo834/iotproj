from __future__ import print_function
from database import Packet
import requests
import json
import datetime
import cherrypy
import paho.mqtt.publish as publish
import time
import telepot
import asynchat
from database import Packet
import threading

def retrievePosition():
    pos = json.loads(requests.get('https://api.thingspeak.com/channels/252276/feeds/last').content)

    stringa = '{"lat" :' + str(pos['field3']) + ',"long": ' + str(pos['field4']) +'}'

    return stringa



def on_message(msg):
    print ('Son passato')

    #msg = bot.getUpdates()
    lena = len(msg)
    if lena != 0:
        id = msg['chat']['id']


        try:
            if (any(msg['entities'])):
                if(msg['entities'][0]['type']== 'bot_command'):
                    if msg['text'] == '/getPosition':
                        try:
                            po = retrievePosition()
                            print (po)
                            pos = json.loads(po)
                            bot.sendLocation(id,pos['lat'],pos['long'])
                            return

                        except Exception as detail:
                            print (detail)

        except:
            bot.sendMessage(id,'You should send me a /command')

if __name__ == '__main__':
    bot = telepot.Bot('253148548:AAHW7DkmO0i26DC6F5NuIQCTzzMyn_wcXxM')
    bot.message_loop({'chat':on_message},run_forever=True)