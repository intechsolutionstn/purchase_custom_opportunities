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
    'name': 'Products shortcut on odoo apps menu ',
    'version': '1.2',
    'category': 'base',
    'sequence': 35,
    'description': "This module adds a shortcut to the products menu on the main apps menu in odoo 14",
    'website': 'https://www.intech-eg.tech',
    'depends': ['product','sale'],
    'author': 'InTech Solutions -- Rabeb Mahmoudi',
    'support': 'odooappssupport@intech-eg.tech',
    
    'data': [
        'views/menu.xml',
    ],
    'qweb': [
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
}
