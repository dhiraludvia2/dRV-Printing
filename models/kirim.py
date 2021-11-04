# -*- coding: utf-8 -*-

from odoo import models, fields, api


class kirim(models.Model):
    _name = 'printing.jeniskirim'
    _description = 'Daftar Teknik Kirim'
    _order = 'name asc'

    name = fields.Selection(
        [("cod a","COD A"),("cod b","COD B"),("jne","JNE"),("j&t","J&T"),("anter","Anter")], 
        string='Teknik Pengiriman',
        required=True)
    
    packaging = fields.Selection(
        [("plastik","Plastik"),("bubble wrap","Bubble wrap"),("kardus","Kardus")], 
        string='Teknik Pengemasan',
        required=True)
    
    berat = fields.Selection(
        [("5","5 kg"),("10","10 kg"),("15","15 kg")], 
        string='Berat Pengemasan Max')
    
    wilayah = fields.Char(string='Jangkauan Wilayah Pengiriman')
    
    ket_kirim = fields.Char(
        string='Detail Delivery',
        required=True)

    active = fields.Boolean(string='Active',
                             default=True)
    
    models_id = fields.One2many(
        comodel_name='printing.jenisprint', 
        inverse_name='kirim_id', 
        string='Data Teknik Pengiriman Printing')
    
    models2_id = fields.One2many(
        comodel_name='printing.jenisbarang', 
        inverse_name='kirim2_id', 
        string='Data Teknik Pengiriman Stationary')
    
    pegawai_id = fields.Many2one(
        comodel_name='res.partner', 
        string='Kurir',
        domain="[('is_pegawainya','ilike',True)]")
    
    
    