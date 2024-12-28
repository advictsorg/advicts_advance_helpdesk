# -*- coding: utf-8 -*-
# Part of Advicts LTD.

from odoo import models, fields


class HelpdeskSubjectType(models.Model):
    _name = 'helpdesk.sub.type'
    _description = 'Helpdesk Subject Type'
    _rec_name = 'name'

    name = fields.Char('Name', required=True,translate=True)
