from odoo import models, fields, api


class product_attribute_line(models.Model):
    _name = 'pim.product_attribute_line'
    _description = 'pim.product_attribute_line,产品信息管理.产品属性行'

    sequence = fields.Integer("Sequence", default=10)

    product_id = fields.Many2one(
        'pim.product_base_info', string='产品')

    attribute_id = fields.Many2one(
        'pim.product_attribute', string='属性')

    attribute_value_ids = fields.Many2many(
        'pim.product_attribute_value', 'product_attribute_value_rel', string='属性值')
