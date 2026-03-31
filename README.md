
<!-- /!\ Non OCA Context : Set here the badge of your runbot / runboat instance. -->
[![Pre-commit Status](https://github.com/grap/grap-odoo-business/actions/workflows/pre-commit.yml/badge.svg?branch=16.0)](https://github.com/grap/grap-odoo-business/actions/workflows/pre-commit.yml?query=branch%3A16.0)
[![Build Status](https://github.com/grap/grap-odoo-business/actions/workflows/test.yml/badge.svg?branch=16.0)](https://github.com/grap/grap-odoo-business/actions/workflows/test.yml?query=branch%3A16.0)
[![codecov](https://codecov.io/gh/grap/grap-odoo-business/branch/16.0/graph/badge.svg)](https://codecov.io/gh/grap/grap-odoo-business)
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
[account_accountant_simple_settings](account_accountant_simple_settings/) | 16.0.1.1.2 | <a href='https://github.com/legalsylvain'><img src='https://github.com/legalsylvain.png' width='32' height='32' style='border-radius:50%;' alt='legalsylvain'/></a> | Allow accountants to make some simple accounting configuration without having administration rights.
[account_invoice_supplierinfo_update_standard_price](account_invoice_supplierinfo_update_standard_price/) | 16.0.1.0.3 |  | In the supplier invoice, automatically update all products whose standard price on the line is different from the product standard price
[account_move_change_number](account_move_change_number/) | 16.0.1.1.1 |  | Allow special user to rename account move
[barcode_rule_per_company](barcode_rule_per_company/) | 16.0.1.0.2 |  | Barcodes Rule Per Company
[hr_direct_address_home](hr_direct_address_home/) | 16.0.1.0.5 |  | Prevent creation of many home partners at employee level.
[mrp_bom_product_allergen](mrp_bom_product_allergen/) | 16.0.1.0.3 |  | Handle Product allergens on MRP BoM and BoM Lines.
[mrp_product_price_quick_menus](mrp_product_price_quick_menus/) | 16.0.1.2.1 |  | Adds menus to help manage price between BoMs and Products.
[partner_distribution_channel_criterion](partner_distribution_channel_criterion/) | 16.0.1.0.1 |  | Partner Distribution Channel Criterion
[partner_hide_technical_abstract](partner_hide_technical_abstract/) | 16.0.2.0.2 |  | Technical module, used to to Hide partners created when creating other items in Odoo
[partner_hide_technical_company](partner_hide_technical_company/) | 16.0.2.0.2 |  | Hide partners created when creating companies.
[partner_hide_technical_employee](partner_hide_technical_employee/) | 16.0.2.0.2 |  | Hide partners created when creating employees.
[partner_hide_technical_fix_calendar](partner_hide_technical_fix_calendar/) | 16.0.2.0.2 |  | Glue module with calendar, to Hide partners created when creating elements.
[partner_hide_technical_fix_calendar_test](partner_hide_technical_fix_calendar_test/) | 16.0.2.0.2 |  | Test module
[partner_hide_technical_user](partner_hide_technical_user/) | 16.0.2.0.2 |  | Hide partners created when creating users.
[product_food](product_food/) | 16.0.1.1.2 |  | Products - Food Informations
[product_food_certification](product_food_certification/) | 16.0.1.0.2 |  | Products - Food Certification Informations
[product_food_certification_account](product_food_certification_account/) | 16.0.1.0.2 |  | Product - Food Certification Informations - Account
[product_food_certification_sale](product_food_certification_sale/) | 16.0.1.0.2 |  | Product - Food Certification Informations - Sale
[product_food_certification_stock](product_food_certification_stock/) | 16.0.1.0.2 |  | Product - Food Certification Informations - Stock
[product_label](product_label/) | 16.0.2.0.4 | <a href='https://github.com/legalsylvain'><img src='https://github.com/legalsylvain.png' width='32' height='32' style='border-radius:50%;' alt='legalsylvain'/></a> <a href='https://github.com/quentinDupont'><img src='https://github.com/quentinDupont.png' width='32' height='32' style='border-radius:50%;' alt='quentinDupont'/></a> | Product Labels
[product_label_mrp](product_label_mrp/) | 16.0.1.1.2 | <a href='https://github.com/quentinDupont'><img src='https://github.com/quentinDupont.png' width='32' height='32' style='border-radius:50%;' alt='quentinDupont'/></a> | Adds labels in MRP BoMs
[product_print_category_food_report](product_print_category_food_report/) | 16.0.1.1.2 |  | Food report like pricetags
[product_standard_price_change_date](product_standard_price_change_date/) | 16.0.1.0.2 |  | Adds Date field every time Product Standard Price change.
[recurring_consignment](recurring_consignment/) | 16.0.2.4.1 |  | Sale - Handle Recurring Consignments
[recurring_consignment_pos](recurring_consignment_pos/) | 16.0.1.2.1 |  | Glue module for Recurring Consignment and PoS modules
[recurring_consignment_purchase](recurring_consignment_purchase/) | 16.0.1.1.1 |  | Glue module for Recurring Consignment and Purchase modules
[sale_eshop](sale_eshop/) | 16.0.1.4.2 |  | Allow connection to Odoo eShop Project
[sale_recovery_moment](sale_recovery_moment/) | 16.0.2.2.1 |  | Manage Recovery Moments and Places for Sale Order

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
* [odoo-addons-driver](https://github.com/grap/odoo-addons-driver)
