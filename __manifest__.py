# -*- coding: utf-8 -*-
{
    'name': "MBUZZ Interns ",

    'summary': "A form module to collect and manage internship details of MBUZZ interns.",

    'description': """
This module is designed to collect, store, and manage detailed information about interns at MBUZZ. It provides a structured form interface within the Odoo environment, allowing administrators to input and track intern-related data such as personal details, internship duration, department, mentor assignment, and progress notes. The module streamlines intern data management, supports HR operations, and ensures centralized record-keeping for better visibility and reporting.
    """,

    'author': "Arun Kumar NV / Devops & Odoo Developer Intern",
    'website': "https://www.mbuzztech.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Form',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/student_views.xml',
        'security/ir.model.access.csv'
    ],

    'images': ['static/description/icon.png']

}

