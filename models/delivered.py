from odoo import fields, models, api

class delivered (models.Model):
    _name = 'printing.delivered'
    _description = 'Delivered to Customer' 
    _order = 'id desc'

    name = fields.Many2one(
        'printing.order', 
        string='Customer',
        domain = "[('delivered','=',False)]")  
    
    tgl_pesan = fields.Char(
        compute='_compute_tgl_pesan', 
        string='Tanggal Pesanan')
    
    @api.depends('name')
    def _compute_tgl_pesan(self):
        for record in self:
            record.tgl_pesan = record.name.tanggal_pesan

    tgl_selesai = fields.Datetime(
        string='Tanggal Terkirim',
        default=fields.Datetime.now())
    
    tagihan = fields.Integer(
        compute='_compute_tagihan', 
        string='Total Tagihan',
        store=True)
    
    @api.depends('name')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.name.total_tagihan
    

