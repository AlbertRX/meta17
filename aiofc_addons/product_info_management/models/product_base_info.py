
from odoo import models, fields, api


class product_base_info(models.Model):
    _name = 'product_info_management.product_base_info'
    _description = 'product_info_management.product_base_info,产品信息管理.产品基本信息'

    name = fields.Char(string='产品名称', required=True)
    sku = fields.Char(string='产品SKU', required=True)
    barcode = fields.Char(string='产品条码')
    default_code = fields.Char(string='产品编码')
    product_catalog_id = fields.Many2one(
        'product_info_management.product_catalog', string='产品目录')
