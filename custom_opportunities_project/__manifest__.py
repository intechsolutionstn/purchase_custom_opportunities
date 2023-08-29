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
    'name': 'Opportunities Module for Project',
    'version': '1.2',
    'category': 'Project/CRM',
    'description': "This Odoo module harmoniously merges the Project and CRM Opportunity modules, simplifying the conversion of leads into projects. Facilitating a fluid transition from initial contact to project execution, this integration fosters efficient communication, optimized resource allocation, and seamless project tracking. Elevate your workflow by uniting these modules, ensuring a cohesive and productive business journey.",
    'images': [
        'static/description/image.png',
    ],
    'depends': ['crm', 'project', 'sale'],
    'website': 'https://www.intech-eg.tech',
    'author': 'InTech Solutions -- Rabeb Mahmoudi',
    'support': 'odooappssupport@intech-eg.tech',
    'data': [
         'views/crm_lead_views.xml',
         'views/project_views.xml',
         
    
    ],
    'qweb': [
    ],
    'demo': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
    'license': 'LGPL-3',
    "price": 15,
    "currency": "EUR",
}
