# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class cetak(models.Model):
    _name = 'printing.jeniscetak'
    _description = 'Daftar Teknik Cetak'
    
    bahan = fields.Selection(
        string='Bahan yang Digunakan',
        selection=[("kertas","Kertas"),("stiker","Stiker"),("banner","Banner"), ("kain","Kain")],
        required=True)

    ukuran = fields.Char(
        string='Ukuran Printing',
        required=True)

    image = fields.Binary(string='Printing Pic')
    
    
class printing(models.Model):
    _name = 'printing.jenisprint'
    _description = 'Daftar Layanan Printing'
    _inherit = 'printing.jeniscetak'
    _order = 'name asc'

    name = fields.Char(
        string='Nama Printing',
        required=True)
    
    harga_cetak = fields.Integer(
        string='Harga Printing',
        required=True)

    keterangan = fields.Char(
        string='Detail Printing',
        required=True)

    active = fields.Boolean(string='Active',
                             default=True)
                            
    kirim_id = fields.Many2one(
        'printing.jeniskirim', 
        string='Teknik Pengiriman',
        required=True,
        delegate=True)
    
    @api.constrains('name')
    def _check_name(self):
        for record in self:
            name = self.env['printing.jenisprint'].search([('name','=',record.name), ('id', '!=', record.id)])
            if (name)  :
                raise ValidationError('%s sudah ada di daftar !' % (str(record.name).upper()))

    @api.onchange('bahan')
    def _onchange_bahan(self):
        if self.bahan == 'kertas':
            return {
                'warning' :{
                    'title' : 'DELIVERY',
                    'message' : 'Teknik Pengiriman Harus COD B / J&T'
                }
            }
        elif self.bahan == 'stiker':
            return {
                'warning' :{
                    'title' : 'DELIVERY',
                    'message' : 'Teknik Pengiriman Harus COD A'
                }
            }
        elif self.bahan == 'banner':
            return {
                'warning' :{
                    'title' : 'DELIVERY',
                    'message' : 'Teknik Pengiriman Harus JNE / J&T'
                }
            }
        
        elif self.bahan == 'kain':
            return {
                'warning' :{
                    'title' : 'DELIVERY',
                    'message' : 'Teknik Pengiriman Harus Anter'
                }
            }