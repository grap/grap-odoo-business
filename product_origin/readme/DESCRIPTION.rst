This module extends the functionality of Product module to support product origins.
It adds on product and product variants models the following fields:

* Production Group Country
* Production Country
* Production State
* Production Complement (free text)
* Maker name (usefull, if different from the supplier name, that can occures
  if the supplier is a wholesaler)

The fields are defined on ``product.product`` model and can be set also
on ``product.template`` models, in a mono variant context.
