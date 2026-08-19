from odoo import fields, models, _


class HelpdeskTeam(models.Model):
    _name = 'flousflow.helpdesk.team'
    _description = 'Helpdesk Team'
    _check_company_auto = True

    name = fields.Char(string=_('Name'), required=True, translate=True,
                       help=_('Name of the team.'))
    user_ids = fields.Many2many('res.users', string=_('Team Members'),
                                help=_('Members of this team. They can be assigned to its tickets.'))
    stage_ids = fields.Many2many('flousflow.helpdesk.stage', string=_('Stages'),
                                 help=_('Stages available to this team\'s tickets.'))
    company_id = fields.Many2one(
        'res.company', string=_('Company'),
        default=lambda self: self.env.company,
        help=_('Company this team belongs to.'))
    active = fields.Boolean(default=True,
                            help=_('Uncheck to archive this team.'))
