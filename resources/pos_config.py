# -*- coding: utf-8 -*-

from odoo import models

class PosConfigResources(models.Model):
    _inherit = 'pos.config'

    def BranchResource(self):
        return {
            'id': self.id,
            'nameEn': self.name,
            'nameAr': self.name,
            'phoneNumber': '',
            'address': '',
            'currency_id': self.currency_id.id,
            'company_id': self.company_id.id,
            'pricelist_id': self.pricelist_id.id,
            'session_id': self.current_session_id.id,
        } 