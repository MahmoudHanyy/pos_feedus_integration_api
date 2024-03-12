# -*- coding: utf-8 -*-

from odoo import models

class PosOrderResources(models.Model):
    _inherit = 'pos.order'

    def OrderResource(self):
        return {
            'id': self.id,
            'name': self.name,
            'state': self.state,
            'partner_id': self.partner_id.name,
        } 