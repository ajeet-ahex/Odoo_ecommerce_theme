import requests
from odoo import models, fields

class HelloWorldModel(models.Model):
    _name = 'hello.world.model'
    _description = 'Model to store Hello World API response'

    name = fields.Char(string="API Response", readonly=True)

    def fetch_and_store_hello(self):
        try:
            response = requests.get('http://localhost:8069/hello')  # Adjust the URL if necessary
            if response.status_code == 200:
                self.name = response.text
            else:
                self.name = "Failed to fetch data"
        except Exception as e:
            self.name = f"Error: {str(e)}"
