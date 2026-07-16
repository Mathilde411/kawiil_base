from odoo import api, fields, models


class Commentaire(models.Model):
    _name = "appel.commentaire"
    _description = "Commentaire Appel"

    timestamp = fields.Datetime(required=True)
    commentaire = fields.Text(required=True)

    name = fields.Char(readonly=True, default='Nouveau')
    personne_id = fields.Many2one("appel.personne", required=True)
    seance_id = fields.Many2one("appel.seance", required=True)
    seance_state = fields.Selection(related="seance_id.state")
    seance_personne_ids = fields.Many2many(related="seance_id.personne_ids")

    @api.model_create_multi
    def create(self, vals_list):
        for val in vals_list:
            val['name'] = self.env['ir.sequence'].sudo().next_by_code("commentaire")
        return super().create(vals_list)
