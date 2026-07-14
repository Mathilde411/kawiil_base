from odoo import api, fields, models


class Commentaire(models.Model):
    _name = "appel.commentaire"
    _description = "Commentaire Appel"

    timestamp = fields.Datetime()
    commentaire = fields.Text()

    personne_id = fields.Many2one("appel.personne", required=True)
    user_id = fields.Many2one(related="personne_id.user_id")

