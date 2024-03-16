# -*- coding: utf-8 -*-

from odoo import models, fields, api


class product_alias(models.Model):
    _name = 'product_catalog_management.product_alias'
    _description = 'product_catalog_management.product_catalog_management,产品目录管理模块.产品别名'

    name = fields.Char('别名', required=True)
    product_alias = fields.Char('产品别名编码', required=True)
    product_catalog_id = fields.Many2one(
        'product_catalog_management.product_catalog', string='产品名称', required=True)
    description = fields.Text('描述')
