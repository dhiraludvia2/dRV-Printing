# -*- coding: utf-8 -*-
from odoo import http, models, fields
from odoo.http import request
import json


class drvPrinting(http.Controller):
    @http.route('/stationary', auth='public')
    def get_stationary(self, **kwargs):
        stationary = request.env['printing.jenisbarang'].search([])
        value = []
        for atk in stationary:
            value.append({
                'nama stationary' : atk.name,
                'harga per kg' : atk.harga_atk,
                'satuan' : atk.satuan
            })
        return json.dumps(value)
    

    @http.route('/printing', auth='public')
    def get_printing(self, **kwargs):
        printing = request.env['printing.jenisprint'].search([])
        value = []
        for p in printing:
            value.append({
                'nama printing' : p.name,
                'bahan printng' : p.bahan,
                'ukuran printng' : p.ukuran,
                'harga printing' : p.harga_cetak
            })
        return json.dumps(value)
    

    @http.route('/kirim', auth='public')
    def get_kirim(self, **kwargs):
        kirim = request.env['printing.jeniskirim'].search([])
        value = []
        for k in kirim:
            value.append({
                'teknik kirim' : k.name,
                'teknik kemas' : k.packaging,
                'berat kemas' : k.berat,
                'wilayah' : k.wilayah
            })
        return json.dumps(value)


