from odoo import models, fields, api


class attribute(models.Model):
    _name = 'pim.attribute'
    _description = 'pim.attribute,产品信息管理.属性'

    name = fields.Char(string='属性名称', required=True)

    type = fields.Selection(string='属性类型', selection=[
        ('text', '文本'),
        ('float', '浮点'),
        ('float_range', '浮点范围'),
        ('int', '整数'),
        ('int_range', '整数范围'),
        ('array', '数组'),
        ('bool', '布尔'),
        ('asset', '资产'),
        ('date', '日期'),
        ('datetime', '日期时间'),
        ('list', '列表'),
        ('multi_value_list', '多值列表'),
        ('url', 'URL'),
        ('string', '字符串'),
        ('html', 'HTML'),
    ])

    attribute_group_id = fields.Char(string='属性组', size=24)

    code = fields.Char(string='属性编码')

    owner_user_id = fields.Char(string='拥有者', size=24)

    assigned_user_id = fields.Char(string='分配给', size=24)

    is_multilang = fields.Boolean(string='多语言')

    asset_type = fields.Char(string='资产类型')

    pattern = fields.Char(string='模式')

    unique = fields.Boolean(string='唯一')

    attribute_tab_id = fields.Char(string='属性标签', size=24)

    prohibited_empty_value = fields.Boolean(string='禁止空值')

    data = fields.Json(string='数据')

    virtual_product_field = fields.Boolean(string='虚拟产品字段')

    is_required = fields.Boolean(string='必填')

    sort_order = fields.Integer(string='排序', default=0)

    default_channel_id = fields.Char(string='默认渠道', size=24)

    sort_order_in_attribute_group = fields.Integer(string='属性组排序')

    sort_order_in_product = fields.Integer(string='产品排序')

    tooltip = fields.Text(string='提示')

    description = fields.Text(string='描述')

    extensible_enum_id = fields.Char(string='可扩展枚举', size=24)

    amount_of_digits_after_comma = fields.Integer(string='小数点后位数')

    default_unit = fields.Char(string='默认单位')

    measure_id = fields.Char(string='度量', size=24)

    use_disabled_textarea_in_view_mode = fields.Boolean(
        string='在查看模式下使用禁用的文本区域')

    default_date = fields.Date(string='默认日期')

    default_value = fields.Text(string='默认值')

    active = fields.Boolean(
        '启用', default=True,
        help="By unchecking the active field, you may hide an INCOTERM you will not use.")

    company_id = fields.Many2one(
        'res.company', string='Company', default=lambda self: self.env.company)

    _sql_constraints = [
        ('name_company_uniq', 'unique(name, company_id)',
         'The name of the job position must be unique per department in company!')
    ]
