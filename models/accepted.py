# -*- coding: utf-8 -*-

from odoo import fields, models, api
    
    
class accepted(models.Model):
    _name = 'printing.accept'
    _description = 'Daftar Penerimaaan Material'

    name = fields.Many2one(
        'printing.purchase', 
        string='Nama Material',
        domain = "[('accept','=',False)]")
    
    tanggal_pesan = fields.Char(
        compute='_compute_tanggal_pesan', 
        string='Tanggal Pemesanan')
    
    @api.depends('name')
    def _compute_tanggal_pesan(self):
        for record in self:
            record.tanggal_pesan = record.name.tanggal_pesan
        
    tanggal_terima = fields.Datetime(
        string='Tanggal Penerimaan Material',
        default=fields.Datetime.now())
    
    tagihan = fields.Float(
        compute='_compute_tagihan', 
        string='Tagihan Supplier')
    
    @api.depends('name')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.name.tagihan
    
    supplier = fields.Char(
        compute='_compute_supplier', 
        string='Supplier')
    
    @api.depends('name')
    def _compute_supplier(self):
        for record in self:
            record.supplier = record.name.supplier