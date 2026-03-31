from odoo import models, fields


class QuestionAnswer(models.Model):
    _name = 'survey.question.answer'
    _description = 'Survey Question Answer'

    question_id = fields.Many2one(
        'survey.question',
        string="Question ID"
    )
    answer = fields.Text(string="Answer to the question")
    response_id = fields.Many2one(
        "survey.response",
        string="Survey Response id"
    )