from odoo import models, fields, api


class attribute_tab(models.Model):
    _name = 'pim.attribute_tab'
    _description = 'pim.attribute_tab,产品信息管理.属性标签'

    name = fields.Char(string='属性标签名称', required=True)

    description = fields.Text(string='描述')

    active = fields.Boolean(
        '启用', default=True,
        help="By unchecking the active field, you may hide an INCOTERM you will not use.")

    company_id = fields.Many2one(
        'res.company', string='Company', default=lambda self: self.env.company)

    _sql_constraints = [
        ('name_company_uniq', 'unique(name, company_id)',
         'The name of the job position must be unique per department in company!')
    ]
