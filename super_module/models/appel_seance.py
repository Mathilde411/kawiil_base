from odoo import api, fields, models
from odoo.exceptions import ValidationError, UserError

class Seance(models.Model):
    _name = "appel.seance"
    _description = "Séance Appel"

    name = fields.Char(compute="_compute_name")
    date = fields.Date(required=True)
    notes = fields.Text()
    user_id = fields.Many2one("res.users")
    state = fields.Selection([
        ('draft', "Brouillon"),
        ('ongoing', "En Cours"),
        ('done', "Terminée"),
        ('cancel', "Anulée"),
    ], default="draft", readonly=True, copy=False, required=True)

    personne_ids = fields.Many2many("appel.personne")
    commentaire_ids = fields.One2many("appel.commentaire", "seance_id")

    @api.depends('date')
    def _compute_name(self):
        for seance in self:
            seance.name = f"Séance du {seance.date.strftime('%d/%m/%Y')}" if seance.date else ""

    @api.constrains('state', 'personne_ids')
    def _check_corum(self):
        for seance in self:
            if seance.state in ('ongoing', 'done') and len(seance.personne_ids) < 2:
                raise ValidationError("Il est impossible de démarrer une séance avec moins de 2 personnes.")

    @api.ondelete(at_uninstall=False)
    def _unlink_check_something(self):
        for seance in self:
            if seance.state in ("ongoing", "done"):
                raise UserError("Il est impossible de supprimer une déance démarrée.")

    def action_ongoing(self):
        self.state = 'ongoing'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'

