from odoo import models, fields, api


class catalog_article(models.Model):
    _name = 'product_info_management.catalog_article'
    _description = 'product_info_management.catalog_article,产品信息管理.产品目录文章'

    name = fields.Char(string='文章标题', required=True)
    content = fields.Text(string='文章内容')
