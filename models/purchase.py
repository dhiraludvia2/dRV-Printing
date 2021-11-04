# -*- coding: utf-8 -*-

from odoo import fields, models, api

class pembelian(models.Model):
    _name = 'printing.beli'
    _description = 'Daftar Pembelian dRV Printing'
    _order = 'id desc'

    name = fields.Char(
        string='Nama Alat & Bahan',
        required=True)

    harga = fields.Integer(
        string='Harga Satuan',
        required=True)
    
    pengguna = fields.Char(
        string='Unit Pengguna',
        required=True)
    
    supplier = fields.Many2one(
        'printing.supplier', 
        string='Supplier',
        delegate=True)