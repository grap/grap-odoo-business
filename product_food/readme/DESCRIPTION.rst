This module extends the functionality of sale module to support food features.

It provides the new model ``certifier.organization``.
It also adds many fiels on product models. (templates and variants)

* ``is_alimentary``, boolean for analysis purpose.
* ``certifier_organization_id``
* ``is_uncertifiable`` for alimentary products that can not be certifiable.
  (like products that come from the sea)
* ``best_before_date_day`` that mentions for how many days a product can
  be eaten, after having packed. (for cheese, meats, etc.)
* ``is_alcohol``, boolean to mention if the product contains alcohol.
* ``origin_type`` to mention if ingredients come from EU or not.
* ``ingredients`` and ``allergens``. (free texts).

Alls the fields are defined on ``product.product`` model and can be set also
on ``product.template`` models, in a mono variant context.
