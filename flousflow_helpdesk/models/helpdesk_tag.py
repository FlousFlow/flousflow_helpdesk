from odoo import fields, models, _


class HelpdeskTag(models.Model):
    _name = 'flousflow.helpdesk.tag'
    _description = 'Helpdesk Tag'

    name = fields.Char(string=_('Name'), required=True, translate=True,
                       help=_('Name of the tag.'))
    color = fields.Integer(string=_('Color'),
                           help=_('Color index used to display the tag.'))
