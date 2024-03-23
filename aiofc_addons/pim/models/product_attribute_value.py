from odoo import models, fields, api


class product_attribute_value(models.Model):
    _name = 'pim.product_attribute_value'
    _description = 'pim.product_attribute_value,产品信息管理.产品属性值'

    name = fields.Char(string='属性值', required=True)

    attribute_id = fields.Many2one(
        'pim.product_attribute', string='属性')
