#coding=utf-8
import requests
from padandunpad import padandunpad
from getEveryMsgREQ import getmsgcode
import json

class getisauthREQ():
    def getisauthREQ(self):
        aa = padandunpad()
        data = aa.padplusmsgcode()
        #msgcode=getmsgcode()
        #msgcode=msgcode.requestcode()
        #加密消息体实例
        # 1：{ "deviceId": "AD00006", "authString": "AD000061490682606","timeStamp": "1490682606"}
        # 2：{"authString": "AD000061490682606", "idCard": "230106199204111421","bussiness": "10","timeStamp": "1490682606"}
        paddata='{"deviceId":"AD00006","data":"' + data + '"}'
        headers = {'content-type': 'application/json'}
        r = requests.post("http://192.168.97.115:8080/socialFaceAuthAPP/getisauthREQ.do", data=paddata, headers=headers)
       # result = json.loads(r.text)
        #return result
        #打印结果
        print u"结果：\n%s" % (r.text)

code=getisauthREQ()
code.getisauthREQ()