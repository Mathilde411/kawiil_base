from odoo.tests import TransactionCase, Form, tagged
from odoo.exceptions import ValidationError

@tagged('-at_install', 'post_install')
class TestSuperModule(TransactionCase):
    
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        cls.test_partner = cls.env['res.partner'].create({
            'name': 'Test',
            'date_naissance': '2000-11-04',
        })
        cls.test_partner2 = cls.env['res.partner'].create({
            'name': 'Test2',
            'date_naissance': '2000-11-04',
        })

    def test_age(self):
        self.assertEqual(self.test_partner.age, 25)

        self.test_partner.date_naissance = '1999-01-01'
        self.assertEqual(self.test_partner.age, 27)

    def test_missing_partner(self):
        f = Form(self.env['appel.seance'])
        f.date = '2026-07-17'
        f.partner_ids.add(self.test_partner)
        f.save()
        
        with self.assertRaisesRegex(ValidationError, "Il est impossible de démarrer une séance avec moins de 2 personnes."):
            f.record.action_ongoing()

        f.partner_ids.add(self.test_partner2)
        f.save()

        f.record.action_ongoing()
        

    
    