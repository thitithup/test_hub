# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import re
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartnerBusinessType(models.Model):
    _name = 'res.partner.business.type'
    _description = 'Business Type'

    name = fields.Char(string="Business Type", required=1)
    note = fields.Char(string="Note")

