# -*- coding: utf-8 -*-
# Part of Advicts LTD.

from odoo import models, fields


class HelpdeskStagesNext(models.Model):
    _name = 'helpdesk.stages.next'
    stage_id = fields.Many2one('helpdesk.stages')
    ticket_type = fields.Many2one('sh.helpdesk.ticket.type', 'Ticket Type',required=True)
    sh_next_stage = fields.Many2one(
        comodel_name='helpdesk.stages',
        string='Next Stage',required=True
    )


class HelpdeskStages(models.Model):
    _name = 'helpdesk.stages'
    _description = "Helpdesk Stages"
    _order = 'sequence ASC'
    _rec_name = 'name'

    name = fields.Char("Name", required=True, translate=True)
    mail_template_ids = fields.Many2many(
        'mail.template', string='Mail Template')
    sh_next_stage = fields.Many2one(
        comodel_name='helpdesk.stages',
        string='Next Stage',
    )
    sh_next_stage_ids = fields.One2many(
        'helpdesk.stages.next', 'stage_id', 'Next Stages'
    )

    sh_group_ids = fields.Many2many(
        comodel_name='res.groups',
        string='Groups'
    )
    is_cancel_button_visible = fields.Boolean(
        string='Is Cancel Button Visible ?'
    )
    is_done_button_visible = fields.Boolean(
        string='Is Resolved Button Visible ?'
    )
    sequence = fields.Integer(string="Sequence")
