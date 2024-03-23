# -*- coding: utf-8 -*-
{
    'name': "copywriting",

    'summary': "文案写作",

    'description': """
                Long description of module's purpose
    """,

    'author': "yfc",
    'website': "https://www.yourcompany.com",
    'category': 'copywriting',
    'version': '0.1',
    'installable': True,
    'auto_install': False,
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/copywriting_views.xml',
        'views/copywriting_actions.xml',
        'views/copywriting_menus.xml',
    ],
}
