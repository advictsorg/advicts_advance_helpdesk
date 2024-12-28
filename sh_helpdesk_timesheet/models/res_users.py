# -*- coding: utf-8 -*-
# Part of Advicts LTD.

from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'

    sh_running_ticket_id = fields.Many2one('sh.helpdesk.ticket','Running Ticket Id')
