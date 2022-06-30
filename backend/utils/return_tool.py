# coding=utf8
#author Jack qq:774428957
import logging
from rest_framework.response import Response
logger = logging.getLogger('views')
'''
    返回值 定义规范
    code：返回值状态码：0成功，其他表示不成功，自己定义不成功的值
    errmsg:错误返回消息 成功里边为空，不成功请编写值
'''
class ReturnTool:
    @classmethod
    def getRet(self,code=0,detail='',data={}):
        ret={'code':0,'detail':detail,'data':data}
        if code!=0:
            ret={'code': code, 'detail': [detail]}
            logger.error(ret)
        else:
            logger.info(ret)
        return ret

class OPGResponse:
    def __init__(self,data):
        if isinstance(data, str):
            if code==0:
                return Response(data)
            else:
                return Response(data,status=500)
        elif type(data)=='dict':
            if 'code' in data:
                if data['code']<400:
                    return Response(data, status=200)
                else:
                    return Response(data, status=data['code'])
        else:
            return Response(data)