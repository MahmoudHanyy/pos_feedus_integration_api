# -*- coding: utf-8 -*-

from odoo import models, fields

class PosOrder(models.Model):
    _inherit = 'pos.order'

    feedus_order_id = fields.Char()
    aggregator_order_id = fields.Char()
    aggregator = fields.Char()
    
    def set_default_session_id(self):
        CONFIG = self.env['pos.config'].sudo()
        session_id = CONFIG.get_default_session()
        return session_id.id

    def make_payment(self):
        PAYMENT = self.env['pos.make.payment'].sudo()
        session_id = self.session_id
        payment_method = session_id.payment_method_ids[0] if len(session_id.payment_method_ids) else False
        # TODO:handle empty method
        payment = PAYMENT.create({
            'config_id': self.session_id.config_id.id,
            'amount': self.amount_paid,
            'payment_method_id': payment_method.id
        })
        payment.with_context({'active_id': self.id}).check()