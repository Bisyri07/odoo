from odoo import models, fields

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property"


    name = fields.Char(string="name", required=True)
    description = fields.Text(default="Estate Property Description")
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    selling_price = fields.Float()
    bedrooms = fields.Integer()
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        selection = [
            ("N", "North"), ("S", "South"), ("E", "East"), ("W", "West")
        ],
        string = "Garden Orientation",
    )