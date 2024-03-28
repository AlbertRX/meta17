from odoo import models, fields, api


class product_attribute_value(models.Model):
    _name = 'pim.product_attribute_value'
    _description = 'pim.product_attribute_value,产品信息管理.产品属性值'

    product_id = fields.Char(string='产品', size=24)

    attribute_id = fields.Char(string='属性', size=24)

    data = fields.Json(string='数据')

    channel_id = fields.Char(string='渠道', size=24)

    text_value = fields.Text(string='文本值', size=255)

    float_value = fields.Float(string='浮点值')

    int_value = fields.Integer(string='整数值')

    varchar_value = fields.Char(string='字符串值', size=255)

    datetime_value = fields.Datetime(string='日期时间值')

    date_value = fields.Date(string='日期值')

    bool_value = fields.Boolean(string='布尔值')

    attribute_type = fields.Char(string='属性类型')

    is_variant_specific_attribute = fields.Integer(string='是否变体特定属性')
    
    count_bytes_instead_of_characters = fields.Boolean(string='计算字节而不是字符')
    
    reference_value = fields.Char(string='参考值', size=255)
