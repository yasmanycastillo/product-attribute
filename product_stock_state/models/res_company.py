# Copyright 2017-Today GRAP (http://www.grap.coop).
# @author Sylvain LE GAL <https://twitter.com/legalsylvain>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models
from odoo.addons import decimal_precision as dp


class ResCompany(models.Model):
    _inherit = "res.company"

    stock_state_threshold = fields.Float(
        default=10, digits=dp.get_precision("Stock Threshold")
    )
