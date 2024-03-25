from odoo import models, fields


class article_category(models.Model):
    _name = 'copywriting.article_category'
    _description = 'copywriting.article_category,文案写作.文章分类'
    _rec_name = 'name'

    name = fields.Char(string='名称')

    category_data = fields.Json(string='分类数据')

    active = fields.Boolean(default=True)

    article_collect_ids = fields.One2many(
        'copywriting.article_collect', 'category_id', string='文章集')

    company_id = fields.Many2one(
        'res.company', string='Company', default=lambda self: self.env.company)

    _sql_constraints = [
        ('name_company_uniq', 'unique(name, company_id, department_id)',
         'The name of the job position must be unique per department in company!')
    ]
