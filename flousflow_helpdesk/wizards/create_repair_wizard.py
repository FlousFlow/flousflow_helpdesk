from odoo import fields, models, _


class HelpdeskCreateRepairWizard(models.TransientModel):
    _name = 'flousflow.helpdesk.create.repair.wizard'
    _description = 'Create Repair Order Wizard'

    ticket_id = fields.Many2one(
        'flousflow.helpdesk.ticket', string=_('Ticket'), required=True,
        help=_('Ticket this repair order is created from.'))
    partner_id = fields.Many2one(
        'res.partner', string=_('Customer'), required=True,
        help=_('Customer for the repair order.'))
    product_id = fields.Many2one(
        'product.product', string=_('Product to Repair'), required=True,
        domain="[('type', 'in', ['consu', 'product'])]",
        help=_('Product to repair.'))

    def action_create_repair(self):
        self.ensure_one()
        repair = self.env['repair.order'].create({
            'partner_id': self.partner_id.id,
            'product_id': self.product_id.id,
            'helpdesk_ticket_id': self.ticket_id.id,
        })
        self.ticket_id.repair_id = repair.id
        return {
            'type': 'ir.actions.act_window',
            'name': _('Repair Order'),
            'res_model': 'repair.order',
            'view_mode': 'form',
            'res_id': repair.id,
            'target': 'current',
        }
