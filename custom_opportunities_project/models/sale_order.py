from odoo import models, fields, api


class ProjectProject(models.Model):
    _inherit = 'project.project'

    opportunity_id = fields.Many2one('crm.lead', string='Opportunity', compute='_compute_opportunity_id', store=True)
    display_name = fields.Char(compute='_compute_display_name', string="display name", store=True)
    name = fields.Char("Name", index=True, required=True, tracking=True,compute='_compute_display_name', store=True)
 

    
    def _compute_display_name(self):
        for task in self:
            task.display_name = f"{task.name} - {task.opportunity_id.name}" if task.opportunity_id.name else task.name
            task.name = task.display_name

    display_name = fields.Char(string="Display Name", compute="_compute_display_name", store=True)
    def _compute_opportunity_id(self):
        for project in self:
            if project.sale_order_id :
               project.opportunity_id = project.sale_order_id.opportunity_id
               
    @api.onchange('name')           
    def _compute_name(self):
        for project in self:
            if project.opportunity_id :
               project.name = project.name + ' ' + project.opportunity_id.name
