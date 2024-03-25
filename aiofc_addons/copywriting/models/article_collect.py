from odoo import models, fields, api


class article_collect(models.Model):
    _name = 'copywriting.article_collect'
    _description = 'copywriting.article_collect,文案写作.文章集'

    name = fields.Char(string='书名', required=True)

    description = fields.Text(string='描述')

    catalog_list = fields.Json(string='目录列表')

    active = fields.Boolean(default=True)

    category_id = fields.Many2one('copywriting.article_category', string='分类')

    article_ids = fields.One2many(
        'copywriting.article', 'article_collect_id', string='文章'
    )

    company_id = fields.Many2one(
        'res.company', string='Company', default=lambda self: self.env.company)

    _sql_constraints = [
        ('name_company_uniq', 'unique(name, company_id, department_id)',
         'The name of the job position must be unique per department in company!')
    ]
