# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models

class ResUsers(models.Model):
    _inherit = 'res.users'

    def action_become_active_user(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': "/become_specific_user/become/{user_id}".format(
                user_id=self.id,
            ),
        }