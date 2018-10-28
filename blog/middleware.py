#!/usr/bin/env python
# encoding: utf-8


import time
from ipware.ip import get_real_ip
from zwhk_blog.utils import cache


class OnlineMiddleware(object):
    def __init__(self, get_response=None):
        self.get_response = get_response
        super().__init__()

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        http_user_agent = request.META.get('HTTP_USER_AGENT', [])
        if 'Spider' in http_user_agent or 'spider' in http_user_agent:
            return response
        cast_time = time.time() - start_time
        try:
            response.content = response.content.replace(b'<!!LOAD_TIMES!!>', str.encode(str(cast_time)[:5]))
            return response
        except:
            return response
