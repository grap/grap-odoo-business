This module extends Odoo Stock module to provide a wizard to easily mass edit
pickings.

It provides a wizard where user can select a product, and some method to change
product quantities massively, if the user doesn't have enough product to give
to its customers.

2 methods are implemented

* A prorata method, the wizard will redistribute fairly, reducing the quantity
  for all the moves.

.. figure:: ../static/description/wizard_form_pro_rata.png

* A fifo method, the wizard will reduce the quantity of the last pickings.

.. figure:: ../static/description/wizard_form_fifo.png
