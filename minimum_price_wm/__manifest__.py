# -*- coding: utf-8 -*-
{
    'name': " Minimum Price Module webmania",
    'summary': """
       Lock and control your minimum sale price to POS, Sales Order and Invoice
""",
    'description': """
        Lock and control your minimum sale price to POS, Sales Order and Invoice
    """,
    'author': "webmania",
    'website': "https://www.webmania.ma/",
    'category': 'Sale',
    'version': '0.1',
    'depends': ['web','base', 'sale'],
    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/templates.xml',
        'views/product_view.xml',
    ],

}
