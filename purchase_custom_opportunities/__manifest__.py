# -*- coding: utf-8 -*-
#╔══════════════════════════════════════════════════════════════════════╗
#║                  SOFTWARE DEVELOPED AND SUPPORTED BY                 ║
#║                  InTech Solutions www.intech-eg.tech                 ║
#║                      COPYRIGHT (C) 201_ - TODAY                      ║
#║                      https://www.intech-eg.tech                      ║
#║                          +216-56-373-373                             ║  
#║                      support: abnasser@intech-eg.tech                ║
#╚══════════════════════════════════════════════════════════════════════╝
{
    'name': 'CRM Opportunity purchases & expenses linking',
    'version': '1.2',
    'category': 'CRM/Purchase/Expenses/Inventory',
    'sequence': 35,
    'description': "Odoo 14 CRM Opportunity purchases & expenses linking module seamlessly connects sales opportunities with related purchases and expenses. It also offers a clear indicator to assess profitability by calculating the difference between sales amounts, purchases, and expenses. NOTE: you have to install the folloing modules (CRM, purchases & expenses)",
    'images': [
        'static/description/purchases_in_opportunity.jpg',
    ],
    'website': 'https://www.intech-eg.tech',
    'author': 'InTech Solutions -- Rabeb Mahmoudi',
    'support': 'odooappssupport@intech-eg.tech',
    'depends': ['crm', 'account', 'purchase', 'hr_expense'],
    'data': [

        'views/purchase_views.xml',
        'views/crm_lead_views.xml',
        'views/hr_expense_views.xml',
        #'views/custom_sale_order.xml',
    ],
    'qweb': [
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    "price": 25,
    "currency": "EUR",
}
