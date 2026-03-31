from odoo import fields, models


class ServeyResponse(models.Model):
    _name = 'survey.response'
    _description = 'Survey Response'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Response Name", default="New Response", required=True)
    survey_id = fields.Many2one('survey.survey', string="Survey")
    answer_ids = fields.One2many(
        'survey.question.answer', 
        'response_id'
    )
    lead = fields.Many2one(
        'crm.lead.demo',
        string="Related Lead"
    )
    user_id = fields.Many2one('res.users', string="User ID")
    state = fields.Selection([
        ('pending', 'Pending'),
        ('done', 'Done')
    ], string='Status', default='pending')

    sub_state = fields.Selection([
        ('p1', 'Not Answered'),
        ('p2', 'Answered but not interested'),
        ('p3', 'Answered and request for another time call'),
        ('d', 'Completed')
    ], string='Sub-Status', default='p1')

    comments = fields.Text(
        string="Comments",
        tracking=True
    )

    def write(self, vals):
        res = super().write(vals)
        if 'sub_state' in vals:
            self.state = 'pending' if vals['sub_state'] != 'd' else 'done'
        return res
        

    