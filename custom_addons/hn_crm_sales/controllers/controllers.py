# -*- coding: utf-8 -*-
# from odoo import http


# class HnCrmSales(http.Controller):
#     @http.route('/hn_crm_sales/hn_crm_sales', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hn_crm_sales/hn_crm_sales/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hn_crm_sales.listing', {
#             'root': '/hn_crm_sales/hn_crm_sales',
#             'objects': http.request.env['hn_crm_sales.hn_crm_sales'].search([]),
#         })

#     @http.route('/hn_crm_sales/hn_crm_sales/objects/<model("hn_crm_sales.hn_crm_sales"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hn_crm_sales.object', {
#             'object': obj
#         })
