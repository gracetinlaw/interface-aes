#coding=utf-8
import requests
import json
# 调用Cipher加密方法
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

class padandunpad():
    def pad(text):
        BS=AES.block_size# 定义填充块的大小
    # 加密算法
        pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    # IV偏移量
        IV = b'0102030405060708'
     # 密钥必须为16或32
        key1 = b'0000000000123456'
    # 要加密的内容
        text = "{ 'deviceId': 'AD00006', 'authString': 'AD000061490682606','timeStamp': '1490682606'}"#raw_input("输入要加密的内容1:")
       # 加密消息体实例{ 'deviceId': 'AD00006', 'authString': 'AD000061490682606','timeStamp': '1490682606'}
     # 加密数据
        cipher = AES.new(key1, AES.MODE_CBC, IV=IV)
        data = b2a_hex(cipher.encrypt(pad(text)))
        return data
    def padplusmsgcode(text):
        from getEveryMsgREQ import getmsgcode
        msgcode = getmsgcode()
        msgcode = msgcode.requestcode()
        BS=AES.block_size# 定义填充块的大小
    # 加密算法
        pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
    # IV偏移量
        IV = b'0102030405060708'
     # 密钥必须为16或32
        key1 = b'00123456'+ msgcode + ''
    # 要加密的内容
        text = raw_input("输入要加密的内容2:")
       # 加密消息体实例{ 'deviceId': 'AD00006', 'authString': 'AD000061490682606','timeStamp': '1490682606'}
     # 加密数据
        cipher = AES.new(key1, AES.MODE_CBC, IV=IV)
        data = b2a_hex(cipher.encrypt(pad(text)))
        return data
    def unpad(self):
        BS = AES.block_size  # 定义填充块的大小
        pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
        # 解密算法
        unpad = lambda s: s[0:-ord(s[-1])]
        # IV偏移量
        IV = b'0102030405060708'
        # 密钥必须为16或32
        key1 = b'0000000000123456'
        # 要加密的内容
        text = raw_input("输入要解密的内容1:")
        # 加密消息体实例{ 'deviceId': 'AD00006', 'authString': 'AD000061490682606','timeStamp': '1490682606'}
        # 加密数据
        cipher = AES.new(key1, AES.MODE_CBC, IV=IV)
        encrypted = cipher.encrypt(pad(text)).encode('hex')
        data = unpad(cipher.decrypt(encrypted.decode('hex')))
        return data
        print data

#a=padandunpad()
#a.unpad()