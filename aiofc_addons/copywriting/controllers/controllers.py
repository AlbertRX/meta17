# -*- coding: utf-8 -*-
# from odoo import http


# class Copywriting(http.Controller):
#     @http.route('/copywriting/copywriting', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/copywriting/copywriting/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('copywriting.listing', {
#             'root': '/copywriting/copywriting',
#             'objects': http.request.env['copywriting.copywriting'].search([]),
#         })

#     @http.route('/copywriting/copywriting/objects/<model("copywriting.copywriting"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('copywriting.object', {
#             'object': obj
#         })

