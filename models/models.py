# -*- coding: utf-8 -*-

from odoo import models, fields, api

class wp_instance_hosts(models.Model):
    _name = 'wp_instance.wp_hosts'

    name = fields.Char()
    description = fields.Text()
    user = fields.Char(string='user')
    host = fields.Char(string='host')
    ssh_port = fields.Integer(string='Port')
    wp_cli_path = fields.Integer(string='wp_cli_path')
    wp_instances = fields.One2many('wp_instance.wp_core', 'wp_hosts')


class wp_instance_core_inherit(models.Model):
    _inherit = 'wp_instance.wp_core'

    name = fields.Char()
    description = fields.Text()
    user = fields.Char(string='user')
    host = fields.Char(string='host')
    ssh_port = fields.Integer(string='Port')
    wp_cli_path = fields.Char(string='wp_cli_path')
    wp_hosts = fields.Many2one('wp_instance.wp_hosts', 'wp_instances')
