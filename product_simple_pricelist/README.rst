.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

==========================
Product - Simple Pricelist
==========================

This module extends the functionality of pricelist to provide a wizard to
manage easily Pricelist By Products


* A "simple pricelist" has one and only one version

* A "simple pricelist" has one item based on product


Configuration
=============

To configure this module, you need to:

* Go to Point of Sale / Configuration / Sectors

* Create your PoS Sectors

* A pricelist has now a new boolean field : ```simple_pricelist```, that
  indicates that user can use a wizard to edit the pricelist by product



* A wizard is available to edit the "simple pricelist", that allow users,
  in an editable tree view, to set price by product


* Open your Point Of Sale configurations and set sectors

.. figure:: /pos_sector/static/description/pos_config_form.png
   :width: 800 px

* Finally, edit your products and set a sector

.. figure:: /pos_sector/static/description/product_form.png
   :width: 800 px


Roadmad / Issue
---------------

* create a simple pricelist should be more intuitive or more documented

* Create a simple pricelist without creating a version will fail

Credits
=======

Contributors
------------

* Sylvain LE GAL (https://www.twitter.com/legalsylvain)

Funders
-------

The development of this module has been financially supported by:

* GRAP, Groupement Régional Alimentaire de Proximité (http://www.grap.coop)
