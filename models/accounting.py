from odoo import api, fields, models


class accounting(models.Model):
    _name = 'printing.accounting'
    _description = 'Data Accounting dRV Printing'

    name = fields.Char(string='Nama')
    date = fields.Datetime(string='Tanggal Masuk', default = fields.Datetime.now())
    debet = fields.Float(string='Debet')
    kredit = fields.Float(string='Kredit')
    saldo = fields.Float(string='Saldo')
    