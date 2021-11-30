from odoo import api, fields, models


class accounting(models.Model):
    _name = 'printing.accounting'
    _description = 'Data Accounting dRV Printing'
    _order = 'id asc'

    name = fields.Char(string='Nama')

    date = fields.Datetime(
        string='Tanggal Masuk', 
        default = fields.Datetime.now())
    
    debet = fields.Float(string='Debet')
    
    kredit = fields.Float(string='Kredit')
    
    saldo = fields.Float(
        compute='_compute_saldo', 
        string='Saldo',
        required=False)
    
    @api.depends('debet','kredit')
    def _compute_saldo(self):
        for record in self:
            prev = self.search_read([('id','<',record.id)], limit=1, order='id desc')
            prev_saldo = prev[0]['saldo'] if prev else 0
            record.saldo = prev_saldo + record.kredit - record.debet