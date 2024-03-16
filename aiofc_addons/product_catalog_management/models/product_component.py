# -*- coding: utf-8 -*-

from odoo import models, fields, api

# 产品组件


class product_component(models.Model):
    _name = 'product_catalog_management.product_component'
    _description = 'product_catalog_management.product_catalog_management,产品目录管理模块.产品组件'

    name = fields.Char(
        '组件名称', related='product_catalog_id.name')

    product_catalog_id = fields.Many2one(
        'product_catalog_management.product_catalog', string='组件名称', required=True)

    component_code = fields.Char('组件识别码', required=True)

    description = fields.Text('描述')
