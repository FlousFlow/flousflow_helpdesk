from odoo import fields, models, _


class HelpdeskTag(models.Model):
    _name = 'flousflow.helpdesk.tag'
    _description = 'Helpdesk Tag'

    name = fields.Char(string=_('Name'), required=True, translate=True)
    color = fields.Integer(string=_('Color'))
