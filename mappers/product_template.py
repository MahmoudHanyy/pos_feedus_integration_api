# -*- coding: utf-8 -*-

from odoo import models

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    def feedus_map(self, source: dict) -> dict:
        qty = source.get('quantity', False)
        price_subtotal = qty * source.get('price', False)
        price_subtotal_incl = qty * source.get('price', False)
        product = self.browse(int(source.get('id', False)))      
        
        return {
            "product_id": product.product_variant_id.id,
            'full_product_name': product.product_variant_id.name,
            "qty": qty,
            "price_unit": source.get('price', False),
            "price_subtotal": price_subtotal,
            "price_subtotal_incl": price_subtotal_incl
            # "discount": ,
        }