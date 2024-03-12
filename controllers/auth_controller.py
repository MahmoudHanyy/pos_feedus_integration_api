# -*- coding: utf-8 -*-
import re

from odoo import http
from odoo.http import request
from ..utils.http_response import HttpResponse
from ..utils.utils import get_active_db
from ..utils.jwt import Jwt

class AuthController(http.Controller):
    
    @http.route('/api/http/login', methods=['POST'], type='json', auth="none")
    def feedus_authenticate(self, **kwargs):
        body = request.jsonrequest
        db = get_active_db(request)
        login = body.get('username', False)
        password = body.get('password', False)
        
        if not all([db, login, password]):
            return HttpResponse.BadRequest()
        
        request.session.authenticate(db, login, password)
        user = request.env.user
        
        token = Jwt.generate_token({
            'id': user.id, 
            'username': login, 
            'password': password
        })
        
        return HttpResponse.Success(
            data=user.UserResource(token=token), 
            message="Successful Login"
        )