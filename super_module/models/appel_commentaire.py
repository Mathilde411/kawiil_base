from odoo import api, fields, models


class Commentaire(models.Model):
    _name = "appel.commentaire"
    _description = "Commentaire Appel"

    timestamp = fields.Datetime(required=True)
    commentaire = fields.Text(required=True)

    name = fields.Char(readonly=True, default='Nouveau')
    partner_id = fields.Many2one("res.partner", required=True)
    seance_id = fields.Many2one("appel.seance", required=True)
    seance_state = fields.Selection(related="seance_id.state")
    seance_partner_ids = fields.Many2many(related="seance_id.partner_ids")

    @api.model_create_multi
    def create(self, vals_list):
        for val in vals_list:
            val['name'] = self.env['ir.sequence'].sudo().next_by_code("commentaire")
        return super().create(vals_list)
