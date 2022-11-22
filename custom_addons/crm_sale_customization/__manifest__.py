# -*- coding: utf-8 -*-
{
    'name': "CRM SALES Customization",

    'summary': """
        CRM SALES Customization""",

    'description': """
        CRM SALES Customization
    """,

    'author': "hieunqdev",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/plan_sale_order_view.xml',
        'views/advan_crm_quotations_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
