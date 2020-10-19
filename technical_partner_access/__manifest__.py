# Copyright (C) 2015 - Today: GRAP (http://www.grap.coop)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'Technical Partners Access',
    'summary': "Limit the access of the partners created when creating"
    " companies and users.",
    'version': "12.0.1.0.1",
    'category': 'base',
    'author': 'GRAP',
    'website': 'http://www.grap.coop',
    'license': 'AGPL-3',
    'depends': [
        'base',
    ],
    'demo': [
        'demo/res_groups.xml',
    ],
    'post_init_hook': 'post_init_hook',
    'installable': True,
}
