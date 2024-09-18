# __manifest__.py
{
    'name': 'Odoo e-commerece theme',
    'version': '1.0',
    'category': 'Website',
    'summary': 'A custom website with custom HTML',
    'author': 'Your Name',
    'depends': ['website', 'sale', 'website_payment', 'website_mail', 'portal_rating', 'digest', 'delivery','website_sale','web','base'],
    'data': [
        'views/home.xml',
        'views/signin.xml',
        'views/signin.xml',
        'views/SIgnUp.xml',
        'views/head.xml',
        'views/footer.xml',
        'views/shop.xml',
    ],
    'assets': {

    },
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
}
