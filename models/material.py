# -*- coding: utf-8 -*-

from odoo import fields, models, api

class pembelian(models.Model):
    _name = 'printing.beli'
    _description = 'Daftar Kebutuhan dRV Printing'
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
    
    stok = fields.Integer(string='Stock')
    
    supplier = fields.Many2one(
        'printing.supplier', 
        string='Supplier',
        delegate=True)
    
    telp = fields.Char(
        compute='_compute_telp', 
        string='No Telephone')
    
    @api.depends('supplier')
    def _compute_telp(self):
        for record in self:
            record.telp = record.supplier.phone