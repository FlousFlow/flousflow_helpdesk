from odoo import fields, models, _


class HelpdeskStage(models.Model):
    _name = 'flousflow.helpdesk.stage'
    _description = 'Helpdesk Stage'
    _order = 'sequence, id'

    name = fields.Char(string=_('Name'), required=True, translate=True)
    sequence = fields.Integer(string=_('Sequence'), default=10)
    fold = fields.Boolean(string=_('Folded in Kanban'))
    is_close = fields.Boolean(string=_('Closing Stage'))
    team_ids = fields.Many2many('flousflow.helpdesk.team', string=_('Teams'))
