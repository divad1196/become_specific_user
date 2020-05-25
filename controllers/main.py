# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.addons.web.controllers import main as web
from odoo.http import route, request, local_redirect
from odoo.service import security
import logging
_logger = logging.getLogger(__name__)

class Home(web.Home):

    @route('/become_specific_user/become/<int:user_id>', type='http', auth='user', sitemap=False)
    def _become_user(self, user_id):
        uid = request.env.user.id
        if request.env.user._is_system() and request.env['res.partner'].browse(user_id).exists():
            uid = request.session.uid = user_id
            request.env['res.users']._invalidate_session_cache()
            request.session.session_token = security.compute_session_token(request.session, request.env)

        return local_redirect(self._login_redirect(uid), keep_hash=True)