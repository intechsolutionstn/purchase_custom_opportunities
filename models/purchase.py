from odoo import models, fields, api


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    opportunity_ids = fields.Many2one('crm.lead', string='Opportunities')

    def _compute_opportunities(self):
        for order in self:
            opportunities = self.env['crm.lead'].search([('partner_id', '=', order.partner_id.id)])
            order.opportunity_ids = opportunities


class CrmLead(models.Model):
    _inherit = 'crm.lead'

    purchase_order_ids = fields.Many2many('purchase.order', string='Associated Purchases',
                                          compute='_compute_purchase_orders',create_edit=True)
    total_expenses = fields.Float(string='Total Expenses',compute='_compute_total_expenses')
    total_purchases = fields.Float(string='Total Purchases', compute='_compute_total_purchases')
    total_orders = fields.Float(string='Total Orders', compute='_compute_total_orders')
    diff = fields.Float(string='Difference', compute='_compute_difference')
    hr_expense_ids = fields.Many2many('hr.expense', string='Expenses', compute='_compute_expense',create_edit=True)
    
    

    def _compute_expense(self):
        for lead in self:
            expense = self.env['hr.expense'].search(
                [('opportunity_ids', 'in', [lead.id]), ('state', '=', 'approved')])
            lead.hr_expense_ids = expense
            
    def _compute_total_orders(self):
        for lead in self:
            lead.total_orders = lead.sale_amount_total
            
    def _compute_total_expenses(self):
        for lead in self:
            lead.total_expenses = sum(lead.hr_expense_ids.mapped('total_amount'))

    @api.depends('purchase_order_ids.amount_total')
    def _compute_total_purchases(self):
        for lead in self:
            lead.total_purchases = sum(lead.purchase_order_ids.mapped('amount_total'))

    @api.depends('total_orders', 'total_purchases', 'total_expenses')
    def _compute_difference(self):
        for lead in self:
            lead.diff = lead.total_orders - (lead.total_purchases + lead.total_expenses)

    def show_achat(self):
        self.ensure_one()
        return {
            'name': 'Associated Purchases',
            'view_mode': 'tree',
            'res_model': 'purchase.order',
            'domain': [('id', 'in', self.purchase_order_ids.ids)],
            'type': 'ir.actions.act_window',
        }

    def _compute_purchase_orders(self):
        for lead in self:
            purchase_orders = self.env['purchase.order'].search(
                [('opportunity_ids', 'in', [lead.id]), ('state', '=', 'purchase')])
            lead.purchase_order_ids = purchase_orders
            
    
            

    
    def create_new_purchase(self):
        PurchaseOrder = self.env['purchase.order']
        
        # Create a new purchase order
        purchase_vals = {
            'opportunity_ids': self.id,
            'partner_id': self.partner_id.id,  # Assuming you want to use the CRM partner
            # Add other purchase values
        }
        new_purchase = PurchaseOrder.create(purchase_vals)
        
        return {
            'type': 'ir.actions.act_window',
            'name': 'Purchase Order',
            'res_model': 'purchase.order',
            'res_id': new_purchase.id,
            'view_mode': 'form',
            'view_id': self.env.ref('purchase.purchase_order_form').id,
            'target': 'current',
        }
          
    def create_new_expense(self):
        Expense = self.env['hr.expense']
        
        # Create a new purchase order
        
        expense_vals = {
            'opportunity_ids': self.id,
            'employee_id': self.partner_id.id,
            'name': 'Expense Description Here',
            'unit_amount': 0.0,
            # Add other purchase values
        }
        new_expense = Expense.create(expense_vals)
        
        return {
            'type': 'ir.actions.act_window',
            'name': 'Expense',
            'res_model': 'hr.expense',
            'res_id': new_expense.id,
            'view_mode': 'form',
            'view_id': self.env.ref('hr_expense.hr_expense_view_form').id,
            'target': 'current',
        }
     


class PurchaseOrderController(models.Model):
    _inherit = 'purchase.order'

    def show_opportunities(self):
        self.ensure_one()
        return {
            'name': 'Opportunities for Purchase Order',
            'view_mode': 'tree',
            'res_model': 'crm.lead',
            'domain': [('id', 'in', self.opportunity_ids.ids)],
            'type': 'ir.actions.act_window',
        }
