import logging

from odoo import http
from odoo.http import request
from odoo.osv import expression
from odoo.addons.website_sale.controllers.main import QueryURL, WebsiteSale

_logger = logging.getLogger(__name__)


class WebsiteSaleProductBrand(WebsiteSale):


    @http.route(["/page/product_categories","/"], type="http", auth="public", website=True)
    def product_categories(self, **post):
        # Fetch all product categories
        categories = request.env["product.public.category"].sudo().search([])
        _logger.info(f"Retrieved categories: {categories}")

        # Prepare the values to be passed to the template
        values = {"categories": categories}

        return request.render("odoo_ecommerce_theme.custom_homepage", values)