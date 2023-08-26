
from odoo import api, fields, models


class Expense(models.Model):
    _inherit = "hr.expense"

    opportunity_ids = fields.Many2one('crm.lead', string='Opportunities')

    def _compute_opportunities(self):
        for order in self:
            opportunities = self.env['crm.lead'].search([('partner_id', '=', order.partner_id.id)])
            order.opportunity_ids = opportunities
