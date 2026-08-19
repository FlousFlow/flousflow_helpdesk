from odoo import http
from odoo.http import request


class HelpdeskTracking(http.Controller):

    @http.route('/helpdesk/track/<string:token>', type='http', auth='public')
    def track(self, token, **kw):
        ticket = request.env['flousflow.helpdesk.ticket'].sudo().search(
            [('access_token', '=', token)], limit=1)
        if not ticket:
            return request.not_found()
        repair = ticket.repair_id
        return request.render('flousflow_helpdesk.ticket_tracking_page', {
            'ticket': ticket,
            'repair': repair,
        })
