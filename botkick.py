# -*- coding: utf-8 -*-
# Edited from script LineVodka script made by AntonLow
from LineAlpha import LineClient
from LineAlpha.LineApi import LineTracer
from LineAlpha.LineThrift.ttypes import Message
from LineAlpha.LineThrift.TalkService import Client
import time, datetime, random ,sys, re, string, os, json

reload(sys)
sys.setdefaultencoding('utf-8')

client = LineClient()
client._qrLogin("line://au/q/")

profile, setting, tracer = client.getProfile(), client.getSettings(), LineTracer(client)
offbot, messageReq, wordsArray, waitingAnswer = [], {}, {}, {}

print client._loginresult()

wait = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
   }

setTime = {}
setTime = wait["setTime"]

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text

    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    client._client.sendMessage(messageReq[to], mes)

def SEND_MESSAGE(op):
    msg = op.message
    try:
        if msg.toType == 2:
            if msg.contentType == 0:
                #if "gname:" in msg.text:
#--------------------------------------------------------------
                if msg.text == "Kill":
                    print "ok"
                    _name = msg.text.replace("Kill All","")
                    gs = client.getGroup(msg.to)
                    sendMessage(msg.to,"Misi jones numpang lewat...\nTerimakasih")
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendMessage(msg.to,"error")
                    else:
                        for target in targets:
                            try:
                                klist=[client]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
				sendText(msg.to,"error")
#-------------------------------------------------------------			
		if msg.text == "Url":
                    sendMessage(msg.to,"line://ti/g/" + client._client.reissueGroupTicket(msg.to))
#-------------------------------------------------------------			
		if msg.text == "Open":
                    group = client.getGroup(msg.to)
                    if group.preventJoinByTicket == False:
                        sendMessage(msg.to, "already open")
                    else:
                        group.preventJoinByTicket = False
                        client.updateGroup(group)
                        sendMessage(msg.to, "URL Open")
#-------------------------------------------------------------			
		if msg.text == "Close":
                    group = client.getGroup(msg.to)
                    if group.preventJoinByTicket == True:
                        sendMessage(msg.to, "already close")
                    else:
                        group.preventJoinByTicket = True
                        client.updateGroup(group)
                        sendMessage(msg.to, "URL close")
#-------------------------------------------------------------			
		if msg.text == "Cancel":
                    group = client.getGroup(msg.to)
                    if group.invitee is None:
                        sendMessage(op.message.to, "No one is inviting.")
                    else:
                        gInviMids = [contact.mid for contact in group.invitee]
                        client.cancelGroupInvitation(msg.to, gInviMids)
                        sendMessage(msg.to, str(len(group.invitee)) + " Done")
#-------------------------------------------------------------			
		if msg.text == "Speed":
                    start = time.time()
                    sendMessage(msg.to, "Speed Test")
                    elapsed_time = time.time() - start
                    sendMessage(msg.to, "%sseconds" % (elapsed_time))
#-------------------------------------------------------------			
                if msg.text == "Spam":
                    sendMessage(msg.to,"Ku mengejar bus yang mulai berjalan")
                    sendMessage(msg.to,"Ku ingin ungkapkan kepada dirimu")
                    sendMessage(msg.to,"Kabut dalam hatiku telah menghilang")
                    sendMessage(msg.to,"Dan hal yang penting bagiku pun terlihat")
                    sendMessage(msg.to,"Walaupun jawaban itu sebenarnya begitu mudah")
                    sendMessage(msg.to,"Tetapi entah mengapa diriku melewatkannya")
                    sendMessage(msg.to,"Untukku menjadi diri sendiri")
                    sendMessage(msg.to,"Ku harus jujur, pada perasaanku")
                    sendMessage(msg.to,"Ku suka dirimu ku suka")
                    sendMessage(msg.to,"Ku berlari sekuat tenaga")
                    sendMessage(msg.to,"Ku suka selalu ku suka")
                    sendMessage(msg.to,"Ku teriak sebisa suaraku")
                    sendMessage(msg.to,"Ku suka dirimu ku suka")
                    sendMessage(msg.to,"Walau susah untukku bernapas")
                    sendMessage(msg.to,"Tak akan ku sembunyikan")
                    sendMessage(msg.to,"Oogoe daiyamondo~")
                    sendMessage(msg.to,"Saat ku sadari sesuatu menghilang")
                    sendMessage(msg.to,"Hati ini pun resah tidak tertahankan")
                    sendMessage(msg.to,"Sekarang juga yang bisa ku lakukan")
                    sendMessage(msg.to,"Merubah perasaan ke dalam kata kata")
                    sendMessage(msg.to,"Mengapa sedari tadi")
                    sendMessage(msg.to,"Aku hanya menatap langit")
                    sendMessage(msg.to,"Mataku berkaca kaca")
                    sendMessage(msg.to,"Berlinang tak bisa berhenti")
                    sendMessage(msg.to,"Di tempat kita tinggal, didunia ini")
                    sendMessage(msg.to,"Dipenuhi cinta, kepada seseorang")
                    sendMessage(msg.to,"Ku yakin ooo ku yakin")
                    sendMessage(msg.to,"Janji tak lepas dirimu lagi")
                    sendMessage(msg.to,"Ku yakin ooo ku yakin")
                    sendMessage(msg.to,"Akhirnya kita bisa bertemu")
                    sendMessage(msg.to,"Ku yakin ooo ku yakin")
                    sendMessage(msg.to,"Ku akan bahagiakan dirimu")
                    sendMessage(msg.to,"Ku ingin kau mendengarkan")
                    sendMessage(msg.to,"Oogoe daiyamondo~")
                    sendMessage(msg.to,"Jika jika kamu ragu")
                    sendMessage(msg.to,"Takkan bisa memulai apapun")
                    sendMessage(msg.to,"Ungkapkan perasaanmu")
                    sendMessage(msg.to,"Jujurlah dari sekarang juga")
                    sendMessage(msg.to,"Jika kau bersuar")
                    sendMessage(msg.to,"Cahaya kan bersinar")
                    sendMessage(msg.to,"Ku suka dirimu ku suka")
                    sendMessage(msg.to,"Ku berlari sekuat tenaga")
                    sendMessage(msg.to,"Ku suka selalu ku suka")
                    sendMessage(msg.to,"Ku teriak sebisa suaraku")
                    sendMessage(msg.to,"Ku suka dirimu ku suka")
                    sendMessage(msg.to,"Sampaikan rasa sayangku ini")
                    sendMessage(msg.to,"Ku suka selalu ku suka")
                    sendMessage(msg.to,"Ku teriakkan ditengah angin")
                    sendMessage(msg.to,"Ku suka dirimu ku suka")
                    sendMessage(msg.to,"Walau susah untuk ku bernapas")
                    sendMessage(msg.to,"Tak akan ku sembunyikan")
                    sendMessage(msg.to,"Oogoe daiyamondo~")
                    sendMessage(msg.to,"Katakan dengan berani")
                    sendMessage(msg.to,"Jika kau diam kan tetap sama")
                    sendMessage(msg.to,"Janganlah kau merasa malu")
                    sendMessage(msg.to,"“Suka” itu kata paling hebat!")
                    sendMessage(msg.to,"“Suka” itu kata paling hebat!")
                    sendMessage(msg.to,"“Suka” itu kata paling hebat!")
                    sendMessage(msg.to,"Ungkapkan perasaanmu")
                    sendMessage(msg.to,"Jujurlah dari sekarang juga..")
                    sendMessage(msg.to,"SPAM IS DONE")
                    sendMessage(msg.to,"Created By : Anton")
                    sendMessage(msg.to,"Subscribe Line : http://line.me/ti/p/~antonlou")
#-------------------------------------------------------------			
                if msg.text == "Tagall":
		      group = client.getGroup(msg.to)
		      mem = [contact.mid for contact in group.members]
		      for mm in mem:
		       xname = client.getContact(mm).displayName
		       xlen = str(len(xname)+1)
		       msg.contentType = 0
                       msg.text = "@"+xname+" "
		       msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(mm)+'}]}','EMTVER':'4'}
		       try:
                         client.sendMessage(msg)
		       except Exception as error:
                   	 print error
#-------------------------------------------------------------		
        else:
            pass

    except Exception as e:
        print e
        print ("\n\nSEND_MESSAGE\n\n")
        return

tracer.addOpInterrupt(25,SEND_MESSAGE)

while True:
    tracer.execute()
