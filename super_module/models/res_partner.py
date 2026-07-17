from odoo import api, models, fields
from dateutil.relativedelta import relativedelta

class ResPartner(models.Model):
    _inherit = 'res.partner'

    date_naissance = fields.Date(required=True)
    age = fields.Integer(compute="_compute_age", store=True)

    seance_ids = fields.Many2many("appel.seance")
    seance_count = fields.Integer(compute="_compute_seance_count")
    
    commentaire_ids = fields.One2many("appel.commentaire", "partner_id")

    @api.depends("date_naissance")
    def _compute_age(self):
        for personne in self:
            delta = relativedelta(fields.Date.today(), personne.date_naissance)
            personne.age = delta.years

    @api.depends('seance_ids')
    def _compute_seance_count(self):
        for personne in self:
            personne.seance_count = len(personne.seance_ids)

    def action_open_seance(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Séances',
            'res_model': 'appel.seance',
            'view_mode': 'list,form',
            'domain': [('partner_ids', 'any', [('id', '=', self.id)])]
        }

    @api.depends('complete_name', 'email', 'vat', 'state_id', 'country_id', 'commercial_company_name', 'age')
    @api.depends_context(
        'show_address', 'partner_show_db_id',
        'show_email', 'show_vat', 'lang', 'formatted_display_name'
    )
    def _compute_display_name(self):
        super()._compute_display_name()
        for partner in self:
            partner.display_name += f" (Age {partner.age})"
        

    
