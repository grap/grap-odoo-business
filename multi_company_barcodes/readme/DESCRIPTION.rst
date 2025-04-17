This module extend Odoo functionnalities, regarding multi companies features,
for the Barcodes module.

* It adds company field on ``barcode.nomenclature`` model and it related ``barcode.rule``
  model, with according ``ir.rule``.

* It adds company fields on the tree, form and search views, of each model
  if this field is not available.

* It creates two new models ``barcode.nomenclature.template`` and barcode.rule.template``
  that will be used each time a new company is created, to create new nomenclature for
  the new company, based on the template datas.
