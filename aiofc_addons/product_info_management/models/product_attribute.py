from odoo import models, fields, api


class product_attribute(models.Model):
    _name = 'product_info_management.product_attribute'
    _description = 'product_info_management.product_attribute,产品信息管理.产品属性'

    name = fields.Char(string='属性名称', required=True)
