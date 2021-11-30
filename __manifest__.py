# -*- coding: utf-8 -*-
{
    'name': "dRV Printing",

    'summary': """
        Print, Art & Stationary""",

    'description': """
        Check out my shop if you want to print something unique and fulfill your work needs 
    """,

    'author': "dRV Corp",
    'website': "http://www.drvcorp.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],


    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/accepted.xml',
        'views/accounting.xml',
        'views/customer.xml',
        'views/delivered.xml',
        'views/kirim.xml',
        'views/material.xml',
        'views/menu.xml',
        'views/order.xml',
        'views/pegawai.xml',
        'views/printing.xml',
        'views/purchase.xml',
        'views/stationary.xml',
        'views/supplier.xml',
        'views/templates.xml',
        'report/invoice.xml',
        'report/report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
