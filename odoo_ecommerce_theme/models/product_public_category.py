from odoo import models, fields

class ProductPublicCategory(models.Model):
    _inherit = 'product.public.category'

    brand_ids = fields.Many2many('product.brand', string='Brands')
