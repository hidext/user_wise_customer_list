# -*- coding: utf-8 -*-
{
    'name': "Sale Person Related Contacts",
    'version': '13.0.1',
    'summary': """This Module is designed for Sale Person Design""",

    'description': """This Module is design for sale person related contacts""",

    'author': "Hidext",
    'website': "http://www.hidext.com",

    'category': 'Uncategorized',
    'version': '0.1',

    'depends': ['base', 'contacts', 'sale', 'stock'],
    'price': 15.0,
    'currency': 'EUR',

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/customer_person.xml',
        # 'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
