# -*- coding: utf-8 -*-

from odoo import models

class CategoryResources(models.Model):
    _inherit = 'product.category'

    def CategoryResource(self, **kwargs):
        return {
            'id': self.id,
            'nameAr': self.name,
            'nameEn': self.name
        } 