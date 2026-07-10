from odoo import models, fields

class Seance(models.Model):
    _name = "appel.commentaire"
    _description = "Commentaire Appel"

    timestamp = fields.Datetime()
    commentaire = fields.Text()

    personne_id = fields.Many2one('appel.personne')
    