# -*- coding: utf-8 -*-
{
    'name': 'Helpdesk (Flous Flow)',
    'version': '19.0.1.0.0',
    'category': 'Services/Helpdesk',
    'summary': 'Manage support tickets and link them to repair orders',
    'description': """
Flous Flow Helpdesk
===================
Manage customer support tickets with teams, stages and tags.

When a ticket needs a physical repair, create a repair order directly
from the ticket. The standard ``repair`` module is installed
automatically as a dependency of this module, and every repair order
keeps a link back to its helpdesk ticket.

Features:
---------
* Helpdesk tickets with teams, stages, tags and priorities
* Kanban view grouped by stage
* Create a repair order from a ticket (linked both ways)
* Chatter and activities on tickets
""",
    'depends': ['base', 'mail', 'product', 'stock', 'repair'],
    'images': [
        'static/description/icon.png',
        'static/description/banner.png',
        'static/description/screenshot_kanban.png',
        'static/description/screenshot_ticket.png',
    ],
    'data': [
        'security/helpdesk_security.xml',
        'security/ir.model.access.csv',
        'views/helpdesk_tag_views.xml',
        'views/helpdesk_stage_views.xml',
        'views/helpdesk_team_views.xml',
        'views/helpdesk_ticket_views.xml',
        'views/repair_order_views.xml',
        'wizards/create_repair_wizard_views.xml',
        'views/helpdesk_menu.xml',
        'reports/ticket_report.xml',
        'reports/ticket_templates.xml',
        'views/tracking_templates.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
    'author': 'Flous Flow',
    'website': 'https://flousflow.com',
}
