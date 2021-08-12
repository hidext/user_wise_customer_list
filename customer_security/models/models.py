# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PartnerInherit(models.Model):
    _inherit = 'res.partner'

    # user_id = fields.Many2one(comodel_name="res.partner", string="Salesperson	", required=False, default=lambda self: self.env.user)
    user_id = fields.Many2one('res.users', 'Internal User' 'Salesperson',      default=lambda self: self.env.uid)
