from odoo import api, fields, models

class ResPartner(models.Model):
    _inherit = 'res.partner'


    def action_call_from_tree_view(self):
        print("action_call_from_tree_view");

