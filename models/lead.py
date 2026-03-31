from odoo import models, fields, api


class CrmLeads(models.Model):
    _name = 'crm.lead.demo'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'CRM Leads Demo'
    
    name = fields.Char(string='Name')
    car_model = fields.Char(string="Car Model")
    age = fields.Integer(string="Age")
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
    ], string="Gender")
    phone = fields.Char(string="Phone")
    current_job = fields.Char(string="Current Job")
    assign_end_users = fields.Many2one('res.users', string="Assign End Users")