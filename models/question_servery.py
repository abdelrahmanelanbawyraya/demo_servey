from odoo import models, fields


class QuestionServey(models.Model):
    _name = 'survey.question'
    _description = 'Survey Question'
    
    name = fields.Char(string="Question Name")
    survey_id = fields.Many2one('survey.survey', string="Survey ID")