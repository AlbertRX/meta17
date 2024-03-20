# -*- coding: utf-8 -*-
{
    'name': "product_info_management",

    'summary': "产品信息管理模块",

    'description': """
            Long description of module's purpose
    """,

    'author': "yfc",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_catalog_data.xml
    # for the full list
    'catalog': 'product',
    'version': '0.1',
    'installable': True,
    'auto_install': False,
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/product_catalog_views.xml',
        'views/product_info_management_actions.xml',
        'views/product_info_management_menus.xml',
    ],
}
