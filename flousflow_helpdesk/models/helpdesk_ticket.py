import uuid

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class HelpdeskTicket(models.Model):
    _name = 'flousflow.helpdesk.ticket'
    _description = 'Helpdesk Ticket'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'priority desc, id desc'
    _rec_name = 'name'
    _check_company_auto = True

    name = fields.Char(string=_('Subject'), required=True, tracking=True,
                       help=_('Short summary of the support request.'))
    description = fields.Html(string=_('Description'), tracking=True,
                              help=_('Detailed description of the issue reported by the customer.'))
    team_id = fields.Many2one(
        'flousflow.helpdesk.team', string=_('Team'), tracking=True,
        help=_('Team responsible for handling this ticket.'))
    stage_id = fields.Many2one(
        'flousflow.helpdesk.stage', string=_('Stage'), tracking=True,
        domain="['|', ('team_ids', 'in', team_id), ('team_ids', '=', False)]",
        group_expand='_read_group_stage_ids',
        help=_('Current stage of the ticket in its workflow.'))
    user_id = fields.Many2one(
        'res.users', string=_('Assigned To'), tracking=True,
        help=_('Internal user assigned to work on this ticket.'))
    partner_id = fields.Many2one(
        'res.partner', string=_('Customer'), tracking=True, index=True,
        help=_('Customer who reported this issue.'))
    priority = fields.Selection([
        ('0', _('Low')),
        ('1', _('Normal')),
        ('2', _('High')),
        ('3', _('Urgent')),
    ], string=_('Priority'), default='1', tracking=True,
        help=_('Urgency of the ticket. Urgent tickets appear first.'))
    tag_ids = fields.Many2many('flousflow.helpdesk.tag', string=_('Tags'),
                               help=_('Tags used to categorize this ticket.'))
    product_id = fields.Many2one(
        'product.product', string=_('Product to Repair'), tracking=True,
        help=_('Product that needs to be repaired.'))
    lot_id = fields.Many2one(
        'stock.lot', string=_('Lot/Serial'),
        domain="[('product_id', '=', product_id)]", tracking=True,
        help=_('Lot or serial number of the product to repair.'))
    repair_id = fields.Many2one(
        'repair.order', string=_('Repair Order'), readonly=True, tracking=True,
        help=_('Repair order linked to this ticket.'))
    state = fields.Selection([
        ('draft', _('New')),
        ('in_progress', _('In Progress')),
        ('done', _('Done')),
        ('cancelled', _('Cancelled')),
    ], string=_('Status'), default='draft', tracking=True,
        help=_('Current status of the ticket.'))
    company_id = fields.Many2one(
        'res.company', string=_('Company'),
        default=lambda self: self.env.company,
        help=_('Company this ticket belongs to.'))
    access_token = fields.Char(string=_('Tracking Token'), copy=False,
                               readonly=True, index=True,
                               default=lambda self: str(uuid.uuid4()),
                               help=_('Unique token used for the public tracking link.'))
    active = fields.Boolean(default=True,
                            help=_('Uncheck to archive this ticket.'))

    def _read_group_stage_ids(self, stages, domain):
        return self.env['flousflow.helpdesk.stage'].search([])

    def _get_state_display(self):
        self.ensure_one()
        return dict(self._fields['state'].selection).get(self.state, self.state)

    def _get_tracking_url(self):
        self.ensure_one()
        base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
        return f"{base_url}/helpdesk/track/{self.access_token}"

    def action_open_tracking(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'url': self._get_tracking_url(),
            'target': 'new',
        }

    def action_start(self):
        self.write({'state': 'in_progress'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_create_repair(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Create Repair Order'),
            'res_model': 'flousflow.helpdesk.create.repair.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {
                'default_ticket_id': self.id,
                'default_partner_id': self.partner_id.id,
                'default_product_id': self.product_id.id,
            },
        }

    def action_view_repair(self):
        self.ensure_one()
        if not self.repair_id:
            raise UserError(_('This ticket has no repair order yet.'))
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'repair.order',
            'view_mode': 'form',
            'res_id': self.repair_id.id,
            'target': 'current',
        }
