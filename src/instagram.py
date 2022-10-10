
from re import U
import requests
import json
import pprint

class Instagram(object):
    config = {
        "access_token":str,
        "app_id":str,
        "app_secret":str,
        "instagram_account_id":str,
        "version":str,
        "graph_endpoint":'https://graph.facebook.com/',
        "endpoint_base":str,
    }
    response = {
        "url":str,
        "endpoint_params":str,
        "endpoint_params_pretty":str,
        "json_data":str,
        "json_data_pretty":str,
    }

    def __init__(self):
        self.config["access_token"] = "EAAVFcxH7SGABAGOZBvVIgCCuX71DUEPTjceUQrG3IX6dH1AHVHhskI7ZCUQ2ppJAznm8QRNVSo9Sq26F4IKIc7mdsQnQhcGsXZC3fPb8fZAPyUMXNyi4A59wQzNU8yfKKuR3NVTb0MVD3zig8uQoEZAPaARJhUNvr7gvWPNya8AZDZD"
        self.config["app_id"] = "1483735408789600"
        self.config["app_secret"] = "a8ec55fd29d67a3001ac63f16e1da6d5"
        self.config["instagram_account_id"] = "17841400562034171"
        self.config["version"] = "v15.0"
        self.config["graph_endpoint"] = "https://graph.facebook.com/"
        self.config["endpoint_base"] = self.config["graph_endpoint"] + self.config["version"] + '/'

        return

    def ApiCall(self,url,params,methods):
        if methods == "POST":
            req = requests.post(url,params)
        else:
            req = requests.get(url,params)
            
        
        
        self.response["url"] = url
        self.response["endpoint_params"] = params
        self.response["endpoint_params_pretty"] = json.dumps(params,indent=4)
        self.response["json_data"] = json.loads(req.content)
        self.response["json_data_pretty"] = json.dumps(self.response["json_data"],indent=4)
        # カルーセルの場合の画像URL取得
        # self.response["json_data"]['business_discovery']['media']['data'][0]['children']['data']

        return self.response
    def GetUserMediaStatus(self,ig_user_name):
        params = dict()
        params["user_id"] = self.config["instagram_account_id"]
        params["access_token"] = self.config["access_token"]
        params["fields"] = 'business_discovery.username(' + ig_user_name + '){followers_count,media_count,media{timestamp,caption,media_type,media_url,children{media_type,media_url}}}'

        url = self.config["endpoint_base"] + params['user_id']
        
        return self.ApiCall(url, params,'GET')

    def getHashTag_ID(self,hashtag_keyword:str):
        params = dict()
        params["user_id"] = self.config["instagram_account_id"]
        params["hashtag_name"] = hashtag_keyword
        params["q"] = params["hashtag_name"]
        params["fields"] = 'id,name'
        params["access_token"] = self.config["access_token"]
        
        url = self.config["endpoint_base"] + 'ig_hashtag_search'
        res = self.ApiCall(url=url, params=params,methods="GET")
        return res['json_data']['data'][0]['id']
    
    def getHashtagMedia(self,hashtag_id:str):
        params = dict()
        params["user_id"] = self.config["instagram_account_id"]
        params["access_token"] = self.config["access_token"]
        params["fields"] = "id,children{media_url},caption"
        
        url = self.config["endpoint_base"] + hashtag_id + '/' + 'top_media'
        
        return self.ApiCall(url, params,methods="GET")
    
    def GetHashTagMain(self,keyword:str):
        """
        *************************************************
        キーワードの情報のタイトル、画像URLを取得
        *************************************************
        """
        hashtag_id = self.getHashTag_ID(keyword)
        hashtag = self.getHashtagMedia(hashtag_id)
        captionList = []
        mediaUrls = []
        mediaList = []
        for post in hashtag['json_data']['data']:
            mediaUrl = []
            mediaDic = dict()
            # print("[タイトル] : " + post['caption'])
            # captionList.append(post['caption'])
            try:
                # print(post['children']['data'])
                # mediaUrl.append(post['children']['data'])
                for media_url in post['children']['data']:
                    mediaUrl.append(media_url["media_url"])
                    # print(media_url["media_url"])
            except:
                pass
            mediaDic["id"] = post['id']
            mediaDic["caption"] = post['caption']
            mediaDic["mediaUrls"]= mediaUrl
            # mediaUrls.append(mediaUrl)
            mediaList.append(mediaDic)
        # print(captionList)
        # print("\n================================")
        # print(mediaUrls)
        # print(len(mediaUrls))
        # print(mediaList)
        print(mediaList[0]["mediaUrls"][0])
        print("\n================================")
        return mediaList