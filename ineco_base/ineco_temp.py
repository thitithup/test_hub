# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class InecoTemp(models.Model):
    _name = 'ineco.temp'
    _description = 'Temp Class'

    name = fields.Char(string='Description', required=True)