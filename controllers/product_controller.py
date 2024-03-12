# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

from ..utils.http_response import HttpResponse
from ..utils.jwt import Jwt, token_required

class ProductController(http.Controller):

    @token_required
    @http.route('/api/http/get_available_menu', methods=["POST"], type='json', auth='user')
    def index(self, **kwargs):
        # TODO: try except
        PRODUCT = request.env['product.template'].sudo()
        available_products = PRODUCT.search([
            ('available_in_pos', '=', True)
        ])
        data = [d.ProductResource() for d in available_products]
        return HttpResponse.Success(
            data
        )