# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Bluestar Solutions Sàrl (<http://www.blues2.ch>).
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

{
    'name': 'Project Timesheet Fix',
    'version': 'master',
    "category" : 'Bluestar/Generic module',
    'complexity': "easy",
    'description': """
Use various user group dependent rights on project task work
============================================================

In the original Project Timesheet module, if a user has update rights on one work but not on all the works of a task, 
he can't update his work because OpenERP triggers a write operation on all the task works when the user saves the task. 
This module fixes this problem by triggering the write call on task works with admin user 
if and only if there is no change on the task works. Only task works with updated value(s) 
will be written with the current logged user. If the user only updates task works on whose he has update rights, 
he can save the task. If he tries to update a task work without having rights on it, the original rights exception is triggered.    
    """,
    'author': 'Bluestar Solutions Sàrl',
    'website': 'http://www.blues2.ch',
    'depends': ['project',
                'project_timesheet',
                ],
    'data': [],
    'init_xml': [],
    'update_xml': [],
    'css': [],
    'js': [],
    'qweb': [], 
    'demo_xml': [],
    'test': [],
    'installable': True,
    'application': False,
    'auto_install': False,
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
