from odoo import models, fields, api

class partner(models.Model):

    _inherit = 'res.partner'
    
    
    is_pegawainya = fields.Boolean(string='Pegawai', 
                                default=False)
    is_customernya = fields.Boolean(string='Customer', 
                                default=False)    