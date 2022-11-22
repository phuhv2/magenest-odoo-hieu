# -*- coding: utf-8 -*-
# from odoo import http


# class CrmSaleCustomization(http.Controller):
#     @http.route('/crm_sale_customization/crm_sale_customization', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/crm_sale_customization/crm_sale_customization/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('crm_sale_customization.listing', {
#             'root': '/crm_sale_customization/crm_sale_customization',
#             'objects': http.request.env['crm_sale_customization.crm_sale_customization'].search([]),
#         })

#     @http.route('/crm_sale_customization/crm_sale_customization/objects/<model("crm_sale_customization.crm_sale_customization"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('crm_sale_customization.object', {
#             'object': obj
#         })
