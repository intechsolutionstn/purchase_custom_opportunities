# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from dateutil.relativedelta import relativedelta

from odoo import api, fields, models




class CrmLead(models.Model):
    _inherit = 'crm.lead'
    
    project_count = fields.Integer(compute='_compute_project_data', string="Number of Project")
   
    project_ids = fields.Many2many('project.project', string='Project',create_edit=True)
    
    

    def _compute_expense(self):
        for lead in self:
            expense = self.env['hr.expense'].search(
                [('opportunity_ids', 'in', [lead.id]), ('state', '=', 'approved')])
            lead.hr_expense_ids = expense
    @api.depends('name')  # Change this to the appropriate field that links leads and projects
    def _compute_project_data(self):
        Project = self.env['project.project']
        
        for lead in self:
            project_domain = [('opportunity_id', '=', lead.id),('partner_id', '=', lead.partner_id.id)]
            lead.project_count = Project.search_count(project_domain)
            
    
    def action_sale_quotations_new(self):
        if not self.partner_id:
            return self.env["ir.actions.actions"]._for_xml_id("sale_crm.crm_quotation_partner_action")
        else:
            return self.action_new_quotation()

    def action_new_quotation(self):
        action = self.env["ir.actions.actions"]._for_xml_id("sale_crm.sale_action_quotations_new")
        action['context'] = {
            'search_default_opportunity_id': self.id,
            'default_opportunity_id': self.id,
            'search_default_partner_id': self.partner_id.id,
            'default_partner_id': self.partner_id.id,
            'default_campaign_id': self.campaign_id.id,
            'default_medium_id': self.medium_id.id,
            'default_origin': self.name + self.opportunity_id.name,
            'default_source_id': self.source_id.id,
            'default_company_id': self.company_id.id or self.env.company.id,
            'default_tag_ids': [(6, 0, self.tag_ids.ids)]
        }
        if self.team_id:
            action['context']['default_team_id'] = self.team_id.id,
        if self.user_id:
            action['context']['default_user_id'] = self.user_id.id
        return action

    def action_view_sale_quotation(self):
        action = self.env["ir.actions.actions"]._for_xml_id("sale.action_quotations_with_onboarding")
        action['context'] = {
            'search_default_draft': 1,
            'search_default_partner_id': self.partner_id.id,
            'default_partner_id': self.partner_id.id,
            'default_opportunity_id': self.id
        }
        action['domain'] = [('opportunity_id', '=', self.id), ('state', 'in', ['draft', 'sent'])]
        quotations = self.mapped('order_ids').filtered(lambda l: l.state in ('draft', 'sent'))
        if len(quotations) == 1:
            action['views'] = [(self.env.ref('sale.view_order_form').id, 'form')]
            action['res_id'] = quotations.id
        return action
        
    def action_list_related_projects(self):
        action = self.env["ir.actions.actions"]._for_xml_id("project.open_view_project_all")
        action['context'] = {
            'search_default_partner_id': self.partner_id.id,
            'default_partner_id': self.partner_id.id,
            'default_opportunity_id': self.id,
        }
        action['domain'] = [('opportunity_id', '=', self.id)]
        
       
        return action