# BiliBiliHelper Python Version
# Copy right (c) 2019 TheWanderingCoel
# 该代码实现了登陆验证功能
# 代码根据metowolf大佬的PHP版本进行改写
# PHP代码地址:https://github.com/metowolf/BilibiliHelper/blob/0.9x/src/plugins/Auth.php

import json
import time
import base64
import requests
import platform
if platform.system() == "Windows":
    from Windows_Log import Log
else:
    from Unix_Log import Log
from Curl import Curl
from config import config
from Base import openssl_public_encrypt,arrange_cookie,set_cookie

class Auth():

    def __init__(self):
        self.lock = int(time.time())
    
    def work(self):
        if self.lock > int(time.time()):
            return
        
        if config["Token"]["ACCESS_TOKEN"] == "":
            self.loginPassword()
        else:
            self.loginToken()
        
        self.checkCookie()

        self.lock = int(time.time()) +3600

    def loginPassword(self):
        data = self.getPublicKey()

        user = config["Account"]["BILIBILI_USER"]
        password = config["Account"]["BILIBILI_PASSWORD"]
        key = data["data"]["key"]
        hash_ = data["data"]["hash"]
        crypt = openssl_public_encrypt(hash_+password,key)

        self.getToken(user,base64.b64encode(crypt))

    def loginToken(self):
        if self.checkToken() == False:
            Log.warning("检测到令牌即将过期")
            Log.info("申请更换令牌")
            if self.refresh() == False:
                Log.warning("更换令牌失败")
                Log.info("使用账号密码方式登陆")
                self.loginPassword()

    def checkCookie(self):
        url = "https://api.live.bilibili.com/User/getUserInfo"
        payload ={
            "ts":int(time.time())
        }
        data = Curl().request_json("GET",url,headers=config["pcheaders"],params=payload)

        if data["code"] != "REPONSE_OK":
            Log.error("检测到 Cookie 过期")
            Log.info("正在重新登陆")
            self.loginPassword()

    def checkToken(self):
        url = "https://passport.bilibili.com/api/v2/oauth2/info"
        payload = {
            "access_token":config["Token"]["ACCESS_TOKEN"]
        }
        data = Curl().request_json("GET",url,headers=config["pcheaders"],params=payload)

        if data["code"] == 0:
            Log.info("令牌验证成功，有效期:"+time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(data["ts"]+data["data"]["expires_in"])))
        else:
            Log.error("令牌验证失败")
            return False

        return data["data"]["expires_in"] > 14400

    def refresh(self):
        url = "https://passport.bilibili.com/api/oauth2/refreshToken"
        payload = {
            "access_token":config["Token"]["ACCESS_TOKEN"],
            "refresh_token":config["Token"]["REFRESH_TOKEN"],
            }
        data = Curl().request_json("POST",url,headers=config["pcheaders"],data=payload)

        if data["code"] == 0:
            Log.info("续签令牌成功")
        else:
            Log.error("续签令牌失败"+"-"+data["message"])
            return False

        return True

    def getPublicKey(self):
        url = "https://passport.bilibili.com/api/oauth2/getKey"
        payload = {}
        data = Curl().request_json("POST",url,headers=config["pcheaders"],data=payload)

        if data["code"] == 0:
            Log.info("公钥获取成功")
        else:
            Log.error("公钥获取失败"+"-"+data["message"])
        return data

    def getToken(self,username,password):
        url = "https://passport.bilibili.com/api/v3/oauth2/login"
        payload = {
            "seccode":"",
            "validate":"",
            "subid":1,
            "permission":"ALL",
            "username":username,
            "password":password,
            "captcha":"",
            "challenge":"",
            "cookies":config["Token"]["COOKIE"]
        }

        data = Curl().request_json("POST",url,headers=config["pcheaders"],data=payload)

        if data["code"] == 0:
            Log.info("账号登陆成功")
        else:
            Log.error("账号登陆失败"+"-"+data["message"])
    
        config["Token"]["ACCESS_TOKEN"] = data["data"]["token_info"]["access_token"]
        config["Token"]["REFRESH_TOKEN"] = data["data"]["token_info"]["refresh_token"]

        csrf,uid,cookie = arrange_cookie(data)
        config["Token"]["CSRF"] = csrf
        config["Token"]["UID"] = uid

        set_cookie(cookie)

        config.write()