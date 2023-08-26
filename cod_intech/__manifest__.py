# -*- coding: utf-8 -*-

{
    # Module Information
    'name': 'COD | Website Cash on Delivery | Cash on Delivery',
    'category': 'Website/eCommerce/account',
    'summary': 'This application enables customers to make payments at their doorstep, facilitating online shopping with the Cash on Delivery (COD) payment method.',
    'version': '14.0',
    "description": "Cash on Delivery (COD) - Payment method for orders with cash on delivery option. Also available as a website payment method and delivery option.",
    'license': 'OPL-1',    
    'depends': ['website_sale','payment','sale_management','account'],

    'data': [
        'data/payment_acquirer_data.xml',
        'security/ir.model.access.csv',
        'views/cod_view.xml',
        'views/template.xml',
        'views/cod_collection_report.xml',
        'views/report_cod_collection.xml',
    ],


    ],

    # Author
    'author': 'InTech Solutions',
    'website': 'https://www.intech-eg.tech',
    'maintainer': 'InTech Solutions',

    # Technical
    'installable': True,
    'auto_install': False,
    'price': 10.00,
    'currency': 'EUR', 
}
