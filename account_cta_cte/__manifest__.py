# -*- coding: utf-8 -*-
{
    'name': "account_cta_cte",

    'summary': """
        Module to manage account CTA CTE
        """,

    'description': """
        This module allows you to manage account CTA CTE records with basic information.
    """,

    'author': "Diego Aquino",
    'category': 'Accounting',
    'version': '0.1',
    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'reports/report_account_cta_cte.xml',
        'views/account_cta_cte_view.xml',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    
    'installable': True,
    'application': True,
}
