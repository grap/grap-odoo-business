.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

=========
Sale Food
=========

This module extends the functionality of sale module to support food features.

It provides new food concepts like

* labels ``product.label`` that can be associated to products
* certifier organizations ``certifier.organization`` that can be associated to
  the companies

It add somes extra fields on product to handle origin, makers, etc and
let the possibility to the user to make a notation of the product regarding
ethical concepts (social, agroecological, etc.)

Configuration
=============

To configure this module, you need to:

* Go to 'Sale' / 'Configuration' / 'Food Sales' / 'Labels'
* create your custom labels

.. figure:: /sale_food/description/product_label_kanban.png
   :width: 600 px

then

* Go to 'Sale' / 'Configuration' / 'Food Sales' / 'Certifier Organizations'
* Configure your organizations

.. figure:: /sale_food/description/certifier_organization_tree.png
   :width: 600 px

then

* Go to 'Sale' / 'Configuration' / 'Product categories and attributes' / 'Product Categories'
* Configure your categories, checking if the categories contains or not
  food products by default

.. figure:: /sale_food/description/product_category_form.png
   :width: 600 px

Usage
=====

To use this module, you need to:

* Go to to your product form
* check 'Is food' Checkbox

.. figure:: /sale_food/description/product_product_form_1.png
   :width: 600 px

* tip the food information, in the new tab

.. figure:: /sale_food/description/product_product_form_2.png
   :width: 800 px

.. figure:: /sale_food/description/product_product_form_3.png
   :width: 800 px

Known issues / Roadmap
======================

* For the time being, some concept are associated to the ``product.product``
  model, and should be associated better to the ``product.template`` model.

* It could be great to have the possibility to manage the certification
  document that provide certification organization with the following model
  ``res.company.certification`` and the fields ``company_id``,
  ``organization_id``, ``date_start``, ``date_end``

* In the same way, it could be great to have the possibility to store
  the certification document of each supplier with the following model
  ``res.partner.certification`` and the fields ``partner_id``,
  ``organization_id``, ``date_start``, ``date_end``

Credits
=======

Contributors
------------

* Julien WESTE
* Sylvain LE GAL (https://www.twitter.com/legalsylvain)

Do not contact contributors directly about support or help with technical issues.

Funders
-------

The development of this module has been financially supported by:

* GRAP, Groupement Régional Alimentaire de Proximité (http://www.grap.coop)
