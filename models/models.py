# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)
class wp_instance_hosts(models.Model):
    _name = 'wp_instance.wp_hosts'

    name = fields.Char()
    description = fields.Text()
    user = fields.Char(string='user')
    host = fields.Char(string='host')
    ssh_port = fields.Integer(string='Port')
    wp_cli_path = fields.Char(string='wp_cli_path')
    wp_instances = fields.One2many('wp_instance.wp_core', 'wp_hosts')
    partner = fields.Many2one('res.partner')

class wp_instance_core_inherit(models.Model):
    _inherit = 'wp_instance.wp_core'
    wp_hosts = fields.Many2one('wp_instance.wp_hosts', 'Hoster')
    
    @api.multi
    def backup_data(self):
        data_set = []
        for record in self:
            data = {}
            data['wp_host']= record['wp_hosts']['host']
            data['user']= record['wp_hosts']['user']
            data['wp_cli_path']= record['wp_hosts']['wp_cli_path']
            data['port']= record['wp_hosts']['ssh_port']
            data['wp_path']= record['wp_path']
            data['sql_path']= record['sql_path']
            data_set.append(data)
        _logger.info(data_set)     
        return data_set
