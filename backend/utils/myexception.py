# -*- coding: utf-8 -*-
#author Jack qq:774428957
import logging

logger = logging.getLogger('views')


class MyException(Exception):
    def __init__(self, code, errmsg):
        self.code = code
        self.errmsg = errmsg

    def getRet(self):
        return {'code': self.code, 'msg': self.errmsg}

    def __str__(self):
        return self.errmsg
