# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from ..utils.http_response import HttpResponse
from ..utils.jwt import Jwt, token_required

class OrderController(http.Controller):
    
    @token_required
    @http.route('/api/http/save_order', methods=["POST"], type='json', auth='none')
    def order_store(self, **kwargs):
        # TODO: try except
        ORDER = request.env['pos.order']
        body = ORDER.feedus_map(request.jsonrequest)
        body['session_id'] = ORDER.set_default_session_id()
        order = ORDER.create(body)
        if order.partner_id:
            order.make_payment()
            order.action_pos_order_invoice()
        
        return HttpResponse.Success(
            order.OrderResource()
        )
    
    @http.route('/api/http/update_order_status', methods=["POST"], type='json', auth='none')
    def order_update_status(self):
        # TODO: try except
        body = request.jsonrequest
        ORDER = request.env['pos.order'].sudo()
        order = ORDER.search([
            ('feedus_order_id', '=', body.get('order_id', False))
        ], limit=1)
        if not order.id:
            return HttpResponse.NotFound()
        return HttpResponse.Success()