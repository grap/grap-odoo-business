This module extend Odoo functionnalities, regarding multi companies
features, for the Barcodes module.

- It adds company field on `barcode.rule` model with according `ir.rule`
  and add the field on the related views.

This module can be interested in multi company context, if barcode
generator module are installed.

Note: when created via UI, the default company of the new `barcode.rule`
is the current company.
