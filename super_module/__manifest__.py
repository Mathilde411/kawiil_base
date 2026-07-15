{
    "name": "Super Module",
    "summary": "Super Module créé pendant le deuxième session.",
    "category": "Custom/Super",
    "author": "MEPL",
    "website": "www.odoo.com",
    "license": "OPL-1",
    "version": "19.0.1.0.0",
    "depends": [
        "stock",
    ],
    "data": [
        "data/actions.xml",
        "data/personne.xml",
        "security/groups.xml",
        "security/rules.xml",
        "security/ir.model.access.csv",
        "views/appel_personne_views.xml",
        "views/appel_seance_views.xml",
        "views/super_module_menus.xml",
    ],
    "demo": [

    ],
    "application": True,
}
