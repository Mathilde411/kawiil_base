from odoo import fields, models


class Commentaire(models.Model):
    _name = "appel.commentaire"
    _description = "Commentaire Appel"

    timestamp = fields.Datetime(required=True)
    commentaire = fields.Text(required=True)

    personne_id = fields.Many2one("appel.personne", required=True)
    seance_id = fields.Many2one("appel.seance", required=True)

