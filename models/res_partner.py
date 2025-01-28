# -*- coding: utf-8 -*-
# Part of Advicts LTD.

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    is_internal_partner = fields.Boolean('Is Internal Ticket Partner')


