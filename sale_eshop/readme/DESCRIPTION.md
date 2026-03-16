This module is the 'odoo' part of the project Odoo eShop.

the 'client' part is available here :
<https://github.com/grap/odoo-eshop>

## eShop Categories

Add a new model `eshop.category` to have the possibility to dispatch
products for the eshop.

![eshop_category_tree](../static/description/eshop_category_tree.png)

![eshop_category_form](../static/description/eshop_category_form.png)

## Customers

Add new fields on `res.partner` to handle authentication on the eshop.
It is maid with a couple `email` and `eshop_password`.

![res_partner_form](../static/description/res_partner_form.png)

## Products

Add new fields on `product.product` that handles display on eShop.

- 'eShop Category': category in the eShop
- 'Start date' and 'End Date' to disable temporarily the sale on the
  eShop
- 'Minimum Quantity', that will force user to buy at least that quantity
- 'Rounded Quantity', that will round quantity purchased

Furthermore, it is possible to allow consumers to buy less than the
minimum quantity, setting 'Unpack Quantity' value. In that case, a
surcharge can be applied in the field 'Unpack Surcharge'.

![product_product_form](../static/description/product_product_form.png)

## Companies

General settings are available via company form.

![res_company_form](../static/description/res_company_form.png)

The important fields are :

- 'has Eshop', that enable all the connexion
- 'eShop URL'
- 'Invalidation Cache URL', to enable invalidation cache system. (see
  below)

Some of cosmectics fields are available in a wizard, to be change by end
users.

you have to go in 'Sale' / 'Configuration' / 'eShop Sale' / 'eShop
Settings'

![wizard_res_company_eshop_setting_form](../static/description/wizard_res_company_eshop_setting_form.png)

## Other models

Furthermore, other models like `account.tax` has extra fields that will
be displayed on the eshop.

## Technical Informations

- The connection from the eShop into odoo, is made with a unique user,
  that has to be member of the group "Is eShop". Then, an extra
  authentication is available via partners.
- Some datas are cached by the eShop, to avoid useless call to odoo. So,
  if data changes, the cached should be invalidated. for that purpose,
  an extra abstract model `eshop.mixin` is available. Models
  synchronized with eShop should inherit of that model, and defined two
  values :

1. `_eshop_invalidation_type` : `single` / `multiple` to indicate if
   all the eShops should be invalidated, or only the one of the current
   object
2. `_eshop_invalidation_fields` : the list of the fields that trigger
   invalidation

## Technical override for Mollie Payment

To handle online payment, we use Mollie provider and its Odoo modules.
We need to override some functions to make it work outside Odoo website.

To sum up :
- each sale on sale_eshop has the Boolean eshop_sale=True
- When customer choose online payment, we generate a payment link (with Odoo
 core modules) for sale_order and retrieve it thanks to public custom route
 `/api/sale_generate_payment_link/`` (controller/sale_order.py)

We also need to add the info that the sale come from sale_eshop in order to go
back to sale_eshop website and not Odoo. Here is the path and overrides.

(Models payment_transaction.py | def _mollie_prepare_payment_payload() )
Add `&eshop_sale=1` to payment_data["redirectUrl"]
     |
     |
     v
(Controller payment_mollie.py | route = /payment/mollie/return | def mollie_return_from_checkout
After Mollie payment, retrieve payment_data and redirect to...
     |
     |
     v
(Controller post_processing.py route = /payment/status)
Redirect to website
