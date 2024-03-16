# -*- coding: utf-8 -*-

from odoo import models, fields, api


class product_catalog(models.Model):
    _name = 'product_catalog_management.product_catalog'
    _description = 'product_catalog_management.product_catalog_management,产品目录管理模块.产品目录'

    name = fields.Char('产品名称', required=True)
    reference_code = fields.Char('内部编码', required=True)
    description = fields.Text('描述')
    component_ids = fields.One2many(
        'product_catalog_management.product_component', 'product_catalog_id', string='产品组件名称')

    product_component_ids = fields.Many2many(
        'product_catalog_management.product_component', 'product_catalog_management_catalog_component_rel', 'product_catalog_id', 'product_component_id', string='产品组件')

    product_alias_ids = fields.One2many(
        "product_catalog_management.product_alias", "product_catalog_id", string="产品别名")
