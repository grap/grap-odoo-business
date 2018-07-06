.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

============================================================
Purchase - define the package of products the supplier sells
============================================================


This module extends the functionality of purchase module to support package
quantity.

Functionnality:
---------------
In the product supplierinfo, add a "Qty per Package" field to register how many
purchase UoM of the product there are in the package the supplier uses.
All purchase lines for this product+supplier must have a quantity that is a
multiple of that package quantity.

For example:
I purchase beer bootles.
The supplier sells them with a price per unit, thus the purchase UoM is PCE.
But the supplier put them in 6pcs boxes, and I have to buy a multiple of 6.

Installation
============

You should initialize the values of your package Quantity of your products.

Configuration
=============

To configure this module, you need to:

TODO

* Go to ...

.. figure:: /path/to/local/image.png
   :width: 800 px


Credits
=======

Contributors
------------

* Julien WESTE
* Sylvain LE GAL <https://twitter.com/legalsylvain>

Funders
-------


* GRAP, Groupement Régional Alimentaire de Proximité <http://www.grap.coop>
