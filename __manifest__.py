# -*- coding: utf-8 -*-
{
    'name': "FieldService Portal",

    'summary': """
        Manage Field Service Location in the Portal""",

    'description': """
        Show current fsm.location STATUS|EQUIPMENT_LOCATION|EQUIPMENT_STATUS
    """,

    'author': "POPSOLUTIONS.CO",
    'website': "https://www.popsolutions.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Membership Certification',
    'version': '12.20.9.23',

    # any module necessary for this one to work correctly
    'depends': ['base',
                'sale',
                'portal',
                'contacts',
                'membership',
                'website_membership',
                'l10n_br_base',
                ],

    # always loaded
    'data': [
        'security/fsm_equipment_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/res_partner_view.xml',
        'views/fsm_equipment_certificates_view.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
