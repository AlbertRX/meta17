
from odoo import models, fields, api


class catalog_category(models.Model):
    _name = 'pim.catalog_category'
    _description = 'pim.catalog_category,产品信息管理.目录类别'

    catalog_id = fields.Char(string='目录', size=24)

    category_id = fields.Char(string='类别', size=24)

    active = fields.Boolean(
        '启用', default=True,
        help="By unchecking the active field, you may hide an INCOTERM you will not use.")

    company_id = fields.Many2one(
        'res.company', string='Company', default=lambda self: self.env.company)

    _sql_constraints = [
        ('catalog_category_uniq', 'unique(catalog_id, category_id, company_id)',
         'The combination of catalog, category and company must be unique!')
    ]
