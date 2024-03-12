# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

from ..utils.http_response import HttpResponse
from ..utils.jwt import Jwt, token_required

class CategoryController(http.Controller):

    @token_required
    @http.route('/api/http/get_available_categories', method=["POST"], type='json', auth='none')
    def index(self, **kwargs):
        # TODO: try except
        CATEGORY = request.env['product.category']
        categories = CATEGORY.search([])
        data = [c.CategoryResource() for c in categories]
        return HttpResponse.Success(
            data= data,
            message= "Available Categories"
        )