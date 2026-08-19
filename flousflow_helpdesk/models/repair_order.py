from odoo import fields, models, _
from odoo.exceptions import UserError


class RepairOrder(models.Model):
    _inherit = 'repair.order'

    helpdesk_ticket_id = fields.Many2one(
        'flousflow.helpdesk.ticket', string=_('Helpdesk Ticket'),
        readonly=True, tracking=True)

    def _get_state_display(self):
        self.ensure_one()
        return dict(self._fields['state'].selection).get(self.state, self.state)

    def action_view_ticket(self):
        self.ensure_one()
        if not self.helpdesk_ticket_id:
            raise UserError(_('This repair order is not linked to a ticket.'))
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'flousflow.helpdesk.ticket',
            'view_mode': 'form',
            'res_id': self.helpdesk_ticket_id.id,
            'target': 'current',
        }
