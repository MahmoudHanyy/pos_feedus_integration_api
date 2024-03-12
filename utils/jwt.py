# -*- coding: utf-8 -*-
import jwt
from datetime import datetime, timedelta
from functools import wraps

from odoo.http import request
from .http_response import HttpResponse
from ..utils.utils import get_active_db

SECRET_KEY = 'MaitdiVfYPrbbGfkeLVJ'

class Jwt:
    
    @classmethod
    def generate_token(cls, payload):
        expiration_time = datetime.now() + timedelta(hours=12)
        token = jwt.encode(
            {'exp': expiration_time, **payload}, 
            SECRET_KEY, algorithm='HS256'
        )
        return token

    @classmethod
    def verify_token(cls, token):
        try:
            decoded_token = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            # if decoded_token['exp'] >= datetime.datetime.utcnow():
            return decoded_token
                
        except jwt.ExpiredSignatureError:
            return False
        
        except jwt.InvalidTokenError:
            return False
        
        
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        headers = request.httprequest.headers
        if 'Authorization' in headers:
            token = headers['Authorization'].split()[1]
        if not token:
            return HttpResponse.BadRequest()
        try:
            payload = Jwt.verify_token(token)
            if not payload:
                return HttpResponse.NotAuthorized()
            else:
                request.session.authenticate(
                    get_active_db(request), 
                    payload.get('username', False), 
                    payload.get('password', False)
                )
        except:
            return HttpResponse.BadRequest()
        
        return f(*args, **kwargs)
    return decorator