from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    custom_description = fields.Char(string='Custom Description')
