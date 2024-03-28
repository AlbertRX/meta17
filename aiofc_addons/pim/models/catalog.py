from odoo import models, fields, api


class catalog(models.Model):
    _name = 'pim.catalog'
    _description = 'pim.catalog,产品信息管理.目录'

    name = fields.Char(string='目录名称', required=True)

    description = fields.Text(string='描述')

    active = fields.Boolean(
        '启用', default=True,
        help="By unchecking the active field, you may hide an INCOTERM you will not use.")

    assigned_user_id = fields.Char(string='分配给', size=24)

    code = fields.Char(string='目录编码', size=255)

    company_id = fields.Many2one(
        'res.company', string='Company', default=lambda self: self.env.company)

    _sql_constraints = [
        ('name_company_uniq', 'unique(name, company_id)',
         'The name of the job position must be unique per department in company!')
    ]
