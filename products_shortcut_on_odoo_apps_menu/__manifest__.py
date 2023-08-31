# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Products shortcut on odoo apps menu ',
    'version': '1.2',
    'category': '',
    'sequence': 35,
    'description': "",
    'website': '',
    'depends': ['product','sale'],
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
