# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import models, fields

class AccountCtaCte(models.Model):
    _name = 'account.cta.cte'
    _description = 'Account CTA CTE'

    name = fields.Char(string='Nombre', required=True)
    creation_date = fields.Date(string='Fecha de Creación')
    balance = fields.Float(string='Saldo')
    description = fields.Text(string='Descripción')


    def action_print_report(self):
        # Obtener todos los registros seleccionados
        docs = self.env['account.cta.cte'].search([])

        date = datetime.now().strftime('%d/%m/%Y')

        data = {
            'date': date
        }

        return self.env.ref('account_cta_cte.action_account_cta_cte_report').report_action(docs)