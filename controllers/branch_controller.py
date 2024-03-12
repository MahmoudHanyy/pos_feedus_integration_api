# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

from ..utils.http_response import HttpResponse
from ..utils.jwt import Jwt, token_required

class BranchController(http.Controller):

    @token_required
    @http.route('/api/http/get_available_branches', method=["POST"], type='json', auth='none')
    def index(self, **kwargs):
        # TODO: try except
        body = request.jsonrequest
        BRANCH = request.env['pos.config']
        branchs = BRANCH.search([])
        data = [d.BranchResource() for d in branchs]
        return HttpResponse.Success(
            data= data,
            message= "Available Branches"
        )