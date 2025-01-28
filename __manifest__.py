# -*- coding: utf-8 -*-
# Part of Advicts LTD.
{
    "name": "Advicts Advance Helpdesk",
    "author": "Advicts LTD",
    "website": "https://www.advicts.com",
    "category": "Discuss",
    "license": "OPL-1",
    "summary": "Customizable Helpdesk to Make it Professional",
    "description": """Customizable Helpdesk to Make it Professional """,
    "version": "0.0.1",
    "depends": ["mail", "portal", "product", 'website', "resource", "sale_management", "purchase", "account",
                "hr_timesheet",
                "crm", "project", 'web_editor'],
    "data": [
        "security/sh_helpdesk_security.xml",
        "security/ir.model.access.csv",

        "data/sh_helpdesk_email_data.xml",
        "data/sh_helpdesk_data.xml",
        "data/sh_helpdesk_cron_data.xml",
        "data/sh_helpdesk_stage_data.xml",

        "views/sh_helpdesk_menu.xml",
        "views/sh_helpdesk_sla_policies.xml",
        "views/sh_helpdesk_alarm.xml",

        "data/sh_helpdesk_reminder_cron.xml",
        "data/sh_helpdesk_reminder_mail_template.xml",

        "views/sh_helpdesk_team_view.xml",
        "views/sh_helpdesk_ticket_type_view.xml",
        "views/sh_helpdesk_subject_type_view.xml",
        "views/sh_helpdesk_tags_view.xml",
        "views/sh_helpdesk_stages_view.xml",
        "views/sh_helpdesk_category_view.xml",
        "views/sh_helpdesk_subcategory_view.xml",
        "views/sh_helpdesk_priority_view.xml",
        "views/sh_helpdesk_config_settings_view.xml",
        "views/sh_helpdesk_ticket_view.xml",
        "views/sh_report_helpdesk_ticket_template.xml",
        "views/sh_helpdeks_report_portal.xml",
        "views/action_report_views.xml",
        "views/sh_ticket_feedback_template.xml",
        # "views/sh_ticket_dashboard_templates.xml",
        "views/res_users.xml",
        "views/res_partner.xml",
        "views/sh_helpdesk_merge_ticket_action.xml",
        "views/sh_helpdesk_ticket_multi_action_view.xml",
        "views/sh_helpdesk_ticket_update_wizard_view.xml",
        "views/sh_helpdesk_ticket_portal_template.xml",
        "views/sh_helpdesk_ticket_megre_wizard_view.xml",
        "views/sh_helpdesk_ticket_task_info.xml",

        "wizard/mail_compose_view.xml",

        "sh_helpdesk_so/security/sh_helpdesk_so_security.xml",
        "sh_helpdesk_so/views/sh_helpdesk_so_tickets.xml",

        "sh_helpdesk_po/security/sh_helpdesk_po_security.xml",
        "sh_helpdesk_po/views/sh_helpdesk_po_tickets.xml",

        "sh_helpdesk_invoice/security/sh_helpdesk_invoice_security.xml",
        "sh_helpdesk_invoice/views/sh_helpdesk_invoice_tickets.xml",

        "sh_helpdesk_timesheet/security/helpdesk_timesheet_security.xml",
        "sh_helpdesk_timesheet/security/ir.model.access.csv",
        "sh_helpdesk_timesheet/views/res_config_setting.xml",
        "sh_helpdesk_timesheet/views/hr_timesheet.xml",
        "sh_helpdesk_timesheet/views/sh_helpdesk_ticket.xml",

        "sh_helpdesk_crm/security/sh_helpdesk_crm_security.xml",
        "sh_helpdesk_crm/views/sh_helpdesk_crm_tickets.xml",

        'sh_helpdesk_task/security/helpdesk_task_security.xml',
        'sh_helpdesk_task/views/sh_helpdesk_ticket.xml',
        'sh_helpdesk_task/views/task.xml',
    ],
    'assets': {
        # 'web.assets_backend': [
        #     'advicts_advance_helpdesk/static/src/js/time_track.js',
        #     'advicts_advance_helpdesk/static/src/xml/TaskTimeCounter.xml',
        #     'advicts_advance_helpdesk/sh_helpdesk_timesheet/static/src/scss/time_track.scss',
        #     'advicts_advance_helpdesk/static/src/js/helpdesk_ticket_kanban_examples.js',
        #     'advicts_advance_helpdesk/static/src/js/ticket_dashboard.js',
        #     'advicts_advance_helpdesk/static/src/css/ticket_dashboard.css',
        #     'advicts_advance_helpdesk/static/src/xml/**/*',
        # ],
        'web.assets_backend': [
            'advicts_advance_helpdesk/static/src/js/bus_notifications.js',
            'advicts_advance_helpdesk/static/src/js/time_track.js',
            'advicts_advance_helpdesk/static/src/xml/TaskTimeCounter.xml',

            'advicts_advance_helpdesk/static/src/xml/ticket_main_dashboard_view.xml',
            'advicts_advance_helpdesk/static/src/xml/ticket_dashboard_card_view.xml',
            'advicts_advance_helpdesk/static/src/xml/ticket_dashboard_tables_dashboard.xml',
            'advicts_advance_helpdesk/static/src/js/dashboard_components/ticket_cards_dashboard.js',
            'advicts_advance_helpdesk/static/src/js/dashboard_components/ticket_dashboard_tables_dashboard.js',
            'advicts_advance_helpdesk/static/src/js/dashboard_components/ticket_main_dashboard.js',
            # 'advicts_advance_helpdesk/static/src/xml/ticket_main_dashboard_view.xml',
            # 'advicts_advance_helpdesk/static/src/xml/ticket_dashboard_card_view.xml',
            # 'advicts_advance_helpdesk/static/src/xml/ticket_dashboard_table_view.xml',
            # 'advicts_advance_helpdesk/static/src/js/dashboard_components/ticket_cards_dashboard.js',
            # 'advicts_advance_helpdesk/static/src/js/dashboard_components/ticket_main_dashboard.js',            
            # 'advicts_advance_helpdesk/static/src/js/dashboard_components/ticket_table_dashboard.js',            
            'advicts_advance_helpdesk/static/src/css/ticket_dashboard.css',
        ],
        'web.assets_frontend': [
            'advicts_advance_helpdesk/static/src/js/portal.js',
            # 'advicts_advance_helpdesk/static/src/js/description.js',
            # 'advicts_advance_helpdesk/static/src/css/bootstrap-multiselect.min.css',
            # 'advicts_advance_helpdesk/static/src/js/bootstrap-multiselect.min.js',
            'advicts_advance_helpdesk/static/src/css/feedback.scss',
            'advicts_advance_helpdesk/static/src/js/file_upload_widget.js',
            # 'advicts_advance_helpdesk/static/src/xml/file_upload_widget.xml',
            'advicts_advance_helpdesk/static/src/css/feedback.scss'
        ],
    },
    "application":
        True,
    "auto_install":
        False,
    "installable":
        True,
}
