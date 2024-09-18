from odoo import fields, models


class ProductBrand(models.Model):
    _name = "product.brand"
    _inherit = ["product.brand", "website.published.mixin"]

    is_published = fields.Boolean(default=True)
    category_id = fields.Many2one('product.public.category', string="Category")
    product_ids = fields.One2many('product.template', 'product_brand_id', string="Products")


class ProductPublicCategory(models.Model):
    _inherit = 'product.public.category'

    brand_ids = fields.Many2many(
        'product.brand',
        'category_brand_rel',
        'category_id',
        'brand_id',
        string='Brands'
    )