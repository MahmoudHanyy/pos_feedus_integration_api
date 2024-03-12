# -*- coding: utf-8 -*-

from odoo import models, fields

class PosConfig(models.Model):
    _inherit = 'pos.config'
    
    is_default_config = fields.Boolean(string="Is Default?", default=False)

    def get_default_session(self):
        SESSION = self.env['pos.session'].sudo()
        CONFIG = self.env['pos.config'].sudo()
        
        config_id = CONFIG.search([
            ('is_default_config', '=', True)
        ], limit=1)

        session_id = SESSION.search([
            ('state','!=', 'closed'),('config_id','=', config_id.id),
        ], limit=1)

        return session_id or SESSION.create({
            'config_id': config_id.id,
        })