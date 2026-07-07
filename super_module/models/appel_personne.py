from odoo import models, fields

class Personne(models.Model):
    _name = "appel.personne"
    _description = "Personne Appel"

    name = fields.Char(string="Nom")
    age = fields.Integer()
