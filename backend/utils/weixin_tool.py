# coding=utf-8
#author Jack qq:774428957
import json
import requests
class Weixin(object):

    def __init__(self, weixin_config):
        self.corpid = weixin_config.get('WEIXIN_CORPID')
        self.secrect= weixin_config.get('WEIXIN_SECRET')
        self.agentid= weixin_config.get('WEIXIN_AGTID')
        self.access_token = self.get_access_token()

    def get_access_token(self):
        access_token_url="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}".format(self.corpid,self.secrect)
        ret = requests.get(access_token_url).json()
        return ret["access_token"]

    def send_msg(self, arrMsg):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=%s' % (self.access_token)
        return requests.post(url, data=arrMsg).json()

    def send_text(self,sToUser,sText):
        postdata = {
            "touser": sToUser,
            "msgtype": "text",
            "agentid": self.agentid,
            "text": {
                "content": sText
            },
            "safe":0
        }
        return self.send_msg(json.dumps(postdata))

    def departments(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token=%s' % (self.access_token)
        return requests.get(url).json()

    def users(self, department_id):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/user/list?access_token={}&department_id={}&fetch_child=1&status=0'.format(
        self.access_token, department_id)
        return requests.get(url).json()


if __name__ == '__main__':
    weixin_config = {
        'WEIXIN_CORPID': '',
        'WEIXIN_SECRET': '',
        'WEIXIN_AGTID': '1000006',
    }
    weixin = Weixin(weixin_config)
    ret = weixin.send_text('cccc', 'xxsdfsdfasfdasdf')
    print(ret)
