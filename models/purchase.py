# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError

class purchase(models.Model):
    _name = 'printing.purchase'
    _description = 'Daftar Pembelian dRV Printing'
    _order = 'id desc'

    name = fields.Many2one(
        'printing.beli', 
        string='Nama Material')
    
    supplier = fields.Char(
        compute='_compute_supplier', 
        string='Supplier')
    
    @api.depends('name')
    def _compute_supplier(self):
        for record in self:
            record.supplier = record.name.supplier.name 
        
    telp = fields.Char(
        compute='_compute_telp', 
        string='No Telephone')
    
    @api.depends('name')
    def _compute_telp(self):
        for record in self:
            record.telp = record.name.supplier.phone
        
    tanggal_pesan = fields.Datetime(
        string='Tanggal Pesan',
        default=fields.Datetime.now())

    tanggal_masuk = fields.Datetime(
        compute='_compute_tanggal_masuk', 
        string='Tanggal Material Datang')
    
    @api.model
    def _compute_tanggal_masuk(self):
        for record in self:
            tgl = self.env['printing.accept'].search([('name','=',record.id)]).mapped('tanggal_terima')
            if tgl :
                record.tanggal_masuk = tgl[0]
                record.accept = True
            else:
                record.tanggal_masuk = 0
                record.accept = False

    jumlah_pesan = fields.Integer(string='Jumlah Pemesanan')
    
    tagihan = fields.Float(
        compute='_compute_tagihan', 
        string='Tagihan Supplier')
    
    @api.depends('jumlah_pesan')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.name.harga * record.jumlah_pesan

    masuk_accounting = fields.Boolean(string='To Accounting')

    accept = fields.Boolean(string='Accepted')
    
    def confirm(self):
        for record in self:
            tgl = self.env['printing.accept'].search([('name','=',record.id)]).mapped('tanggal_terima')
            if tgl:
                record.masuk_accounting = True
                self.env['printing.accounting'].create({'debet':record.tagihan, 'name':record.name.name})
            else:
                raise ValidationError ('MATERIAL HAVE NOT ARRIVE')
            
    def cancel(self):
        for record in self:
            record.masuk_accounting = False
            data = self.env['printing.accounting'].search([('name','=',record.name.name)])
            data.unlink()
    
