from odoo import fields, models
from datetime import date, timedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Model"

    name = fields.Char(required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        copy=False, default=date.today() + timedelta(days=90)
    )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer()
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer()
    garden_orientation = fields.Selection(
        string="Garden Orientation",
        selection=[
            ("north", "North"),
            ("south", "South"),
            ("east", "East"),
            ("west", "West"),
        ],
        help="The direction the garden is orientated",
    )
    active = fields.Boolean(default=False)
    state = fields.Selection(
        string="State",
        selection=[
            ("New", "new"),
            ("Offer Received", "offer received"),
            ("Offer Accepted", "offer accepted"),
            ("Sold", "sold"),
            ("Canceled", "canceled"),
        ],
        help="The current state of the listing",
        default="New",
    )
