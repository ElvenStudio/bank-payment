# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2018 Elvenstudio S.N.C. (<http://www.elvenstudio.it>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################


from openerp.osv import osv


class AccountPaymentPopulateStatement(osv.osv_memory):
    _inherit = "account.payment.populate.statement"

    def _prepare_statement_line_vals(self, cr, uid, payment_line, amount, statement, context=None):
        line_vals = super(AccountPaymentPopulateStatement, self)._prepare_statement_line_vals(
            cr, uid, payment_line, amount, statement, context=context)

        if payment_line.order_id.payment_order_type == 'debit':
            line_vals['amount'] = amount
            if payment_line.bank_id:
                line_vals['bank_account_id'] = payment_line.bank_id.id

        return line_vals
