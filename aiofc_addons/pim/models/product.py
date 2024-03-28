from odoo import models, fields, api, _


class Product(models.Model):
    _name = 'pim.product'
    _description = 'pim.product,产品信息管理.产品'

    name = fields.Char(string='产品名称', required=True)

    sku = fields.Char(string='SKU', size=255)

    quantity = fields.Float(string='数量', default=0)

    brand_id = fields.Char(string='品牌', size=24)

    product_status = fields.Selection(

        [
            ('draft', '草稿'),
            ('prepared', '已准备'),
            ('reviewed', '审核'),
            ('not_ready', '未准备'),
            ('done', '完成'),
        ],
        default="draft",
    )

    tax_id = fields.Char(string='税', size=24)

    ean = fields.Char(string='厂商识别码', size=255)

    mpn = fields.Char(string='最小包装数量', size=255)

    packaging_id = fields.Char(string='包装', size=24)

    uvp = fields.Float(string='市场指导价', default=0)

    tag = fields.Json(string='标签')

    owner_user_id = fields.Char(string='拥有者', size=24)

    assigned_user_id = fields.Char(string='分配给', size=24)

    long_description = fields.Text(string='长描述')

    product_serie_id = fields.Char(string='产品系列', size=24)

    data = fields.Json(string='数据')

    catalog_id = fields.Char(string='目录', size=24)

    is_inherit_assigned_user = fields.Boolean(string='是否继承分派者', default=False)

    is_inherit_owner_user = fields.Boolean(string='是否继承拥有者', default=False)

    is_inherit_teams = fields.Boolean(string='是否继承团队', default=False)

    task_status = fields.Json(string='任务状态')

    sort_order = fields.Integer(string='排序', default=0)

    price_unit_id = fields.Char(string='价格单位', size=24)

    image_id = fields.Char(string='图片', size=24)

    active = fields.Boolean(
        '启用', default=True,
        help="By unchecking the active field, you may hide an INCOTERM you will not use.")

    company_id = fields.Many2one(
        'res.company', string='Company', default=lambda self: self.env.company)

    _sql_constraints = [
        ('name_company_uniq', 'unique(name, company_id)',
         'The name of the job position must be unique per department in company!')
    ]

    price = fields.Float(string='单价', default=0)
