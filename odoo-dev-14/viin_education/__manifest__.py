{
   'name': "Education Management",
   'summary': "Module education management",
   'description': """
   What it does

   The module provides management education features.
   Key Features

   * Students management
   * Parents management
   """,
   'author': "Your name",
   'website': "https://viindoo.com",
   'category': 'Uncategorized',
   'version': '0.1.0',
   'depends': ['base'],
   'data': [
      'security/groups.xml',
      'security/ir.model.access.csv',
      'views/education_student_views.xml',
      'views/student_level_views.xml',
      'views/education_school_views.xml',
      'views/education_class_views.xml',
      'views/education_class_group_views.xml',
   ],
   'demo': ['demo.xml'],
}