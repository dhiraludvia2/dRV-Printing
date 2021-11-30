from odoo import models, fields, api

class partner(models.Model):

    _inherit = 'res.partner'
    
    
    is_pegawainya = fields.Boolean(string='Pegawai', 
                                default=False)
    is_customernya = fields.Boolean(string='Customer', 
                                default=False)    


class supplier(models.Model):
    _name = 'printing.supplier'
    _description = 'Data Supplier'
    _order = 'name asc'

    name = fields.Char(
        string='Nama Supplier',
        required=True)
    
    alamat = fields.Char(
        string='Alamat Supplier',
        required=True)
    
    contact = fields.Char(
        string='Contact Person',
        required=True)

    phone = fields.Char(
        string='No Telephone',
        required=True)
    
    beli = fields.One2many(
        'printing.beli', 
        'supplier',
        string='Alat & Bahan Supply')