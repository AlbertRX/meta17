from odoo import models, fields, api


class product_attribute_value(models.Model):
    _name = 'product_info_management.product_attribute_value'
    _description = 'product_info_management.product_attribute_value,产品信息管理.产品属性值'

    name = fields.Char(string='属性值', required=True)

    attribute_id = fields.Many2one(
        'product_info_management.product_attribute', string='属性')
