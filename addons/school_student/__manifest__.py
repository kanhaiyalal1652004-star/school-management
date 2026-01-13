{
    'name': 'School Student Management',
    'version': '18.0.1.0.0',
    'category': 'School Management',
    'summary': 'Student registration, profile management, admission records',
    'author': 'Kanhaiya Lal',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_views.xml',
        'views/parent_views.xml',
        'views/admission_views.xml',
    ],
    'demo': [],
    'installable': True,
    'auto_install': False,
}
