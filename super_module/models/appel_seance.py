from odoo import fields, models


class Seance(models.Model):
    _name = "appel.seance"
    _description = "Séance Appel"

    name = fields.Char(compute="_compute_name")
    date = fields.Date(required=True)
    notes = fields.Text()
    user_id = fields.Many2one("res.users")

    personne_ids = fields.Many2many("appel.personne")
    commentaire_ids = fields.One2many("appel.commentaire", "seance_id")

    def _compute_name(self):
        for seance in self:
            seance.name = f"Séance du {seance.date.strftime('%d/%m/%Y')}" if seance.date else ""

