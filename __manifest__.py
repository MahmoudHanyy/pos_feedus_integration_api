# -*- coding: utf-8 -*-
{
    'name': "POS Product/Order APIs",

    'summary': """""",

    'description': """""",

    'author': "BPerformance",
    'website': "",

    'category': 'Point Of Sale',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','point_of_sale', 'contacts', 'pos_customer_list'],
    "external_dependencies": {"python" : ["pyjwt"]},

    # always loaded
    'data': [
        'views/pos_config_views.xml'
    ],
}
