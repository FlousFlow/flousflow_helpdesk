from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    helpdesk_ticket_ids = fields.One2many(
        'flousflow.helpdesk.ticket', 'partner_id',
        string=_('Maintenance Tickets'))
    maintenance_ticket_count = fields.Integer(
        string=_('Maintenance Tickets'),
        compute='_compute_maintenance', store=True)
    has_maintenance = fields.Boolean(
        string=_('Maintenance Customer'),
        compute='_compute_maintenance', store=True,
        help=_('Checked automatically when this customer has at least one '
               'maintenance ticket.'))

    @api.depends('helpdesk_ticket_ids')
    def _compute_maintenance(self):
        for partner in self:
            count = len(partner.helpdesk_ticket_ids)
            partner.maintenance_ticket_count = count
            partner.has_maintenance = count > 0
