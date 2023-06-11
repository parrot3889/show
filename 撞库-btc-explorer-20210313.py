import bitcoin
import random
import threading, time, datetime
import json
import urllib
import datetime
import time
import requests
import blockcypher
import base58
import hashlib
import ecdsa
import bitcoinaddress
from bitcoinaddress.util import *
from moneywagon import AddressBalance

#############1分钟30个地址，超时2-3次，光库连不了################
counts = 1000000000
bal = 0
bal1 = 0
bal2 = 0
error=0

while counts > 0:
    private_key =bitcoin.random_key()
    wallet=bitcoinaddress.Wallet(private_key)
    #非压缩地址余额
    try:
        addr=wallet.address.__dict__['mainnet'].pubaddr1
        #addr="1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ"    ###测试用，有余额的地址
    except:
        print("地址错误")
        time.sleep(0.5)
    flag=0
    returnString=""
    api="https://explorer.spectrocoin.com/api/addr/"
    try:
        #bal=requests.get(api+ str(addr),timeout=10)
        bal=((requests.get(api+ str(addr),timeout=10)).json()['balance']) 
    except:
        error=error+1
        #print('地址gain all Error')
    if(bal>0 or float(bal)>0):
        bal=str(float(bal))
        print('私钥：'+private_key+'：压缩私钥wif：'+wallet.key.__dict__['mainnet'].wif+'：压缩私钥wifc：'+wallet.key.__dict__['mainnet'].wifc+'：非压缩地址：'+addr+'：余额： '+ bal)
        with open("F:\VALUEICO.txt",'a') as f:
            f.write('私钥：'+private_key+'：压缩私钥wif：'+wallet.key.__dict__['mainnet'].wif+'：压缩私钥wifc：'+wallet.key.__dict__['mainnet'].wifc+'：非压缩地址：'+addr+'：余额： '+ bal)
            f.write('\n')
        time.sleep(0.5)
    else:
        time.sleep(0.5)
    ########addr1=addr1.encode('utf-8')
    ###############################生成压缩地址###############################
    try:
        addr1=wallet.address.__dict__['mainnet'].pubaddr1c
        #addr1="1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ"    ###测试用，有余额的地址
    except:
        print("压缩地址错误")
        time.sleep(0.5)
    ###############################压缩地址余额###############################
    try:
        #bal1=requests.get(api+ str(addr1),timeout=10)
        bal1=((requests.get(api+ str(addr1),timeout=10)).json()['balance']) 
    except:
        error=error+1
        #print('压缩gain all Error')
    if(bal1>0 or float(bal1)>0):
        bal1=str(float(bal1))
        print('私钥：'+private_key+'：压缩私钥wif：'+wallet.key.__dict__['mainnet'].wif+'：压缩私钥wifc：'+wallet.key.__dict__['mainnet'].wifc+'：压缩地址：'+addr1+'：余额： '+ bal1)
        with open("F:\VALUEICO.txt",'a') as f:
            f.write('私钥：'+private_key+'：压缩私钥wif：'+wallet.key.__dict__['mainnet'].wif+'：压缩私钥wifc：'+wallet.key.__dict__['mainnet'].wifc+'：压缩地址：'+addr1+'：余额： '+ bal1)
            f.write('\n')
        time.sleep(0.5)
    else:
        time.sleep(0.5)
    ###############################生成隔离见证地址###############################
    try:
        addr2=wallet.address.__dict__['mainnet'].pubaddr3
        #addr2="1P5ZEDWTKTFGxQjZphgWPQUpe554WKDfHQ"    ###测试用，有余额的地址
    except:
        print("隔离见证地址错误")
        time.sleep(0.5)
      ###############################隔离见证地址余额###############################
    try:
        #bal2=requests.get(api+ str(addr2),timeout=10)
        bal2=((requests.get(api+ str(addr2),timeout=10)).json()['balance']) 
    except:
        error=error+1
        #print('隔离地址gain all Error')
    if(bal2>0 or float(bal2)>0):
        bal2=str(float(bal2))
        print('私钥：'+private_key+'：压缩私钥wif：'+wallet.key.__dict__['mainnet'].wif+'：压缩私钥wifc：'+wallet.key.__dict__['mainnet'].wifc+'：隔离地址：'+addr2+'：余额： '+ bal2)
        with open("F:\VALUEICO.txt",'a') as f:
            f.write('私钥：'+private_key+'：压缩私钥wif：'+wallet.key.__dict__['mainnet'].wif+'：压缩私钥wifc：'+wallet.key.__dict__['mainnet'].wifc+'：隔离地址：'+addr2+'：余额： '+ bal2)
            f.write('\n')
        time.sleep(0.5)
    else:
        time.sleep(0.5)
    if counts % 1000 == 0:
        countnum='%d'%counts
        error1='%d'%error
        print('记录：'+countnum+'：时间：'+time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime())+'：余额错误次数：'+error1)
        error=0
        #print(time.strftime("%Y-%m-%d-%H:%M:%S", time.localtime()))
    counts = counts - 1
    
print("结束！")


