from odoo import models, fields, api


class attribute_group(models.Model):
    _name = 'pim.attribute_group'
    _description = 'pim.attribute_group,产品信息管理.属性组'

    name = fields.Char(string='属性组名称', required=True)

    active = fields.Boolean(
        '启用', default=True,
        help="By unchecking the active field, you may hide an INCOTERM you will not use.")

    description = fields.Text(string='描述')

    sort_order = fields.Integer(string='排序', default=0)

    assigned_user_id = fields.Char(string='分配给', size=24)

    code = fields.Char(string='属性组编码', size=255)

    owner_user_id = fields.Char(string='拥有者', size=24)

    company_id = fields.Many2one(
        'res.company', string='Company', default=lambda self: self.env.company)

    _sql_constraints = [
        ('name_company_uniq', 'unique(name, company_id)',
         'The name of the job position must be unique per department in company!')
    ]
