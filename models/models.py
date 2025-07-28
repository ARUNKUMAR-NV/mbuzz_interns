from odoo import models, fields

class Intern(models.Model):
    _name = 'mbuzz.intern'
    _description = 'MBUZZ Intern'

    # ---- basics ----
    name        = fields.Char(string='Name', required=True)
    email       = fields.Char(string='Email')        
    phone       = fields.Char(string='Phone')
    department  = fields.Char(string='Department')

    # ---- relations ----
    mentor_id   = fields.Many2one('res.users', string='Mentor')

    # ---- workflow ----
    status = fields.Selection(
        [('pending',   'Pending'),
         ('confirmed', 'Confirmed'),
         ('done',      'Completed')],
        default='pending',
        string='Status')
    remarks = fields.Text(string='Remarks')
