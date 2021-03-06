# -*- coding: utf-8 -*-

from odoo import fields, models, api
from odoo.exceptions import ValidationError

class order(models.Model):
    _name = 'printing.order'
    _description = 'Daftar Order dRV Printing'
    _order = 'id desc'

    name = fields.Many2one(
        comodel_name='res.partner', 
        string='Customer',
        domain = "[('is_customernya','=',True)]",
        delegate=True)
    
    telp = fields.Char(
        compute='_compute_telp', 
        string='No Telephone')
    
    @api.depends('name')
    def _compute_telp(self):
        for record in self:
            record.telp = record.name.phone

    tanggal_pesan = fields.Datetime(
        string='Tanggal Pesanan',
        default=fields.Datetime.now)
    
    tanggal_selesai = fields.Datetime(
        string='Tanggal Terkirim',
        compute='_compute_tanggal_selesai')
    
    @api.model
    def _compute_tanggal_selesai(self):
        for record in self:
            tgl = self.env['printing.delivered'].search([('name','=',record.id)]).mapped('tgl_selesai')
            if tgl:
                record.tanggal_selesai = tgl[0]
                record.delivered = True
            else:
                record.tanggal_selesai = 0
                record.delivered = False

    detailorder_ids = fields.One2many(
        comodel_name='printing.detailorderatk', 
        inverse_name='order_id', 
        string='Detail Order')
    
    detailorder2_ids = fields.One2many(
        comodel_name='printing.detailorderprint', 
        inverse_name='order2_id', 
        string='Detail Order')

    delivered_ids = fields.One2many(
        'printing.delivered', 
        'name', 
        string='Delivered')

    delivered = fields.Boolean(string='Delivered')
  
    jumlah_pesanan = fields.Char(
        compute='_compute_jumlah_pesanan', 
        string='Jumlah Order')
    
    @api.depends('detailorder_ids','detailorder2_ids')
    def _compute_jumlah_pesanan(self):
        for record in self:
            record.jumlah_pesanan += (len(record.detailorder_ids)+len(record.detailorder2_ids))

    total_tagihan = fields.Integer(
        compute='_compute_total_tagihan', 
        string='Total Tagihan')
    
    @api.model
    def _compute_total_tagihan(self):
        for record in self:
            total1 = sum(self.env['printing.detailorderatk'].search([('order_id','=',record.id)]).mapped('jumlah_harga'))
            total2 = sum(self.env['printing.detailorderprint'].search([('order2_id','=',record.id)]).mapped('jumlah_harga'))
            record.total_tagihan = total1 + total2

    masuk_accounting = fields.Boolean(string='To Accounting')

    def confirm(self):
        for record in self:
            if record.tanggal_selesai:
                record.masuk_accounting = True
                self.env['printing.accounting'].create({'kredit':record.total_tagihan,'name':record.name.display_name})
            else:
                raise ValidationError('STILL DELIVER TO CUSTOMER')

    def cancel(self):
        for record in self:
            record.masuk_accounting = False
            data = self.env['printing.accounting'].search([('name','=',record.name.display_name)])
            data.unlink()


class DetailOrderStationary(models.Model):
    _name = 'printing.detailorderatk'
    _description = 'Detail Order Stationary'
    _order = 'name_atk asc'


    order_id = fields.Many2one(
        comodel_name='printing.order', 
        string='Order Stationary')

    name_atk = fields.Many2one(
        comodel_name='printing.jenisbarang', 
        string='Nama Stationary')

    harga_atk = fields.Integer(
        compute='_compute_harga_atk', 
        string='Harga Satuan')
    
    @api.depends('name_atk')
    def _compute_harga_atk(self):
        for record in self:
            record.harga_atk = record.name_atk.harga_atk
        
    banyaknya_atk = fields.Integer(string='Banyaknya')

    jumlah_harga = fields.Integer(
        compute='_compute_jumlah_harga', 
        string='Jumlah Harga Stationary')
    
    @api.depends('banyaknya_atk')
    def _compute_jumlah_harga(self):
        for record in self:
            record.jumlah_harga = record.harga_atk * record.banyaknya_atk 
    
    
    
class DetailOrderPrinting(models.Model):
    _name = 'printing.detailorderprint'
    _description = 'Detail Order Printing'
    _order = 'name_print asc'


    order2_id = fields.Many2one(
        comodel_name='printing.order', 
        string='Order Printing')

    name_print = fields.Many2one(
        comodel_name='printing.jenisprint', 
        string='Nama Printing')

    harga_print = fields.Integer(
        compute='_compute_harga_print', 
        string='Harga Satuan')
    
    @api.depends('name_print')
    def _compute_harga_print(self):
        for record in self:
            record.harga_print = record.name_print.harga_cetak
        
    banyaknya_print = fields.Integer(string='Banyaknya')

    jumlah_harga = fields.Integer(
        compute='_compute_jumlah_harga', 
        string='Jumlah Harga Printing')
    
    @api.depends('banyaknya_print')
    def _compute_jumlah_harga(self):
        for record in self:
            record.jumlah_harga = record.harga_print * record.banyaknya_print
    
    
    
    
    
    