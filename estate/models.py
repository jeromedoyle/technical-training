from odoo import fields, models
from datetime import date, timedelta


class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Estate Property Model"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date(
        string="Available From", copy=False, default=date.today() + timedelta(days=90)
    )
    expected_price = fields.Float(required=True)
    selling_price = fields.Float(readonly=True, copy=False)
    bedrooms = fields.Integer(default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer()
    garage = fields.Boolean()
    garden = fields.Boolean()
    garden_area = fields.Integer(string="Garden Orientation (sqm)")
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
    active = fields.Boolean(default=True)
    state = fields.Selection(
        string="State",
        selection=[
            ("new", "New"),
            ("offer received", "Offer Received"),
            ("offer accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        help="The current state of the listing",
        default="new",
    )
    property_type_id = fields.Many2one("estate.property_type", string="Property Type")
    buyer = fields.Many2one("res.partner", string="Buyer")
    seller = fields.Many2one(
        "res.users", string="Salesperson", default=lambda self: self.env.user
    )
    tag_ids = fields.Many2many("estate.property.tag", string="Tags")


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type Model"

    name = fields.Char(required=True)


class EstatePropertyTag(models.Model):
    _name = "estate.property.tag"
    _description = "Tag to identify attributes of a property"

    name = fields.Char(required=True)
