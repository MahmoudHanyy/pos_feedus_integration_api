# -*- coding: utf-8 -*-

from odoo import models

class UserResources(models.Model):
    _inherit = 'res.users'

    def UserResource(self, **kwargs):
        return {
            'token': kwargs.get('token', False),
            'branch_id': False
        } 