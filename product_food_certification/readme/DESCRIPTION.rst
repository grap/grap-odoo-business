* Add a Selection field ``ingredient_origin_type`` on product model,
  that mention if the ingredients of the product come from EU and / or not
  from EU.

* Provides a new model ``certifier.organization``.

* It also adds many fiels on product models. (templates and variants)
    * ``certifier_organization_id``
    * ``is_uncertifiable`` for alimentary products that can not be certifiable.
      (like products that come from the sea)
