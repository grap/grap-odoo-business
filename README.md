
<!-- /!\ Non OCA Context : Set here the badge of your runbot / runboat instance. -->
[![Pre-commit Status](https://github.com/grap/grap-odoo-business/actions/workflows/pre-commit.yml/badge.svg?branch=12.0)](https://github.com/grap/grap-odoo-business/actions/workflows/pre-commit.yml?query=branch%3A12.0)
[![Build Status](https://github.com/grap/grap-odoo-business/actions/workflows/test.yml/badge.svg?branch=12.0)](https://github.com/grap/grap-odoo-business/actions/workflows/test.yml?query=branch%3A12.0)
[![codecov](https://codecov.io/gh/grap/grap-odoo-business/branch/12.0/graph/badge.svg)](https://codecov.io/gh/grap/grap-odoo-business)
<!-- /!\ Non OCA Context : Set here the badge of your translation instance. -->

<!-- /!\ do not modify above this line -->

# Set of Odoo modules that meet the business needs of GRAP

This repository contains Odoo modules developped by the company GRAP that meet the business needs of GRAP.

<!-- /!\ do not modify below this line -->

<!-- prettier-ignore-start -->

[//]: # (addons)

Available addons
----------------
addon | version | maintainers | summary
--- | --- | --- | ---
[account_invoice_supplierinfo_update_standard_price](account_invoice_supplierinfo_update_standard_price/) | 12.0.1.1.3 |  | In the supplier invoice, automatically update all products whose standard price on the line is different from the product standard price
[account_invoice_supplierinfo_update_standard_price_test](account_invoice_supplierinfo_update_standard_price_test/) | 12.0.1.0.3 |  | Test module for the module account_invoice_supplierinfo_update_standard_price
[account_move_change_number](account_move_change_number/) | 12.0.1.1.2 |  | Allow special user to rename account move
[product_food](product_food/) | 12.0.1.1.10 |  | Products - Food Informations
[product_label](product_label/) | 12.0.1.1.5 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) [![quentinDupont](https://github.com/quentinDupont.png?size=30px)](https://github.com/quentinDupont) | Product Labels
[product_label_account](product_label_account/) | 12.0.1.1.4 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) [![quentinDupont](https://github.com/quentinDupont.png?size=30px)](https://github.com/quentinDupont) | Product Labels (Invoice Glue Module)
[product_label_sale](product_label_sale/) | 12.0.1.1.4 | [![legalsylvain](https://github.com/legalsylvain.png?size=30px)](https://github.com/legalsylvain) [![quentinDupont](https://github.com/quentinDupont.png?size=30px)](https://github.com/quentinDupont) | Product Labels (Sale Glue Module)
[product_notation](product_notation/) | 12.0.3.1.1 |  | Product Notation
[product_origin](product_origin/) | 12.0.1.1.5 |  | Origin for Products
[product_origin_l10n_fr_department](product_origin_l10n_fr_department/) | 12.0.1.1.1 |  | Origin Information for Products (French Departments)
[product_print_category_food_report](product_print_category_food_report/) | 12.0.1.1.7 |  | Food report like pricetags
[product_to_scale_bizerba](product_to_scale_bizerba/) | 12.0.2.0.3 |  | Synchronize Odoo database with Retail Connect Bizerba System
[recurring_consignment](recurring_consignment/) | 12.0.2.0.1 |  | Sale - Handle Recurring Consignments
[recurring_consignment_pos](recurring_consignment_pos/) | 12.0.1.1.2 |  | Glue module for Recurring Consignment and PoS modules
[recurring_consignment_purchase](recurring_consignment_purchase/) | 12.0.1.1.4 |  | Glue module for Recurring Consignment and Purchase modules
[recurring_consignment_sale](recurring_consignment_sale/) | 12.0.1.1.2 |  | Glue module for Recurring Consignment and Sale modules
[recurring_consignment_test](recurring_consignment_test/) | 12.0.1.1.7 |  | Test module for Recurring_ Consignment Module
[sale_eshop](sale_eshop/) | 12.0.2.0.0 |  | Allow connection to Odoo eShop Project
[sale_recovery_moment](sale_recovery_moment/) | 12.0.1.2.2 |  | Manage Recovery Moments and Places for Sale Order
[stock_preparation_category](stock_preparation_category/) | 12.0.1.1.2 |  | Manage Preparation Categories for stock moves
[technical_partner_access](technical_partner_access/) | 12.0.1.2.1 |  | Limit the access of the partners created when creating companies and users.

[//]: # (end addons)

<!-- prettier-ignore-end -->

## Licenses

This repository is licensed under [AGPL-3.0](LICENSE).

However, each module can have a totally different license, as long as they adhere to GRAP
policy. Consult each module's `__manifest__.py` file, which contains a `license` key
that explains its license.

----

## About GRAP

<p align="center">
   <img src="http://www.grap.coop/wp-content/uploads/2016/11/GRAP.png" width="200"/>
</p>

GRAP, [Groupement Régional Alimentaire de Proximité](http://www.grap.coop) is a
french company which brings together activities that sale food products in the
region Rhône Alpes. We promote organic and local food, social and solidarity
economy and cooperation.

The GRAP IT Team promote Free Software and developp all the Odoo modules under
AGPL-3 Licence.

You can find all these modules here:

* on the [OCA Apps Store](https://odoo-community.org/shop?&search=GRAP)
* on the [Odoo Apps Store](https://www.odoo.com/apps/modules/browse?author=GRAP).
* on [Odoo Code Search](https://odoo-code-search.com/ocs/search?q=author%3AOCA+author%3AGRAP)

You can also take a look on the following repositories:

* [grap-odoo-incubator](https://github.com/grap/grap-odoo-incubator)
* [grap-odoo-business](https://github.com/grap/grap-odoo-business)
* [grap-odoo-business-supplier-invoice](https://github.com/grap/grap-odoo-business-supplier-invoice)
* [odoo-addons-logistics](https://github.com/grap/odoo-addons-logistics)
* [odoo-addons-cae](https://github.com/grap/odoo-addons-cae)
* [odoo-addons-intercompany-trade](https://github.com/grap/odoo-addons-intercompany-trade)
* [odoo-addons-multi-company](https://github.com/grap/odoo-addons-multi-company)
* [odoo-addons-company-wizard](https://github.com/grap/odoo-addons-company-wizard)
