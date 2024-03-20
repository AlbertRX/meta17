# -*- coding: utf-8 -*-

from odoo import models, fields, api


class product_catalog(models.Model):
    _name = 'product_info_management.product_catalog'
    _description = 'product_info_management.product_catalog,产品信息管理.产品目录'

    name = fields.Char(string='名称', required=True)

    parent_id = fields.Many2one(
        'product_info_management.product_catalog', string='上级目录')

    child_ids = fields.One2many(
        'product_info_management.product_catalog', 'parent_id', string='下级目录')

    product_ids = fields.One2many(
        'product_info_management.product_base_info', 'product_catalog_id', string='产品')

    article_id = fields.Many2one(
        'product_info_management.catalog_article', string='文章')
    
    
