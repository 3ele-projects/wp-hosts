# -*- coding: utf-8 -*-
from odoo import http

# class Wp-hoster(http.Controller):
#     @http.route('/wp-hoster/wp-hoster/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/wp-hoster/wp-hoster/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('wp-hoster.listing', {
#             'root': '/wp-hoster/wp-hoster',
#             'objects': http.request.env['wp-hoster.wp-hoster'].search([]),
#         })

#     @http.route('/wp-hoster/wp-hoster/objects/<model("wp-hoster.wp-hoster"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('wp-hoster.object', {
#             'object': obj
#         })