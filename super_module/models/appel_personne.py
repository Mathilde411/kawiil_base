from dateutil.relativedelta import relativedelta

from odoo import api, fields, models


class Personne(models.Model):
    _name = "appel.personne"
    _description = "Personne Appel"

    _unique_name = models.Constraint(
        "UNIQUE(name)",
        "Le nom doit être unique."
    )
    _no_minors = models.Constraint(
        "CHECK(age >= 18)",
        "La personne doit être majeure."
    )

    name = fields.Char(string="Nom", required=True)
    date_naissance = fields.Date(required=True)
    age = fields.Integer(compute="_compute_age", store=True)
    user_id = fields.Many2one("res.users")
    description = fields.Text()

    seance_ids = fields.Many2many("appel.seance")
    commentaire_ids = fields.One2many("appel.commentaire", "personne_id")

    seance_count = fields.Integer(compute="_compute_seance_count")

    
    def _compute_seance_count(self):
        for personne in self:
            personne.seance_count = self.env['appel.seance'].search_count([('personne_ids', 'any', [('id', '=', personne.id)])])

    @api.depends("date_naissance")
    def _compute_age(self):
        for personne in self:
            delta = relativedelta(fields.Date.today(), personne.date_naissance)
            personne.age = delta.years
        