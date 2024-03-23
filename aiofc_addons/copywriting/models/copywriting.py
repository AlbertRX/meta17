# -*- coding: utf-8 -*-

from odoo import models, fields, api


class copywriting(models.Model):
    _name = 'copywriting.copywriting'
    _description = 'copywriting.copywriting,文案写作.文案'
    _rec_name = 'title'

    title = fields.Char(string='标题')

    body_data = fields.Json(string='内容数据')

    published = fields.Boolean(string='发布')
