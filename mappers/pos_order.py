# -*- coding: utf-8 -*-

from odoo import models

class PosOrder(models.Model):
    _inherit = 'pos.order'
    
    def feedus_map(self, source: dict) -> dict:
        PRODUCT = self.env['product.template'].sudo()
        partner_id = self.get_partner_by_name_feedus(source.get('customer', False)) 
        
        return {
            'session_id': self.set_default_session_id(),
            'partner_id': partner_id.id if partner_id else False,
            'feedus_order_id': source.get('feedus_order_id', False),
            'aggregator_order_id': source.get('aggregator_order_id', False),
            'aggregator': source.get('aggregator', False),
            'note': source.get('note', False),
            'date_order': source.get('orderDate', False),
            'amount_tax': source.get('taxTotal', False),
            'amount_total': source.get('grandTotal', False),
            'amount_paid': source.get('grandTotal', False),
            'amount_return': 0,
            'lines': [
                (0, 0, PRODUCT.feedus_map(item)) for item in source.get('items', False)
            ]
        }
             
    
    def get_partner_by_name_feedus(self, name):
        PARTNER = self.env['res.partner'].sudo()
        if not name: 
            return False
        partner_name = name.get('name', False)
        if not partner_name:
            return False
        
        return PARTNER.search([('name', '=ilike', partner_name)], limit=1)