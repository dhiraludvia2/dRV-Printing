# -*- coding: utf-8 -*-
# from odoo import http


# class DrvPrinting(http.Controller):
#     @http.route('/drv_printing/drv_printing/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/drv_printing/drv_printing/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('drv_printing.listing', {
#             'root': '/drv_printing/drv_printing',
#             'objects': http.request.env['drv_printing.drv_printing'].search([]),
#         })

#     @http.route('/drv_printing/drv_printing/objects/<model("drv_printing.drv_printing"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('drv_printing.object', {
#             'object': obj
#         })
