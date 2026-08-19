from odoo import fields, models, _


class HelpdeskStage(models.Model):
    _name = 'flousflow.helpdesk.stage'
    _description = 'Helpdesk Stage'
    _order = 'sequence, id'

    name = fields.Char(string=_('Name'), required=True, translate=True,
                       help=_('Name of the stage.'))
    sequence = fields.Integer(string=_('Sequence'), default=10,
                              help=_('Order of the stage in the kanban view.'))
    fold = fields.Boolean(string=_('Folded in Kanban'),
                          help=_('Fold this stage by default in the kanban view.'))
    is_close = fields.Boolean(string=_('Closing Stage'),
                              help=_('Tickets in this stage are considered as closed.'))
    team_ids = fields.Many2many('flousflow.helpdesk.team', string=_('Teams'),
                                help=_('Teams that use this stage. Leave empty to make it available to all teams.'))
