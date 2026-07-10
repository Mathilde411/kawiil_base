from odoo import models, fields

class Seance(models.Model):
    _name = "appel.seance"
    _description = "Seance Appel"

    name = fields.Char(string="Nom")
    date = fields.Date()
    notes = fields.Text()

    personne_ids = fields.Many2many('appel.personne')
    