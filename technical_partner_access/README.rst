=========================
Technical Partners Access
=========================

.. 
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! This file is generated by oca-gen-addon-readme !!
   !! changes will be overwritten.                   !!
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
   !! source digest: sha256:939f70ccfe92e91e3a60432c5c3d22a40e08db489364ab0e455e5843c103aff5
   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :target: https://odoo-community.org/page/development-status
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/licence-AGPL--3-blue.png
    :target: http://www.gnu.org/licenses/agpl-3.0-standalone.html
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-grap%2Fgrap--odoo--business-lightgray.png?logo=github
    :target: https://github.com/grap/grap-odoo-business/tree/12.0/technical_partner_access
    :alt: grap/grap-odoo-business

|badge1| |badge2| |badge3|

In Odoo, a user has a partner associated. This feature is great to manage
commun fields, but generate some non desired behaviours in some multi company
cases:

If a user has multi company access, the company of the associated partner will
change when the user change company. So the associated partner will be
"available or not", depending of user configuration. This generates error
access.

With this module:

* the users partners will not be accessible by default.
  This will force saler / purchaser to create new partner
  (if the user is a customer or a supplier too)

* the users partners will have no company, this will fix all bug access

* the companies partners will not be accessible by default.
  This will force saler / purchaser to create new partner
  (if the cpmpany is a customer or a supplier too)


**Technically**

All partners associated to a user:

* have ``company_id`` empty
* have a field ``is_odoo_user`` checked
* can be searched, only if ``show_odoo_user=True`` is in the context

All partners associated to a company:

* have a field ``is_odoo_company`` checked
* can be search, only if ``show_odoo_company=True`` is in the context


.. figure:: https://raw.githubusercontent.com/grap/grap-odoo-business/12.0/technical_partner_access/static/description/res_partner_form.png

Only members of 'Administration / Access Rights' can update those partners.

**Table of contents**

.. contents::
   :local:

Bug Tracker
===========

Bugs are tracked on `GitHub Issues <https://github.com/grap/grap-odoo-business/issues>`_.
In case of trouble, please check there if your issue has already been reported.
If you spotted it first, help us to smash it by providing a detailed and welcomed
`feedback <https://github.com/grap/grap-odoo-business/issues/new?body=module:%20technical_partner_access%0Aversion:%2012.0%0A%0A**Steps%20to%20reproduce**%0A-%20...%0A%0A**Current%20behavior**%0A%0A**Expected%20behavior**>`_.

Do not contact contributors directly about support or help with technical issues.

Credits
=======

Authors
~~~~~~~

* GRAP

Contributors
~~~~~~~~~~~~

* Sylvain LE GAL (https://www.twitter.com/legalsylvain)
* Quentin Dupont <quentin.dupont@grap.coop>

Maintainers
~~~~~~~~~~~

This module is part of the `grap/grap-odoo-business <https://github.com/grap/grap-odoo-business/tree/12.0/technical_partner_access>`_ project on GitHub.

You are welcome to contribute.
