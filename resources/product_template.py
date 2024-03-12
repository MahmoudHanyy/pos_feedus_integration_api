# -*- coding: utf-8 -*-

from odoo import models

class ProductTemplateResources(models.Model):
    _inherit = 'product.template'

    def ProductResource(self):
        CONFIG = self.env['ir.config_parameter'].sudo()
        BASE_URL = CONFIG.search([('key', '=', 'web.base.url')], limit=1).value
        return {
            'id': self.id,
            'nameAr': self.name,
            'nameEn': self.display_name,
            'description': self.description,        
            'category_ids': [self.categ_id.id],           
            'imageUrl': f'{BASE_URL}/web/image?model=product.template&id={self.id}&field=image_1024',
            'price': self.list_price,	
        } 