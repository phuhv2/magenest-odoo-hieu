{
    'name': 'School',
    'version': '1.1',
    'author': 'hieunqdev',
    'summary': "School Management System",
    'sequence': 1,
    'description': "School Management System software supported in Odoo 16",
    'category': 'School',
    'website': 'https://hieunqdev.school.com',
    'depends': ['base'],
    'installable': True,
    'application': True,
    'data': [
        "security/ir.model.access.csv",
        "views/school_view.xml"
    ]
}