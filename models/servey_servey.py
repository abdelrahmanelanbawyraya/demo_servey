from odoo import models, fields


class ServeyServey(models.Model):
    _name = 'survey.survey'
    _description = 'Survey'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Survey Name')
    description = fields.Text(string="Survey Description")
    question_ids = fields.One2many(
        'survey.question', 
        'survey_id', 
        string="Related Questions"
    )
    associated_users = fields.Many2many(
        'res.users',
        string="Associated Users"
    )