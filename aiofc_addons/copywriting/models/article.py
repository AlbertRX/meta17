# -*- coding: utf-8 -*-

import uuid

from odoo import models, fields, api


class article(models.Model):
    _name = 'copywriting.article'
    _description = 'copywriting.article,文案写作.文章'
    _rec_name = 'title'

    title = fields.Char(string='标题')

    uuid = fields.Char(string='UUID', default=lambda self: str(uuid.uuid4()))

    body_data = fields.Json(string='内容数据')

    published = fields.Boolean(string='发布')

    active = fields.Boolean(default=True)

    article_collect_id = fields.Many2one(
        'copywriting.article_collect', string='文章集')
    
    

    company_id = fields.Many2one(
        'res.company', string='Company', default=lambda self: self.env.company)

    _sql_constraints = [
        ('name_company_uniq', 'unique(name, company_id, department_id)',
         'The name of the job position must be unique per department in company!')
    ]
