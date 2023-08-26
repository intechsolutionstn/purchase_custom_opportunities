from odoo import models, fields


class CustomSaleOrder(models.Model):
    _inherit = 'sale.order'
    
    opportunity_ids = fields.Many2many('crm.lead', string='Opportunities', compute='_compute_opportunities')

    def _compute_opportunities(self):
        for order in self:
            opportunities = self.env['crm.lead'].search([('partner_id', '=', order.partner_id.id)])
            order.opportunity_ids = opportunities
