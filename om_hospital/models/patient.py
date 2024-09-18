# -*- coding: utf-8 -*-
from contextlib import nullcontext

from odoo import api, fields, models, _, tools, Command

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Patient Master"

    name = fields.Char(string="Name", required = True)
    date_of_birth = fields.Date(string="DOB")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender')

