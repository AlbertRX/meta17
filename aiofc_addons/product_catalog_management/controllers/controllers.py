# -*- coding: utf-8 -*-
# from odoo import http


# class ProductCategoryManagement(http.Controller):
#     @http.route('/product_category_management/product_category_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/product_category_management/product_category_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('product_category_management.listing', {
#             'root': '/product_category_management/product_category_management',
#             'objects': http.request.env['product_category_management.product_category_management'].search([]),
#         })

#     @http.route('/product_category_management/product_category_management/objects/<model("product_category_management.product_category_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('product_category_management.object', {
#             'object': obj
#         })

