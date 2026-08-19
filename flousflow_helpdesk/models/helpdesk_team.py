from odoo import fields, models, _


class HelpdeskTeam(models.Model):
    _name = 'flousflow.helpdesk.team'
    _description = 'Helpdesk Team'
    _check_company_auto = True

    name = fields.Char(string=_('Name'), required=True, translate=True)
    user_ids = fields.Many2many('res.users', string=_('Team Members'))
    stage_ids = fields.Many2many('flousflow.helpdesk.stage', string=_('Stages'))
    company_id = fields.Many2one(
        'res.company', string=_('Company'),
        default=lambda self: self.env.company)
    active = fields.Boolean(default=True)
