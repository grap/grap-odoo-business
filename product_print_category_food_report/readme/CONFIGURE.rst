Barcodes
~~~~~~~~~~~~

Report use barcode image handle `directly by Odoo <https://www.odoo.com/documentation/12.0/reference/reports.html#barcodes>`_
To make it wortk in your report :

1. Update wkhtmltopdf to version 0.12.5
2. Add new system parameter : ``Key: web.base.url.freeze Value: True``
3. Change your report definition by using web_basic_layout ``<template> <t t-call="web.basic_layout">your things</t> </template>``


For your css
~~~~~~~~~~~~

To use custom css in report, we can use inline css or externalize css file (even scss).
For this purpose, add your css file in web.report_assets_common

``<template id="id_css_for_my_report" inherit_id="web.report_assets_common"> <xpath expr="." position="inside"> <link href="/product_print_category_food_report/static/css/my_css.scss" rel="stylesheet" type="text/scss"/> </xpath> </template>``

Beware, all css file will be shared, so you can't have the same css calling rules for two differents results.
You can use scss nesting for that purpose.
