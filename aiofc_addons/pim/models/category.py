from odoo import models, fields, api


class category (models.Model):
    _name = 'pim.category'
    _description = 'pim.category,产品信息管理.类别'

    name = fields.Char(string='类别名称', size=255)

    description = fields.Text(string='描述')

    active = fields.Boolean(
        '启用', default=True,
        help="By unchecking the active field, you may hide an INCOTERM you will not use.")

    code = fields.Char(string='类别编码', size=255)

    category_route = fields.Text(string='类别路径')

    category_route_name = fields.Text(string='类别路径名称')

    owner_user_id = fields.Char(string='拥有者', size=24)

    assigned_user_id = fields.Char(string='分配给', size=24)

    sort_order = fields.Integer(string='排序', default=0)

    company_id = fields.Many2one(
        'res.company', string='Company', default=lambda self: self.env.company)

    _sql_constraints = [
        ('name_company_uniq', 'unique(name, company_id)',
         'The name of the job position must be unique per department in company!')
    ]
