# -*- coding: utf-8 -*-

from datetime import date, datetime
import json
from odoo import http
from odoo.http import Response, request


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        return super().default(obj)


class PimController(http.Controller):

    @http.route('/get_attribute_data', auth='public', type='http', methods=['GET'])
    def get_attribute_data(self):
        attribute_groups = request.env['pim.attribute_group'].search_read([], [
        ])
        attributes = request.env['pim.attribute'].search_read([], [])
        attribute_tabs = request.env['pim.attribute_tab'].search_read([], [])

        attribute_data = {
            'attribute_groups': attribute_groups,
            'attributes': attributes,
            'attribute_tabs': attribute_tabs
        }

        return Response(CustomJSONEncoder().encode(attribute_data), headers=[('Content-Type', 'application/json')])
