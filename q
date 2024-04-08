[33mec73084 [31mMon Apr 8 14:41:56 2024 +0200 [34mSylvain LE GAL[32m (HEAD -> 12.0-REF-ADD-product_food_certification) [m[REF] product_food : move organic_type into product_food_certification
[33mee89a11 [31mMon Apr 8 14:29:58 2024 +0200 [34mSylvain LE GAL[32m [m[REF] Move certifier.organization from product_food to product_food_certification
[33m7273fd4 [31mWed Jan 10 23:38:54 2024 +0100 [34mSylvain LE GAL[32m (legalsylvain/12.0-REF-ADD-product_food_certification, 12.0-current) [m[REF] rename product_origin_l10n_fr_department into l10n_fr_department_product_origin
[33m871d0e8 [31mWed Jan 10 23:19:04 2024 +0100 [34mSylvain LE GAL[32m [m[IMP] automatize uninstallation of obsolete module 'product_notation' and installation of new module 'product_food_certification'
[33m45f4a92 [31mWed Jan 10 23:18:28 2024 +0100 [34mSylvain LE GAL[32m [mfixup! [REM] product_food : remove allergens field, and populate allergen_ids fields
[33m281cae5 [31mWed Jan 10 23:15:36 2024 +0100 [34mSylvain LE GAL[32m [m[FIX] product_print_category_food_report : field_ids of product.print.category should refer to stored field. replace 'price_per_unit' by 'volume' and 'net_weight'
[33m3468e96 [31mWed Jan 10 00:28:38 2024 +0100 [34mSylvain LE GAL[32m [m[REF] product_food -> product_print_category_food_report : move price_per_unit field
[33m56beda8 [31mTue Jan 9 22:12:18 2024 +0100 [34mSylvain LE GAL[32m [m[REM] product_food : remove allergens field, and populate allergen_ids fields
[33mfd31bff [31mTue Jan 9 10:13:50 2024 +0100 [34mSylvain LE GAL[32m [m[FIX] pricetag_origin field depends on department_id
[33m1793e1d [31mMon Jan 8 15:21:54 2024 +0100 [34mSylvain LE GAL[32m [m[REM] Remove product_notation
[33m91cdd5f [31mMon Jan 8 14:48:52 2024 +0100 [34mSylvain LE GAL[32m [m[REF] grap_qweb_report -> product_print_category_food_report : Move 4 pricetags report into a single one module [IMP] Add tests for all pricetags reports
[33m745b089 [31mFri Jan 5 21:51:18 2024 +0100 [34mSylvain LE GAL[32m [m[REF-DATA] product_food_certification : replace various label_ids by ingredient_origin_type
[33m57d070c [31mFri Jan 5 21:16:35 2024 +0100 [34mSylvain LE GAL[32m [m[IMP] product_food_certification : Add new 'fr' key as possible value
[33m216f2f3 [31mFri Jan 5 15:55:15 2024 +0100 [34mSylvain LE GAL[32m [m[REF-DATA] product_origin/product_print_category_food_report/product_food_certification : replace country_group_id by ingredient_origin_type
[33m068a4de [31mFri Jan 5 11:59:42 2024 +0100 [34mSylvain LE GAL[32m [m[REF] Move and rename product_food / origin_type >> product_food_certification / ingredient_origin_type Note : This field unused for the time being.
[33m233d7e9 [31mFri Jan 5 11:38:30 2024 +0100 [34mSylvain LE GAL[32m [m[ADD] product_food_certification
[33mb539336 [31mSun Dec 3 21:25:22 2023 +0000 [34mGithub GRAP Bot[32m (grap/12.0, 12.0) [m[BOT] post-merge updates
[33m7748d81 [31mSun Dec 3 21:21:51 2023 +0000 [34mGithub GRAP Bot[32m [mMerge PR #142 into 12.0
[33mcc9b5a0 [31mSun Dec 3 21:16:35 2023 +0000 [34mGithub GRAP Bot[32m [m[BOT] post-merge updates
[33m1eaa43b [31mSun Dec 3 21:13:04 2023 +0000 [34mGithub GRAP Bot[32m [mMerge PR #140 into 12.0
[33m4555279 [31mThu Nov 30 22:18:02 2023 +0100 [34mSylvain LE GAL[32m (legalsylvain/12.0-IMP-359-product_food-add-fresh, 12.0-IMP-359-product_food-add-fresh) [m[IMP] product_food : add fresh status. (< 10°) for fruits and vegetables + [REF] update various translation
[33mdb12330 [31mTue Nov 21 18:57:13 2023 +0100 [34mQuentin Dupont[32m [mfix
[33m5231ea9 [31mMon Nov 20 16:53:40 2023 +0100 [34mQuentin Dupont[32m [m[ADD] Font Luciole for standardization [IMP] Organic info standardization
[33mc990be6 [31mTue Nov 21 20:17:25 2023 +0000 [34mGithub GRAP Bot[32m [m[BOT] post-merge updates
[33m0e219b9 [31mTue Nov 21 20:13:35 2023 +0000 [34mGithub GRAP Bot[32m [mMerge PR #141 into 12.0
[33m5998abe [31mTue Nov 21 21:04:16 2023 +0100 [34mSylvain LE GAL[32m (legalsylvain/12.0-REF-copier-2023-11-21, 12.0-REF-copier-2023-11-21) [m[REF] New rule : remove obsolete 'data' tag
[33med251bf [31mTue Nov 21 21:03:46 2023 +0100 [34mSylvain LE GAL[32m [m[REF] New rule remove 'string' attributes on tree view and replace colors by decoration-*
[33m75aac15 [31mTue Nov 21 20:44:13 2023 +0100 [34mSylvain LE GAL[32m [m[REF] Update copier update (2023-11-21)
[33m9b81205 [31mMon Oct 2 11:31:08 2023 +0200 [34mSylvain LE GAL[32m [m[REF] remove useless requirement
[33m9dd351a [31mMon Oct 2 08:16:12 2023 +0000 [34mGithub GRAP Bot[32m [m[UPD] README.rst
[33maf31f2c [31mMon Oct 2 08:16:10 2023 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mba0ad1f [31mMon Oct 2 08:10:28 2023 +0000 [34mGithub GRAP Bot[32m [mMerge PR #128 into 12.0
[33m0affeb5 [31mMon Sep 4 16:11:36 2023 +0200 [34mSylvain LE GAL[32m (12.0-REF-recurring_consignment-single-vat) [m[FIX] recurring_consignment : Do not use generic 467 for new vat (of non subject), reuse account of the partner
[33m59e42ce [31mMon Sep 4 15:40:32 2023 +0200 [34mSylvain LE GAL[32m [m[FIX/IMP] recurring consignment : correct group in wizard to create consignors
[33m8089840 [31mMon Aug 7 16:39:49 2023 +0200 [34mSylvain LE GAL[32m [m[REF] recurring_consignment : Improve migration script
[33m742bbb1 [31mTue Aug 1 21:33:47 2023 +0200 [34mSylvain LE GAL[32m [m[IMP] recurring_consignment : do not display vat option is the supplier is not vat subject
[33m3319f80 [31mTue Aug 1 21:33:15 2023 +0200 [34mSylvain LE GAL[32m [m[MIG] Finish migration
[33mcd21ca7 [31mMon Jun 12 09:38:17 2023 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mc75a696 [31mMon Jun 12 09:33:58 2023 +0000 [34mGithub GRAP Bot[32m [mMerge PR #138 into 12.0
[33ma813be7 [31mMon Jun 12 09:30:20 2023 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m16a4656 [31mMon Jun 12 09:30:14 2023 +0000 [34mGithub GRAP Bot[32m [mproduct_food 12.0.1.1.9
[33m89aed1b [31mMon Jun 12 09:26:05 2023 +0000 [34mGithub GRAP Bot[32m [mMerge PR #137 into 12.0
[33mc0f4150 [31mWed Feb 8 14:57:48 2023 +0100 [34mSylvain LE GAL[32m [m[REF] recurring_consignment_* : Single VAT to make consignment invoices
[33m471e4f9 [31mMon Apr 24 14:47:47 2023 +0200 [34mSylvain LE GAL[32m (12.0-449-REF-sale_eshop-use-standard-social-fields) [m[REF] sale_eshop : use standard social network fields
[33mebef50b [31mFri Apr 21 12:30:39 2023 +0200 [34mQuentin Dupont[32m [m[12.0][IMP] Add product_qty allergen tree view
[33m6a270c9 [31mTue Apr 18 13:01:43 2023 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m8af4074 [31mTue Apr 18 13:01:38 2023 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.1.9
[33mc403bb0 [31mTue Apr 18 12:56:15 2023 +0000 [34mGithub GRAP Bot[32m [mMerge PR #136 into 12.0
[33m111bcd9 [31mTue Apr 18 12:33:10 2023 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m2f29c71 [31mTue Apr 18 12:33:05 2023 +0000 [34mGithub GRAP Bot[32m [maccount_invoice_supplierinfo_update_standard_price 12.0.1.1.3
[33m0fd855c [31mTue Apr 18 12:28:03 2023 +0000 [34mGithub GRAP Bot[32m [mMerge PR #135 into 12.0
[33m1f13949 [31mTue Apr 18 12:15:22 2023 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mfbd0a79 [31mTue Apr 18 12:15:17 2023 +0000 [34mGithub GRAP Bot[32m [mproduct_origin 12.0.1.1.4
[33m8a67ae6 [31mTue Apr 18 12:09:19 2023 +0000 [34mGithub GRAP Bot[32m [mMerge PR #134 into 12.0
[33m25eea12 [31mTue Apr 18 12:08:00 2023 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m114dd80 [31mTue Apr 18 12:07:55 2023 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.1.8
[33m161c926 [31mTue Apr 18 12:01:47 2023 +0000 [34mGithub GRAP Bot[32m [mMerge PR #133 into 12.0
[33m7ff5428 [31mFri Apr 7 13:33:28 2023 +0200 [34mSylvain LE GAL[32m (12.0-860-IMP-recurring_consignment-secure-bad-dispatch-leeeets-the-sun-shiiiiiine) [m[FIX] recurring_consignment : in case of mass commission, do not affect move lines on wrong invoice
[33m9f17a54 [31mFri Apr 7 13:25:44 2023 +0200 [34mSylvain LE GAL[32m [m[IMP] recurring_consignment : Add constraint to avoid bad link between commission invoices and commissionned lines
[33m07b9cef [31mFri Apr 7 13:00:36 2023 +0200 [34mSylvain LE GAL[32m [m[IMP] recurring_consignment : display important fields on account.invoice to understand witch lines are commissionned
[33mfcd8816 [31mThu Apr 6 22:10:09 2023 +0200 [34mSylvain LE GAL[32m (12.0-343-REF-grap-odoo-business-prix-de-revient-2-cout) [m[REF] Prix de Revient -> Coût
[33m8fa499a [31mThu Apr 6 19:50:58 2023 +0200 [34mSylvain LE GAL[32m (12.0-802-IMP-product_origin-add-help-on-distribution_channel_criterion) [m[IMP] product_origin : add help on distribution_channel_criterion field
[33m94bfc64 [31mTue Mar 28 13:54:52 2023 +0200 [34mSylvain LE GAL[32m (12.0-845-ADD_grap_index-account-postgresql-perf) [m[IMP] recurring_consignment : add index on field to improve read queries
[33m53bf5de [31mTue Mar 21 11:05:37 2023 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m6ed3fec [31mTue Mar 21 11:05:31 2023 +0000 [34mGithub GRAP Bot[32m [mproduct_origin 12.0.1.1.3
[33m01d5f62 [31mTue Mar 21 11:00:14 2023 +0000 [34mGithub GRAP Bot[32m [mMerge PR #130 into 12.0
[33m47ec957 [31mFri Feb 10 17:25:18 2023 +0100 [34mSylvain LE GAL[32m [m[REF] product_origin : move attrs of distribution_channel_criterion from grap_change_views_partner to main module (product_origin)
[33m7513631 [31mSun Mar 19 13:59:18 2023 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m55f3451 [31mSun Mar 19 13:59:14 2023 +0000 [34mGithub GRAP Bot[32m [msale_eshop 12.0.1.1.7
[33m57e5694 [31mSun Mar 19 13:54:49 2023 +0000 [34mGithub GRAP Bot[32m [mMerge PR #131 into 12.0
[33md3ad509 [31mFri Mar 10 16:37:52 2023 +0100 [34mSylvain LE GAL[32m (12.0-FIX-sale_eshop-use-sudo-for-config-param) [m[FIX] sale_eshop : use sudo() to access to config parameter
[33m2699bb2 [31mFri Mar 10 16:22:01 2023 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m200f633 [31mFri Mar 10 16:15:56 2023 +0000 [34mGithub GRAP Bot[32m [mMerge PR #132 into 12.0
[33mc39398d [31mFri Mar 10 17:14:58 2023 +0100 [34mSylvain LE GAL[32m (12.0-copier-2023-03-10) [m[REF] Initialize Copier template
[33m2f356ed [31mFri Mar 10 17:08:47 2023 +0100 [34mSylvain LE GAL[32m [m[REF] Add copier answer file
[33m6fac7f9 [31mWed Feb 8 16:25:15 2023 +0000 [34mGithub GRAP Bot[32m [mMerge PR #129 into 12.0
[33mf8fc994 [31mWed Feb 8 17:16:48 2023 +0100 [34mSylvain LE GAL[32m (12.0-FIX-precommit-stuff-2023-02-08) [m[FIX] pre-commit stuff
[33m88613f3 [31mTue Jan 3 15:46:31 2023 +0000 [34mGithub GRAP Bot[32m [mMerge PR #126 into 12.0
[33m09f013c [31mTue Jan 3 15:37:20 2023 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m2244175 [31mTue Jan 3 15:37:12 2023 +0000 [34mGithub GRAP Bot[32m [msale_recovery_moment 12.0.1.2.2
[33m2b7468d [31mTue Jan 3 15:31:52 2023 +0000 [34mGithub GRAP Bot[32m [mMerge PR #121 into 12.0
[33m32a10ae [31mFri Dec 9 12:17:03 2022 +0100 [34mSylvain LE GAL[32m (12.0-REM-ref-stock_picking_report_summary) [m[REM] reference to stock_picking_report_summary as the module is now in OCA/stock-logistics-reporting
[33m9b0fd0a [31mFri Dec 9 10:39:55 2022 +0000 [34mGithub GRAP Bot[32m [mMerge PR #125 into 12.0
[33mcd8d305 [31mFri Dec 9 11:39:30 2022 +0100 [34mSylvain LE GAL[32m (12.0-REF-pin-ubuntu-20-pre-commit-test) [m[FIX] pin ubuntu 20 env in pre-commit test
[33m26fafef [31mTue Nov 15 14:28:31 2022 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m2a7fbe1 [31mTue Nov 15 14:28:23 2022 +0000 [34mGithub GRAP Bot[32m [mproduct_print_category_food_report 12.0.1.1.6
[33m61a4696 [31mTue Nov 15 14:23:56 2022 +0000 [34mGithub GRAP Bot[32m [mMerge PR #123 into 12.0
[33m12bb6f7 [31mTue Oct 11 23:29:12 2022 +0200 [34mQuentin Dupont[32m [mFR i18n
[33m735d6a2 [31mTue Oct 11 16:27:01 2022 +0200 [34mQuentin Dupont[32m [mwip labels default code and options
[33mf5a6ffe [31mTue Nov 15 13:59:06 2022 +0000 [34mGithub GRAP Bot[32m [mMerge PR #124 into 12.0
[33ma4b5c58 [31mTue Nov 15 14:45:45 2022 +0100 [34mSylvain LE GAL[32m (12.0-CI-FIX-flake-gitlab-github) [m[FIX] CI : replace gitlab by github
[33m1428d09 [31mWed Sep 28 09:04:09 2022 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mcb29bfb [31mWed Sep 28 09:04:00 2022 +0000 [34mGithub GRAP Bot[32m [msale_eshop 12.0.1.1.6
[33mfc38587 [31mWed Sep 28 08:59:14 2022 +0000 [34mGithub GRAP Bot[32m [mMerge PR #122 into 12.0
[33mb6225d7 [31mThu Sep 22 12:23:53 2022 +0200 [34mSylvain LE GAL[32m (12.0-FIX-sale_eshop-singleton-compute_eshop_url) [m[FIX] sale_eshop : call api.one function with only one item
[33m827e129 [31mMon Sep 19 12:17:47 2022 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m7829e17 [31mMon Sep 19 12:17:33 2022 +0000 [34mGithub GRAP Bot[32m [msale_eshop 12.0.1.1.5
[33me8e05ed [31mMon Sep 19 12:17:32 2022 +0000 [34mGithub GRAP Bot[32m [m[UPD] README.rst
[33m90ea2e4 [31mMon Sep 19 12:12:56 2022 +0000 [34mGithub GRAP Bot[32m [mMerge PR #120 into 12.0
[33mdda5879 [31mMon Sep 19 11:48:05 2022 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m13701c7 [31mMon Sep 19 11:47:51 2022 +0000 [34mGithub GRAP Bot[32m [msale_eshop 12.0.1.1.4
[33mcff09eb [31mMon Sep 19 11:43:03 2022 +0000 [34mGithub GRAP Bot[32m [mMerge PR #119 into 12.0
[33ma03cb65 [31mWed Sep 14 16:38:27 2022 +0200 [34mSylvain LE GAL[32m (12.0-FIX-sale_recovery_moment-sequence-global) [m[FIX] sale_recovery_moment : sequence for sale.recovery.moment and sale.recovery.moment.group should be global.
[33m1564332 [31mMon Sep 12 18:17:18 2022 +0200 [34mSylvain LE GAL[32m (12.0-IMP-sale_eshop-allow-multi-database) [m[IMP] sale_eshop : add database name in the ir_config_parameter of the sale eshop, to allow to work in a multi-database context, when server_environment_ir_config_parameter is installed
[33m7c2ad2b [31mFri Jul 29 11:44:07 2022 +0200 [34mmounasb[32m [m[FIX] model import
[33mc91373e [31mThu Jul 28 18:03:45 2022 +0200 [34mmounasb[32m [m[IMP] menu harmonisation
[33m8a4bd0e [31mThu Jul 28 18:00:15 2022 +0200 [34mmounasb[32m [m[ADD] eshop_fake_account : add elements
[33m027ea50 [31mThu Jul 28 17:53:37 2022 +0200 [34mmounasb[32m [m[ADD] sale_eshop : add new model to log bot log attempts
[33m308a9a6 [31mTue Jun 28 11:51:13 2022 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33ma1e9a24 [31mTue Jun 28 11:50:56 2022 +0000 [34mGithub GRAP Bot[32m [mproduct_label 12.0.1.1.5
[33m2bbb4ad [31mTue Jun 28 11:50:54 2022 +0000 [34mGithub GRAP Bot[32m [mproduct_label_account 12.0.1.1.4
[33mcbff8d6 [31mTue Jun 28 11:50:51 2022 +0000 [34mGithub GRAP Bot[32m [mproduct_label_sale 12.0.1.1.4
[33m99763c7 [31mTue Jun 28 11:46:18 2022 +0000 [34mGithub GRAP Bot[32m [mMerge PR #118 into 12.0
[33m226b21c [31mTue Jun 28 11:45:49 2022 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m8e9c016 [31mTue Jun 28 11:45:41 2022 +0000 [34mGithub GRAP Bot[32m [mproduct_food 12.0.1.1.8
[33m4fb9c0a [31mTue Jun 28 11:40:45 2022 +0000 [34mGithub GRAP Bot[32m [mMerge PR #117 into 12.0
[33m679f9b6 [31mFri May 20 13:09:39 2022 +0200 [34mSylvain LE GAL[32m (12.0-FIX-product_label_sale-fr-translation) [m[FIX] product_label_sale : fix translation
[33ma511970 [31mMon Apr 25 17:11:52 2022 +0200 [34mSylvain LE GAL[32m (12.0-IMP-product_food-write-product-with-alcohol) [m[IMP] product_food : set alcohol category automatically set alcohol label ; [IMP] product_food : normalize onchange name and fix missing onchange function on product template
[33m630c0ed [31mWed Apr 13 09:45:45 2022 +0000 [34mGithub GRAP Bot[32m [mMerge PR #116 into 12.0
[33m808d82a [31mWed Apr 13 11:39:42 2022 +0200 [34mSylvain LE GAL[32m (12.0-META-CI-reduce-execution) [m[META] reduce CI execution [META] bump black to 22.3.0
[33mfa2ca04 [31mTue Mar 8 11:06:34 2022 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m5295cdb [31mTue Mar 8 11:06:27 2022 +0000 [34mGithub GRAP Bot[32m [msale_recovery_moment 12.0.1.2.1
[33m2df977d [31mTue Mar 8 11:01:30 2022 +0000 [34mGithub GRAP Bot[32m [mMerge PR #113 into 12.0
[33m408d40c [31mThu Feb 17 12:07:45 2022 +0100 [34mSylvain LE GAL[32m (12.0-sale_recovery_moment-add-extra-info-picking-summary) [m[IMP] sale_recovery_moment : depends on stock_picking_report_summary and add recovery place and date on picking summary report
[33m11b2872 [31mTue Mar 8 11:00:28 2022 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mf42e3c0 [31mTue Mar 8 11:00:20 2022 +0000 [34mGithub GRAP Bot[32m [mproduct_print_category_food_report 12.0.1.1.5
[33m4102ca4 [31mTue Mar 8 10:55:23 2022 +0000 [34mGithub GRAP Bot[32m [mMerge PR #105 into 12.0
[33me4b9bbd [31mTue Mar 8 08:54:54 2022 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m841f87f [31mTue Mar 8 08:54:47 2022 +0000 [34mGithub GRAP Bot[32m [msale_recovery_moment 12.0.1.2.0
[33m0b8f99f [31mTue Mar 8 08:50:07 2022 +0000 [34mGithub GRAP Bot[32m [mMerge PR #114 into 12.0
[33m2e7099f [31mTue Mar 8 08:32:18 2022 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m5f5ebe4 [31mTue Mar 8 08:32:10 2022 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.1.7
[33m9cd1390 [31mTue Mar 8 08:32:07 2022 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_sale 12.0.1.1.2
[33m99782fa [31mTue Mar 8 08:32:04 2022 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_test 12.0.1.1.7
[33m899506a [31mTue Mar 8 08:32:01 2022 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_purchase 12.0.1.1.4
[33mcd7cdae [31mTue Mar 8 08:31:58 2022 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_pos 12.0.1.1.2
[33m7ea6c3b [31mTue Mar 8 08:26:36 2022 +0000 [34mGithub GRAP Bot[32m [mMerge PR #115 into 12.0
[33m1fb9269 [31mSun Mar 6 23:55:38 2022 +0100 [34mSylvain LE GAL[32m (12.0-FIX-recurring_consignment_pos-exclude-invoiced-pos-order-lines) [m[FR] recurring_consignment_* : update fr translation
[33mbd7cb3c [31mSun Mar 6 23:40:26 2022 +0100 [34mSylvain LE GAL[32m [m[IMP] recurring_consignment * : Add buttons to see the invoice / order lines related to a commission invoice
[33m0593306 [31mSun Mar 6 11:46:40 2022 +0100 [34mSylvain LE GAL[32m [m[REF] recurring_consigment* : refactor code
[33m3c1ee0a [31mSun Mar 6 10:20:04 2022 +0100 [34mSylvain LE GAL[32m [m[REF] recurring_consignment : move code
[33m4835e86 [31mFri Mar 4 20:52:30 2022 +0100 [34mSylvain LE GAL[32m [m[FIX] recurring_consigment : compute detail of product for invoice commission correctly in case of refund or consigned product
[33mdc8557a [31mFri Mar 4 12:42:05 2022 +0100 [34mSylvain LE GAL[32m [m[FIX] recurring_consignment_pos: exclude invoiced pos.order.lines, to avoid to multiply by 2, the sold products, in the report
[33m90b9de6 [31mThu Feb 17 17:36:00 2022 +0100 [34mSylvain LE GAL[32m [m[IMP] sale_recovery_moment : add possibility to duplicates moments
[33m4ae95cd [31mThu Feb 17 16:19:53 2022 +0100 [34mSylvain LE GAL[32m [m[META] update pre-commit file
[33m65717fc [31mThu Feb 17 16:19:41 2022 +0100 [34mSylvain LE GAL[32m [m[IMP] sale_recovery_moment : allow to duplicate many groups
[33mc085d15 [31mMon Jan 24 09:46:04 2022 +0100 [34mQuentin Dupont[32m [mRemove trigger fields useless
[33m0f579ad [31mFri Jan 21 16:47:52 2022 +0100 [34mQuentin Dupont[32m [mIMP counter changement de structure + améliorations
[33maa6ac6f [31mFri Jan 21 15:23:00 2022 +0100 [34mQuentin Dupont[32m [mPrinted field
[33md484cc7 [31mFri Jan 21 14:42:45 2022 +0100 [34mQuentin Dupont[32m [mimp minor fixes
[33mf00c315 [31mFri Jan 21 13:36:21 2022 +0000 [34mGithub GRAP Bot[32m [mMerge PR #111 into 12.0
[33m58856d3 [31mFri Jan 21 13:08:34 2022 +0000 [34mGithub GRAP Bot[32m [mMerge PR #112 into 12.0
[33m9d6e5b9 [31mFri Jan 21 14:08:06 2022 +0100 [34mSylvain LE GAL[32m [m[REF] remove obsolete oca_dependencies files
[33m9701fab [31mFri Jan 21 13:58:47 2022 +0100 [34mSylvain LE GAL[32m [m[REF] Try to simplify test-requirements.txt
[33m0917956 [31mWed Jan 19 19:45:07 2022 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mc2cd94a [31mWed Jan 19 19:44:58 2022 +0000 [34mGithub GRAP Bot[32m [mproduct_food 12.0.1.1.7
[33m050ff2e [31mWed Jan 19 19:40:21 2022 +0000 [34mGithub GRAP Bot[32m [mMerge PR #110 into 12.0
[33mbe29506 [31mWed Jan 19 20:34:31 2022 +0100 [34mSylvain LE GAL[32m [m[TEST] new CI
[33ma0f8f91 [31mWed Jan 19 20:20:41 2022 +0100 [34mSylvain LE GAL[32m [mfixup! fixup! [REF] apply new CI checks.
[33m838ea14 [31mWed Jan 19 20:18:11 2022 +0100 [34mSylvain LE GAL[32m [mfixup! [REF] apply new CI checks.
[33mb22d406 [31mWed Jan 19 14:12:24 2022 +0100 [34mSylvain LE GAL[32m [m[REF] apply new CI checks.
[33m8702f4f [31mWed Jan 19 14:06:17 2022 +0100 [34mSylvain LE GAL[32m [m[REF] [REF] Remove Travis CI. add Github actions CI.
[33mf215477 [31mWed Jan 19 19:15:22 2022 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m000557d [31mWed Jan 19 20:10:35 2022 +0100 [34mSylvain LE GAL[32m [m[REF] move recurring_consignment_fiscal_company from grap/grap-odoo-business into grap/odoo-addons-cae
[33m5b283d4 [31mWed Jan 19 13:07:54 2022 +0100 [34mQuentin Dupont[32m [mwip pleins dameliorations mineures
[33medabbd2 [31mTue Jan 18 21:56:54 2022 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m20e6f44 [31mTue Jan 18 21:56:50 2022 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_test 12.0.1.1.6
[33m728eaac [31mTue Jan 18 21:56:50 2022 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.1.6
[33me3744d5 [31mTue Jan 18 18:14:55 2022 +0000 [34mGithub GRAP Bot[32m [mMerge PR #107 into 12.0
[33mc87c71f [31mTue Jan 18 17:55:24 2022 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33ma063159 [31mTue Jan 18 17:55:19 2022 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.1.5
[33m221d52e [31mTue Jan 18 15:53:08 2022 +0100 [34mQuentin Dupont[32m [mfix
[33ma56f90b [31mTue Jan 18 14:38:28 2022 +0000 [34mGithub GRAP Bot[32m [mMerge PR #104 into 12.0
[33mec9c763 [31mFri Jan 14 10:26:05 2022 +0100 [34mSylvain LE GAL[32m [m[FIX] recurring_consignment : make standard_price null for product of consignors
[33meb3f98e [31mMon Jan 10 11:07:10 2022 +0100 [34mQuentin Dupont[32m [m[IMP] Unit product for bulk long label
[33mb58cb08 [31mThu Dec 23 11:42:37 2021 +0100 [34mSylvain LE GAL[32m [m[IMP] recurring_consignment : allow to sale product without vat
[33m6cd87e0 [31mWed Dec 22 00:36:21 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m28b1f26 [31mWed Dec 22 00:36:16 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_print_category_food_report 12.0.1.1.4
[33m8086907 [31mWed Dec 22 00:36:16 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_food 12.0.1.1.6
[33m6086adb [31mTue Dec 21 22:44:55 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #103 into 12.0
[33m3b0dd6d [31mFri Dec 10 13:40:51 2021 +0100 [34mSylvain LE GAL[32m [m[REF] product_food : depends on OCA/product-attribute/product_net_weight module
[33m3c9c9b1 [31mTue Dec 21 22:39:30 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33ma9486a8 [31mTue Dec 21 22:39:26 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.1.4
[33m98cf2f3 [31mTue Dec 21 21:14:25 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #102 into 12.0
[33m84b577f [31mTue Dec 21 21:10:34 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33md793aee [31mTue Dec 21 21:10:29 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_test 12.0.1.1.5
[33mfd359d2 [31mTue Dec 21 21:10:29 2021 +0000 [34mGithub GRAP Bot[32m [maccount_move_change_number 12.0.1.1.2
[33med73632 [31mTue Dec 21 17:41:41 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #101 into 12.0
[33mdc9ce89 [31mTue Dec 21 18:40:29 2021 +0100 [34mSylvain LE GAL[32m [m[FIX] pre-commit + bad test on recurring_consignment
[33mf29e847 [31mFri Dec 10 13:35:32 2021 +0100 [34mSylvain LE GAL[32m [m[FIX] recurring consignement : allow no tax
[33m72e2ba4 [31mFri Nov 19 11:30:46 2021 +0100 [34mSylvain LE GAL[32m [m [FIX] account_move_change_number : correctly change number also for refund. (without that patch a VTAV/ is renamed into VT/
[33m26e1471 [31mTue Nov 2 10:25:28 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m32e7570 [31mTue Nov 2 10:25:23 2021 +0000 [34mGithub GRAP Bot[32m [msale_eshop 12.0.1.1.3
[33m1101cde [31mTue Nov 2 08:59:22 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #100 into 12.0
[33m7e7fea6 [31mTue Oct 26 16:58:46 2021 +0200 [34mSylvain LE GAL[32m [m [FIX] sale_eshop : FIX buttons icons on tree and form views
[33mff7cfa3 [31mMon Oct 25 22:52:29 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m76f9a53 [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_label_sale 12.0.1.1.3
[33m9034e06 [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [maccount_invoice_supplierinfo_update_standard_price_test 12.0.1.0.3
[33m76fd44a [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.1.3
[33md9dcccb [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_origin_l10n_fr_department 12.0.1.1.1
[33m8fa79d9 [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [maccount_move_change_number 12.0.1.1.1
[33m1d82fac [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [msale_recovery_moment 12.0.1.1.2
[33mf8969c6 [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [mtechnical_partner_access 12.0.1.2.1
[33mab05f16 [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_origin 12.0.1.1.2
[33mba4982c [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_print_category_food_report 12.0.1.1.3
[33m2fe8619 [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [mstock_preparation_category 12.0.1.1.2
[33ma12ae32 [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_food 12.0.1.1.5
[33m8a3bbbb [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_sale 12.0.1.1.1
[33mf5ddc8a [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_label_account 12.0.1.1.3
[33ma49b8ae [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [maccount_invoice_supplierinfo_update_standard_price 12.0.1.1.2
[33mc06b4af [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_label 12.0.1.1.4
[33mffb010b [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [msale_eshop 12.0.1.1.2
[33m58787b9 [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_test 12.0.1.1.4
[33m5b3df15 [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_to_scale_bizerba 12.0.2.0.3
[33m58770ea [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_purchase 12.0.1.1.3
[33m25cab5d [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_pos 12.0.1.1.1
[33m4353f9d [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_notation 12.0.3.1.1
[33m8696711 [31mMon Oct 25 22:52:24 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_fiscal_company 12.0.1.1.1
[33m53f53bf [31mMon Oct 25 17:00:23 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #99 into 12.0
[33m21a4c80 [31mMon Oct 25 12:14:08 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mbd010f7 [31mMon Oct 25 12:14:04 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_label 12.0.1.1.3
[33m65b8854 [31mMon Oct 25 12:14:04 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_label_account 12.0.1.1.2
[33mc6c0b2e [31mMon Oct 25 12:14:04 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_label_sale 12.0.1.1.2
[33ma5ad977 [31mMon Oct 25 12:14:03 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] README.rst
[33m01738bd [31mMon Oct 25 12:13:59 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m06ff5d0 [31mMon Oct 25 12:14:35 2021 +0200 [34mSylvain LE GAL[32m [m[12.0][REF] uniformize website in __manifest__.py + add pre-commit check
[33m982b7b6 [31mMon Oct 25 09:28:34 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #98 into 12.0
[33mb7eda8b [31mMon Oct 25 10:50:11 2021 +0200 [34mQuentin Dupont[32m [mAdd quentinDupont maintainer
[33m5007ecc [31mMon Aug 9 13:06:43 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] README.rst
[33maf8b509 [31mMon Aug 9 15:06:35 2021 +0200 [34mSylvain LE GAL[32m [mUpdate USAGE.rst
[33m06b8e79 [31mMon Aug 9 12:48:01 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m08415b5 [31mMon Aug 9 12:47:56 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_label 12.0.1.1.2
[33mc70b033 [31mMon Aug 9 12:47:55 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] README.rst
[33m97dac8a [31mMon Aug 9 09:24:52 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #96 into 12.0
[33mf6d2008 [31mMon Aug 9 11:24:04 2021 +0200 [34mSylvain LE GAL[32m [m[FIX] product_label : incorrect syntax of images in redme section
[33m94d852d [31mMon Aug 9 09:11:57 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mb344803 [31mMon Aug 9 09:11:52 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_label 12.0.1.1.1
[33m8324f20 [31mMon Aug 9 09:11:52 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_label_account 12.0.1.1.1
[33mebd71cd [31mMon Aug 9 09:11:52 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_food 12.0.1.1.4
[33m9928441 [31mMon Aug 9 09:11:52 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_label_sale 12.0.1.1.1
[33m6b2a1b1 [31mMon Aug 9 09:11:51 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] README.rst
[33mbface41 [31mMon Aug 9 09:11:47 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m6107b61 [31mMon Aug 9 08:17:02 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #95 into 12.0
[33me206677 [31mSun Aug 8 11:57:04 2021 +0200 [34mSylvain LE GAL[32m [m[ADD] product_food : roadmap
[33m9c0be26 [31mWed Aug 4 16:04:35 2021 +0200 [34mSylvain LE GAL[32m [m[IMP] product_food : add use-by Date and Best before date ; add storage_method ;
[33ma715a63 [31mWed Aug 4 12:45:22 2021 +0200 [34mSylvain LE GAL[32m [m[REF] product_label : split into 3 modules
[33m3285913 [31mMon Aug 2 20:43:54 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m86fc7c6 [31mMon Aug 2 16:40:33 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #94 into 12.0
[33mbd8c94d [31mMon Aug 2 15:56:38 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m23c75c5 [31mMon Aug 2 16:58:57 2021 +0200 [34mSylvain LE GAL[32m [m [REF] clean oca_depedencies
[33m682ce28 [31mMon Aug 2 14:54:35 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #92 into 12.0
[33m37c56bf [31mFri Jul 30 23:28:43 2021 +0200 [34mSylvain LE GAL[32m [m[REF] Move purchase_package_qty from business to incubator
[33mefc9d5f [31mSat Jul 31 20:34:26 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m01ceacd [31mSat Jul 31 20:34:20 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_food 12.0.1.1.3
[33mcc78159 [31mSat Jul 31 20:06:04 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #90 into 12.0
[33mf7aeaaf [31mSat Jul 31 15:22:15 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m8735d00 [31mSat Jul 31 15:22:09 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_test 12.0.1.1.3
[33m09fd9bb [31mSat Jul 31 13:33:39 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #93 into 12.0
[33mc1c8677 [31mSat Jul 31 15:32:06 2021 +0200 [34mSylvain LE GAL[32m [m[FIX] recurring_consignment_test: fix test in case of test is ran at the end of the month
[33m29b4132 [31mWed Jul 28 16:06:49 2021 +0200 [34mSylvain LE GAL[32m [m[IMP][12.0] product_food : add alcohol by volume
[33m7105f5a [31mThu Jul 29 21:55:20 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m2101807 [31mThu Jul 29 21:55:14 2021 +0000 [34mGithub GRAP Bot[32m [msale_recovery_moment 12.0.1.1.1
[33m52075ef [31mThu Jul 29 17:42:25 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #89 into 12.0
[33ma9307ea [31mThu Jul 29 16:02:37 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m82d4295 [31mThu Jul 29 16:02:31 2021 +0000 [34mGithub GRAP Bot[32m [msale_eshop 12.0.1.1.1
[33me7a36ac [31mThu Jul 29 10:39:33 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #88 into 12.0
[33ma4b996e [31mThu Jul 29 10:35:43 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m98782cb [31mThu Jul 29 10:35:37 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_food 12.0.1.1.2
[33ma2ee7d3 [31mThu Jul 29 10:35:37 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_print_category_food_report 12.0.1.1.2
[33m04fe22d [31mThu Jul 29 10:35:37 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_origin 12.0.1.1.1
[33mc804ec2 [31mThu Jul 29 10:35:37 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] README.rst
[33me263e8d [31mThu Jul 29 07:51:19 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #80 into 12.0
[33m6890764 [31mThu Jul 29 07:49:27 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m88cfb9b [31mThu Jul 29 07:49:21 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.1.2
[33mb1482c7 [31mThu Jul 29 07:20:59 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #87 into 12.0
[33m71f3873 [31mWed Jul 28 17:14:01 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m0ea3a48 [31mWed Jul 28 17:13:55 2021 +0000 [34mGithub GRAP Bot[32m [mstock_preparation_category 12.0.1.1.1
[33mccef2be [31mWed Jul 28 15:03:52 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #91 into 12.0
[33mf7daffa [31mWed Jul 28 17:03:17 2021 +0200 [34mSylvain LE GAL[32m [m [FIX][12.0] stock_preparation_category : fix bad fr.po file
[33m85bae45 [31mTue Jul 27 11:43:32 2021 +0200 [34mSylvain LE GAL[32m [m[FIX] sale_recovery_moment : prevent error is user is not member anymore of Recovery Moment User
[33mb0363ee [31mTue Jul 20 11:52:29 2021 +0200 [34mSylvain LE GAL[32m [m[FIX] set 'ue - Non UE' to 'ue - Non UE'
[33ma59c7e2 [31mTue Jul 20 11:51:46 2021 +0200 [34mSylvain LE GAL[32m [m[IMP] product_origin : remove try/except and warning if no country group is found
[33m0ce2f8a [31mMon Jul 19 15:27:33 2021 +0200 [34mSylvain LE GAL[32m [m[REF] sale_eshop : update, following queue_job refactoring
[33ma793615 [31mWed Jul 7 14:23:53 2021 +0200 [34mSylvain LE GAL[32m [m [FIX] recurring_consignment : set regular account type for consignor account (467xxx)
[33m17b01a5 [31mMon Jun 28 16:40:44 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mb8b6d09 [31mMon Jun 28 16:40:36 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.1.1
[33mb6917c7 [31mMon Jun 28 16:40:36 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_test 12.0.1.1.2
[33m4ce7638 [31mMon Jun 28 16:40:36 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_to_scale_bizerba 12.0.2.0.2
[33m402f6ee [31mMon Jun 28 16:40:32 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m57445fe [31mMon Jun 28 16:13:07 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #86 into 12.0
[33mcef16ef [31mMon Jun 21 20:48:35 2021 +0200 [34mSylvain LE GAL[32m [m[FIX] recurring_consignment : avoid bad fiscal settings. (classification of consignor, without consignor defined)
[33m17860d3 [31mThu Jun 24 15:09:58 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mc2f07c4 [31mThu Jun 24 15:09:53 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_to_scale_bizerba 12.0.2.0.1
[33mb2f78a4 [31mThu Jun 24 12:32:31 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #85 into 12.0
[33mea841f6 [31mWed May 19 12:07:41 2021 +0200 [34mQuentin Dupont[32m [m[IMP] Improve for product : Organic legislation for origin, distribution channel, vegan
[33m2595171 [31mFri Jun 18 16:44:08 2021 +0200 [34mSylvain LE GAL[32m [m [IMP] product_to_scale_bizerba : add constrains on product.product : product can not have a scale group without barcode
[33m95346e0 [31mFri Jun 11 14:25:25 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m7be52f2 [31mFri Jun 11 14:25:19 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_print_category_food_report 12.0.1.1.1
[33m5f06116 [31mFri Jun 11 14:08:23 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #84 into 12.0
[33m19f769a [31mFri Jun 11 12:27:06 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mbd5c61f [31mFri Jun 11 12:27:00 2021 +0000 [34mGithub GRAP Bot[32m [maccount_invoice_supplierinfo_update_standard_price_test 12.0.1.0.2
[33m5a75906 [31mFri Jun 11 12:27:00 2021 +0000 [34mGithub GRAP Bot[32m [maccount_invoice_supplierinfo_update_standard_price 12.0.1.1.1
[33m213ad80 [31mFri Jun 11 12:27:00 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] README.rst
[33mefb414f [31mFri Jun 11 12:26:55 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33ma2f9d5b [31mFri Jun 11 11:50:41 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #83 into 12.0
[33mff954ff [31mFri Jun 11 11:41:24 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m1d574b5 [31mFri Jun 11 11:04:23 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #82 into 12.0
[33mb5e3ff2 [31mFri Jun 11 10:59:42 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m8c1d7ba [31mFri Jun 11 10:59:36 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_purchase 12.0.1.1.2
[33mdc65697 [31mFri Jun 11 10:40:57 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #81 into 12.0
[33mf991fbd [31mTue Jun 8 12:18:25 2021 +0200 [34mSylvain LE GAL[32m [m[FIX] product_print_category_food_report : bad translation for qweb_template_pricetag_bulk_square generate html on pdf
[33m0693d57 [31mThu Jun 3 14:51:03 2021 +0200 [34mSylvain LE GAL[32m [m[FIX] account_invoice_supplierinfo_update_standard_price: split into a dedicated test module, to avoid error during test installation
[33m26e0149 [31mThu Jun 3 13:00:34 2021 +0200 [34mSylvain LE GAL[32m [m[REF] product_to_scale_bizerba : remove scale_tare_weight field, and replace it by tare_weight field (pos_tare)
[33mbbdc401 [31mWed May 26 22:39:31 2021 +0200 [34mSylvain LE GAL[32m [m [FIX] recurring_consignment_murchase : make button_validate working with many elements
[33m04853b1 [31mSat May 15 07:20:20 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33me980d02 [31mSat May 15 07:20:15 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_food 12.0.1.1.1
[33m2d4cfad [31mSat May 15 07:01:53 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #79 into 12.0
[33m5a50855 [31mWed May 12 16:48:58 2021 +0200 [34mSylvain LE GAL[32m [mfixup!  [IMP] product_food : guess is_alimentary and is_alcohol based on categ_id
[33m0ead814 [31mWed May 12 16:16:17 2021 +0200 [34mSylvain LE GAL[32m [m [IMP] product_food : guess is_alimentary and is_alcohol based on categ_id
[33m944c0b6 [31mTue Apr 13 09:08:25 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mca6815f [31mTue Apr 13 09:08:19 2021 +0000 [34mGithub GRAP Bot[32m [mtechnical_partner_access 12.0.1.2.0
[33m0db029d [31mTue Apr 13 08:26:44 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #78 into 12.0
[33m4ae5417 [31mTue Apr 13 08:19:38 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m354f903 [31mTue Apr 13 08:19:32 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_purchase 12.0.1.1.1
[33mc9f2c32 [31mTue Apr 13 08:19:32 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_test 12.0.1.1.1
[33m9c41c8f [31mTue Apr 13 07:58:48 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #76 into 12.0
[33m4727049 [31mThu Apr 1 23:28:17 2021 +0200 [34mSylvain LE GAL[32m [m[TRY][FIX] travis
[33m5e301f9 [31mThu Feb 18 16:07:53 2021 +0100 [34mQuentin Dupont[32m [m[IMP] Purchase state
[33m4dfa1f4 [31mFri Mar 19 20:43:12 2021 +0100 [34mSylvain LE GAL[32m [m[IMP] technical_partner_access : add indexes on is_odoo_user and is_odoo_company fields ; [IMP] remove overload of _name_search and instead, add a dependency to new module name_search_reset_res_partner
[33m2be73e8 [31mMon Feb 22 09:22:22 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m958407d [31mMon Feb 22 09:22:15 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_origin 12.0.1.1.0
[33m7f4f74e [31mMon Feb 22 09:22:15 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_to_scale_bizerba 12.0.1.1.0
[33md4b7974 [31mMon Feb 22 09:22:15 2021 +0000 [34mGithub GRAP Bot[32m [msale_eshop 12.0.1.1.0
[33m1d3753c [31mMon Feb 22 09:22:15 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.1.0
[33m57199fd [31mMon Feb 22 09:22:15 2021 +0000 [34mGithub GRAP Bot[32m [mpurchase_package_qty 12.0.1.1.0
[33mafef1cf [31mMon Feb 22 09:22:15 2021 +0000 [34mGithub GRAP Bot[32m [maccount_invoice_supplierinfo_update_standard_price 12.0.1.1.0
[33mda134ea [31mMon Feb 22 09:22:15 2021 +0000 [34mGithub GRAP Bot[32m [mstock_preparation_category 12.0.1.1.0
[33m70956f9 [31mMon Feb 22 09:22:15 2021 +0000 [34mGithub GRAP Bot[32m [msale_recovery_moment 12.0.1.1.0
[33mf573106 [31mMon Feb 22 09:22:15 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_print_category_food_report 12.0.1.1.0
[33m2125b6c [31mMon Feb 22 09:22:15 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_purchase 12.0.1.1.0
[33meb709c5 [31mMon Feb 22 09:22:14 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_label 12.0.1.1.0
[33m8c7c135 [31mMon Feb 22 09:22:14 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_notation 12.0.3.1.0
[33m5d8ee09 [31mMon Feb 22 09:22:14 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_origin_l10n_fr_department 12.0.1.1.0
[33me25e8d5 [31mMon Feb 22 09:22:14 2021 +0000 [34mGithub GRAP Bot[32m [mtechnical_partner_access 12.0.1.1.0
[33mb2bdb36 [31mMon Feb 22 09:22:14 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_sale 12.0.1.1.0
[33mb2036ec [31mMon Feb 22 09:22:14 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_pos 12.0.1.1.0
[33m50ac316 [31mMon Feb 22 09:22:14 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_fiscal_company 12.0.1.1.0
[33m735eb6e [31mMon Feb 22 09:22:14 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_food 12.0.1.1.0
[33m431569f [31mMon Feb 22 09:22:14 2021 +0000 [34mGithub GRAP Bot[32m [maccount_move_change_number 12.0.1.1.0
[33ma51c091 [31mMon Feb 22 09:22:14 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_test 12.0.1.1.0
[33mff4f216 [31mMon Feb 22 09:22:14 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] README.rst
[33mf4791d2 [31mMon Feb 22 09:02:49 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #75 into 12.0
[33m938b6c4 [31mTue Feb 16 20:20:57 2021 +0100 [34mSylvain LE GAL[32m [m[BLACK]
[33m5c53f2f [31mTue Feb 16 14:55:15 2021 +0100 [34mSylvain LE GAL[32m [mWIP
[33m93b8866 [31mTue Feb 16 14:23:25 2021 +0100 [34mSylvain LE GAL[32m [mWIP
[33m99b9375 [31mTue Feb 16 13:57:11 2021 +0100 [34mSylvain LE GAL[32m [m[REF] add pre-commit
[33m706af96 [31mMon Feb 15 16:05:46 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m8afbf24 [31mMon Feb 15 16:05:38 2021 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_purchase 12.0.1.0.3
[33m3e6135a [31mMon Feb 15 15:37:16 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #74 into 12.0
[33m92fd0d1 [31mMon Feb 15 15:06:12 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m5c3a7cb [31mMon Feb 15 15:06:05 2021 +0000 [34mGithub GRAP Bot[32m [mtechnical_partner_access 12.0.1.0.4
[33m2dae32b [31mMon Feb 15 14:46:06 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #73 into 12.0
[33m92f81e4 [31mMon Feb 15 13:23:50 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mda45853 [31mMon Feb 15 13:05:09 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #72 into 12.0
[33maa668a6 [31mMon Feb 8 16:04:14 2021 +0100 [34mQuentin Dupont[32m [m[IMP] Hide invoice button
[33m003569c [31mWed Feb 3 22:43:02 2021 +0100 [34mSylvain LE GAL[32m [m[FIX] ouais, finalement c'était pas la bonne méthode on dirait
[33mc68349c [31mWed Feb 3 22:20:52 2021 +0100 [34mSylvain LE GAL[32m [m [FIX] technical_partner_access : make domain working also in name_search if name is defined
[33m3bfde4f [31mSun Jan 17 18:31:41 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m2800226 [31mSun Jan 17 18:31:26 2021 +0000 [34mGithub GRAP Bot[32m [mproduct_food 12.0.1.0.3
[33md719bdc [31mSun Jan 17 18:03:51 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #71 into 12.0
[33mc55d622 [31mSun Jan 17 17:20:28 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m56759d9 [31mSun Jan 17 17:20:20 2021 +0000 [34mGithub GRAP Bot[32m [maccount_invoice_supplierinfo_update_standard_price 12.0.1.0.4
[33mabb8647 [31mSun Jan 17 16:00:13 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #70 into 12.0
[33m54cc6fd [31mSun Jan 17 15:48:51 2021 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m02ea348 [31mSun Jan 17 15:48:43 2021 +0000 [34mGithub GRAP Bot[32m [maccount_move_change_number 12.0.1.0.2
[33m810173d [31mSun Jan 17 15:20:41 2021 +0000 [34mGithub GRAP Bot[32m [mMerge PR #69 into 12.0
[33ma3f0af6 [31mSun Jan 17 16:18:11 2021 +0100 [34mSylvain LE GAL[32m [m [REM] remove obsolete module product_category_recursive_property
[33me01a243 [31mFri Dec 18 16:21:49 2020 +0100 [34mSylvain LE GAL[32m [m [FIX] product_food : dont raise an error on compute. Move raise in constrains
[33mabcd08c [31mFri Dec 18 00:41:07 2020 +0100 [34mSylvain LE GAL[32m [m[FIX] account_invoice_supplierinfo_update_standard_price: wrong test ...
[33m83a4cbe [31mThu Dec 17 20:58:15 2020 +0100 [34mSylvain LE GAL[32m [m [FIX] account_invoice_supplierinfo_update_standard_price: divide per quantity to compute shared cost
[33m035a47a [31mSat Dec 12 06:53:55 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m3df94e6 [31mSat Dec 12 06:53:47 2020 +0000 [34mGithub GRAP Bot[32m [mtechnical_partner_access 12.0.1.0.3
[33md462b2a [31mSat Dec 12 06:53:47 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] README.rst
[33m949fd3c [31mFri Dec 11 18:42:20 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #66 into 12.0
[33mefd8b20 [31mFri Dec 11 18:40:11 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m1e93e54 [31mFri Dec 11 18:40:03 2020 +0000 [34mGithub GRAP Bot[32m [mproduct_print_category_food_report 12.0.1.0.10
[33m59b2d86 [31mFri Dec 11 16:29:03 2020 +0100 [34mSylvain LE GAL[32m [m[FIX] account_move_change_number: allow xmlrpc call, returning True
[33m6dd834a [31mFri Dec 11 11:52:18 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #67 into 12.0
[33m5da5e12 [31mFri Dec 11 10:31:32 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m96b10da [31mFri Dec 11 10:31:24 2020 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_purchase 12.0.1.0.2
[33m32e88c5 [31mFri Dec 11 08:51:04 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #68 into 12.0
[33m9438bc8 [31mFri Dec 11 00:07:54 2020 +0100 [34mSylvain LE GAL[32m [m[FIX] recurring_consignment_purchase: bad dependency
[33ma57754b [31mWed Dec 2 10:55:38 2020 +0100 [34mQuentin Dupont[32m [m[IMP] Bulk square : No uom for unit product
[33m1d24a4d [31mTue Dec 1 12:40:58 2020 +0100 [34mSylvain LE GAL[32m [m [IMP] technical_partner_access : prevent updating company partners for non admin users. [IMP] improve is_odoo_company write. [IMP] add images and improve description
[33me528d99 [31mMon Nov 16 14:39:54 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mada3121 [31mMon Nov 16 14:39:46 2020 +0000 [34mGithub GRAP Bot[32m [mpurchase_package_qty 12.0.1.0.2
[33ma4f1321 [31mMon Nov 16 13:24:25 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #65 into 12.0
[33mf5d8064 [31mSun Nov 15 19:35:17 2020 +0100 [34mSylvain LE GAL[32m [m [FIX] purchase_package_qty: do not raise an error if package_qty == 0 and improve test coverage
[33m62eff22 [31mSat Nov 14 06:59:08 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m56b4670 [31mSat Nov 14 06:59:00 2020 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.0.15
[33mea89653 [31mSat Nov 14 06:03:12 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #64 into 12.0
[33mc799866 [31mSat Nov 14 05:55:38 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m9fd3677 [31mSat Nov 14 05:55:31 2020 +0000 [34mGithub GRAP Bot[32m [mproduct_to_scale_bizerba 12.0.1.0.3
[33m330d0d1 [31mSat Nov 14 04:10:57 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #63 into 12.0
[33mba8ff96 [31mSat Nov 14 03:52:30 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mce310a9 [31mSat Nov 14 03:52:23 2020 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_pos 12.0.1.0.2
[33m606f6a0 [31mSat Nov 14 03:52:23 2020 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.0.14
[33me4bc678 [31mFri Nov 13 22:23:52 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #62 into 12.0
[33mc7a010d [31mFri Nov 13 21:29:52 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m2c693e6 [31mFri Nov 13 21:29:43 2020 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.0.13
[33m2856a6f [31mFri Nov 13 19:29:21 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #61 into 12.0
[33m487296f [31mThu Nov 12 00:13:14 2020 +0100 [34mSylvain LE GAL[32m [m [FIX] recurring_consignment : do not raise an error on product update, if user doesnt have the right to create / write on product.pricelist.item
[33mc611903 [31mWed Nov 11 23:22:01 2020 +0100 [34mSylvain LE GAL[32m [m[FIX] access right to log and scale group. [IMP] add widget on product.form selection
[33m0fa06d1 [31mWed Nov 11 22:14:13 2020 +0100 [34mSylvain LE GAL[32m [m [FIX] product_to_scale_bizerba: handle encoding ; [RESTORE] uom_uom view
[33m4bcc78e [31mFri Nov 6 19:40:59 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mdca79ae [31mFri Nov 6 19:40:51 2020 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.0.12
[33mc4c751b [31mFri Nov 6 19:50:11 2020 +0100 [34mSylvain LE GAL[32m [m[FIX] recurring_consignment : display in the product list, the sales made in the PoS
[33m511dc6c [31mFri Nov 6 18:46:38 2020 +0100 [34mSylvain LE GAL[32m [m [FIX] recurring_consigment : bad code make text not translatable
[33ma72c70a [31mFri Nov 6 17:26:03 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #60 into 12.0
[33m8ecf88b [31mFri Nov 6 18:08:53 2020 +0100 [34mQuentin Dupont[32m [mBIG TRAD CHANGE
[33m2b69063 [31mThu Nov 5 03:24:05 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m929a74a [31mThu Nov 5 03:23:58 2020 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.0.11
[33mc9a8b96 [31mThu Nov 5 00:37:48 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #59 into 12.0
[33m74a2bce [31mThu Nov 5 01:37:18 2020 +0100 [34mSylvain LE GAL[32m [m [FIX] recurring_consignment : res.company::create should return object
[33m9a3a3d0 [31mWed Nov 4 22:21:36 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m7515aed [31mWed Nov 4 22:21:26 2020 +0000 [34mGithub GRAP Bot[32m [mproduct_print_category_food_report 12.0.1.0.9
[33m94d949e [31mWed Nov 4 18:29:34 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #58 into 12.0
[33mfba4fb4 [31mWed Nov 4 19:28:45 2020 +0100 [34mSylvain LE GAL[32m [m [FIX] remove obsolete field report_extra_food_info
[33m6bc8eb3 [31mWed Nov 4 14:41:54 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m51a3100 [31mWed Nov 4 14:41:45 2020 +0000 [34mGithub GRAP Bot[32m [mproduct_print_category_food_report 12.0.1.0.8
[33ma249b8c [31mWed Nov 4 14:41:45 2020 +0000 [34mGithub GRAP Bot[32m [mproduct_origin 12.0.1.0.2
[33me4554be [31mWed Nov 4 12:56:04 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #57 into 12.0
[33maed5365 [31mWed Nov 4 13:52:24 2020 +0100 [34mQuentin Dupont[32m [mchange translation
[33m241d31e [31mWed Nov 4 12:01:32 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33ma3360c0 [31mWed Nov 4 12:01:24 2020 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_test 12.0.1.0.2
[33md918eb5 [31mWed Nov 4 10:52:10 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #54 into 12.0
[33m1fc7b95 [31mWed Nov 4 10:34:16 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m344d4c6 [31mWed Nov 4 10:34:08 2020 +0000 [34mGithub GRAP Bot[32m [msale_recovery_moment 12.0.1.0.4
[33m72a5089 [31mWed Nov 4 10:01:39 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #55 into 12.0
[33m47b5a0e [31mSat Oct 31 16:48:36 2020 +0100 [34mSylvain LE GAL[32m [m [FIX] sale_recovery_moment : set default temporary code to avoid error on creation ; [IMP] make recovery moments editable bottom in the group view ; [FIX] do not crash during the computation of group state, if no moments are defined
[33mc181025 [31mSat Oct 31 15:20:27 2020 +0100 [34mSylvain LE GAL[32m [m [REM] recurring_consignment_test: useless comment
[33m0299c49 [31mMon Nov 2 21:52:14 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mb1c9ba6 [31mMon Nov 2 21:52:07 2020 +0000 [34mGithub GRAP Bot[32m [mproduct_print_category_food_report 12.0.1.0.7
[33m41b0cfa [31mMon Nov 2 20:41:40 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #56 into 12.0
[33md84bb95 [31mMon Nov 2 18:38:20 2020 +0100 [34mQuentin Dupont[32m [mcss dit la baleine
[33m85e1d0d [31mThu Oct 29 20:51:13 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33ma4ef90c [31mThu Oct 29 20:51:05 2020 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.0.10
[33m1fa315b [31mThu Oct 29 18:29:40 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #53 into 12.0
[33m7beab2d [31mThu Oct 29 16:44:54 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m5bf783e [31mThu Oct 29 16:44:46 2020 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.0.9
[33m93f552c [31mThu Oct 29 16:43:19 2020 +0100 [34mSylvain LE GAL[32m [m [FIX] do not create reconciable account
[33m57b0b2c [31mThu Oct 29 14:42:10 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #52 into 12.0
[33m1495fca [31mThu Oct 29 15:40:51 2020 +0100 [34mSylvain LE GAL[32m [m [FIX] recurring_consignment: set correct description on taxes
[33m60de87a [31mWed Oct 28 18:41:38 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33md5020aa [31mWed Oct 28 18:41:30 2020 +0000 [34mGithub GRAP Bot[32m [mproduct_label 12.0.1.0.2
[33mb069cc0 [31mWed Oct 28 18:41:30 2020 +0000 [34mGithub GRAP Bot[32m [msale_eshop 12.0.1.0.6
[33mffb561b [31mWed Oct 28 14:08:12 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #51 into 12.0
[33m789b500 [31mWed Oct 28 13:10:14 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m295a7e8 [31mWed Oct 28 13:10:07 2020 +0000 [34mGithub GRAP Bot[32m [mproduct_print_category_food_report 12.0.1.0.6
[33m417a87b [31mWed Oct 28 12:11:06 2020 +0100 [34mSylvain LE GAL[32m [m [FIX] product_label : add migration image ; sale_eshop : migrate also medium and small images
[33mba1593f [31mWed Oct 28 11:08:17 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #50 into 12.0
[33m2df0495 [31mWed Oct 28 11:48:47 2020 +0100 [34mQuentin Dupont[32m [m[IMP] write date in product labels
[33m088ca7d [31mMon Oct 26 16:42:48 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mc629d1b [31mMon Oct 26 16:42:40 2020 +0000 [34mGithub GRAP Bot[32m [mproduct_print_category_food_report 12.0.1.0.5
[33mbe85595 [31mMon Oct 26 14:24:19 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #49 into 12.0
[33mf990d48 [31mMon Oct 26 14:53:54 2020 +0100 [34mQuentin Dupont[32m [mIMP make translation great again
[33m9eef6d3 [31mSat Oct 24 13:00:52 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m34ae7d5 [31mSat Oct 24 13:00:44 2020 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.0.8
[33m5c702b4 [31mSat Oct 24 12:44:16 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #48 into 12.0
[33m04852c4 [31mSat Oct 24 12:08:01 2020 +0200 [34mSylvain LE GAL[32m [m [ADD] recurring_consignment: allow possibility to make invoices for any dates ; [IMP] translation
[33m6bff307 [31mFri Oct 23 23:02:51 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mff1006e [31mFri Oct 23 23:02:43 2020 +0000 [34mGithub GRAP Bot[32m [mproduct_food 12.0.1.0.2
[33mf278d13 [31mFri Oct 23 18:56:52 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #33 into 12.0
[33m7986c79 [31mWed Oct 21 16:13:13 2020 +0200 [34mQuentin Dupont[32m [mnew name + display only if different from list price
[33m9c7655a [31mWed Oct 21 08:28:11 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m73d92d2 [31mWed Oct 21 08:28:04 2020 +0000 [34mGithub GRAP Bot[32m [mproduct_print_category_food_report 12.0.1.0.4
[33m415892e [31mWed Oct 21 08:06:30 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #42 into 12.0
[33m26fa729 [31mWed Oct 21 07:44:18 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m7abc24e [31mWed Oct 21 07:44:10 2020 +0000 [34mGithub GRAP Bot[32m [msale_eshop 12.0.1.0.5
[33m5cd594c [31mWed Oct 21 07:44:10 2020 +0000 [34mGithub GRAP Bot[32m [mproduct_notation 12.0.3.0.7
[33med02c07 [31mWed Oct 21 07:44:10 2020 +0000 [34mGithub GRAP Bot[32m [msale_recovery_moment 12.0.1.0.3
[33m0871096 [31mWed Oct 21 07:44:10 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] README.rst
[33m85a51cb [31mWed Oct 21 07:27:08 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #44 into 12.0
[33m9bab023 [31mSun Oct 18 20:04:58 2020 +0200 [34mSylvain LE GAL[32m [m[TRY] to fix image migration of eshop.category ; [FIX] wizard duplication in sale_recovery_moment + [ADD] demo data for eshop configuration
[33m7a2c6c9 [31mTue Oct 20 21:13:56 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m53618b3 [31mTue Oct 20 21:13:46 2020 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_fiscal_company 12.0.1.0.3
[33mdf43555 [31mTue Oct 20 21:13:46 2020 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.0.7
[33m757ff01 [31mTue Oct 20 20:53:00 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #47 into 12.0
[33m65e2d10 [31mTue Oct 20 22:48:05 2020 +0200 [34mSylvain LE GAL[32m [m[FIX] consignor creation ; [IMP] prevent creation of consignor without wizard
[33m9744355 [31mTue Oct 20 17:06:13 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mf5a4cf4 [31mTue Oct 20 17:06:05 2020 +0000 [34mGithub GRAP Bot[32m [mproduct_print_category_food_report 12.0.1.0.3
[33m4fdba90 [31mTue Oct 20 15:57:25 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #46 into 12.0
[33m75ccdd6 [31mTue Oct 20 17:56:53 2020 +0200 [34mSylvain LE GAL[32m [m[FIX] product_print_category_food_report : add ir.rule for product.pricetag.type model and company_id on tree view
[33mbec99ff [31mMon Oct 19 09:25:31 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mec4e8c1 [31mMon Oct 19 09:25:23 2020 +0000 [34mGithub GRAP Bot[32m [mtechnical_partner_access 12.0.1.0.2
[33mf6579c5 [31mMon Oct 19 09:25:23 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] README.rst
[33m6c1f74f [31mMon Oct 19 09:25:18 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mfc1bb88 [31mMon Oct 19 09:07:24 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #45 into 12.0
[33mce9704a [31mMon Oct 19 10:40:58 2020 +0200 [34mSylvain LE GAL[32m [m[REF] users_partners_access : renamed and refactored into technical_partner_access
[33mfd2f68b [31mFri Oct 16 14:30:14 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m0419b4f [31mFri Oct 16 14:30:06 2020 +0000 [34mGithub GRAP Bot[32m [msale_eshop 12.0.1.0.4
[33md997b17 [31mFri Oct 16 14:13:12 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #43 into 12.0
[33m4a0ac6b [31mFri Oct 16 15:25:40 2020 +0200 [34mSylvain LE GAL[32m [m[IMP] sale_eshop: eshop_url and eshop_invalidation_key are now parameters
[33m83c6feb [31mThu Oct 15 17:25:17 2020 +0200 [34mQuentin Dupont[32m [m[IMP] add spider chart in product label normal
[33mf3f8848 [31mTue Oct 13 23:35:19 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m612428d [31mTue Oct 13 23:35:12 2020 +0000 [34mGithub GRAP Bot[32m [mproduct_notation 12.0.3.0.6
[33m8b5205c [31mTue Oct 13 23:16:37 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #41 into 12.0
[33m99c1bbd [31mWed Oct 14 01:16:01 2020 +0200 [34mSylvain LE GAL[32m [m[TRY] to run migration script
[33m851403d [31mTue Oct 13 10:18:34 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m4ed00bd [31mTue Oct 13 10:18:26 2020 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment_fiscal_company 12.0.1.0.2
[33ma306737 [31mTue Oct 13 10:18:26 2020 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.0.6
[33me5b6a08 [31mTue Oct 13 10:18:26 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] README.rst
[33m036a418 [31mTue Oct 13 10:18:21 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mc63d7b6 [31mTue Oct 13 10:02:15 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #40 into 12.0
[33m3cba0fc [31mMon Oct 12 20:31:30 2020 +0200 [34mSylvain LE GAL[32m [m[FIX] recurring_consignement ; [ADD] sequence on consignors ; [ADD] glue module with fiscal_company_base
[33mbcce2df [31mSat Oct 10 07:13:59 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m88db6cf [31mSat Oct 10 06:56:56 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #39 into 12.0
[33m1e367d7 [31mSat Oct 10 08:55:53 2020 +0200 [34mSylvain LE GAL[32m [m[FIX] production_notation upgrade
[33me8c5ced [31mTue Oct 6 17:31:29 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m814522f [31mTue Oct 6 17:31:21 2020 +0000 [34mGithub GRAP Bot[32m [mproduct_notation 12.0.3.0.3
[33m8c0967d [31mTue Oct 6 16:29:34 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #38 into 12.0
[33m38bdd00 [31mTue Oct 6 18:28:28 2020 +0200 [34mSylvain LE GAL[32m [m[FIX] TRY : try to fix product_notation image migration
[33m9139ca4 [31mThu Oct 1 10:55:46 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33ma0e671b [31mThu Oct 1 10:55:39 2020 +0000 [34mGithub GRAP Bot[32m [mproduct_print_category_food_report 12.0.1.0.2
[33m3ce4fec [31mThu Oct 1 10:38:30 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #37 into 12.0
[33m246b60c [31mThu Oct 1 12:37:38 2020 +0200 [34mSylvain LE GAL[32m [m[FIX] product_print_category_food_report: restore broken features. (missing company_id field, broken views)
[33mc61355c [31mThu Oct 1 09:51:50 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33mb0fcfa8 [31mThu Oct 1 09:51:42 2020 +0000 [34mGithub GRAP Bot[32m [mproduct_notation 12.0.3.0.2
[33m5a9e57c [31mThu Oct 1 09:34:14 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #36 into 12.0
[33mbd850a9 [31mThu Oct 1 11:33:33 2020 +0200 [34mSylvain LE GAL[32m [m[IMP] product_notation: migration of spider_chart_image
[33m28a7aab [31mWed Sep 30 10:45:06 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m4cb889a [31mWed Sep 30 10:44:58 2020 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.0.3
[33m28bc955 [31mWed Sep 30 10:27:05 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #35 into 12.0
[33m8ed280f [31mWed Sep 23 22:43:30 2020 +0200 [34mSylvain LE GAL[32m [m[FIX] recurring consignement, regarding taxes
[33me09f1c3 [31mFri Sep 18 14:11:54 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33md5fd2b8 [31mFri Sep 18 14:11:46 2020 +0000 [34mGithub GRAP Bot[32m [maccount_invoice_supplierinfo_update_standard_price 12.0.1.0.3
[33m51ebfe5 [31mFri Sep 18 14:11:46 2020 +0000 [34mGithub GRAP Bot[32m [msale_recovery_moment 12.0.1.0.2
[33me8c98fd [31mFri Sep 18 14:11:45 2020 +0000 [34mGithub GRAP Bot[32m [msale_eshop 12.0.1.0.3
[33m0bcee2b [31mFri Sep 18 14:11:45 2020 +0000 [34mGithub GRAP Bot[32m [mproduct_to_scale_bizerba 12.0.1.0.2
[33mdfeb4e8 [31mFri Sep 18 14:11:45 2020 +0000 [34mGithub GRAP Bot[32m [mrecurring_consignment 12.0.1.0.2
[33mef78daf [31mFri Sep 18 13:39:05 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #34 into 12.0
[33ma9d3089 [31mFri Sep 18 15:37:29 2020 +0200 [34mSylvain LE GAL[32m [m[UPD] translation
[33m9c424dd [31mMon Aug 10 10:05:23 2020 +0200 [34mQuentin Dupont[32m [m[ADD] Field Unit price
[33mdcfea37 [31mWed Jun 17 00:32:27 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33m715fb76 [31mWed Jun 17 00:32:08 2020 +0000 [34mGRAP Bot[32m [maccount_invoice_supplierinfo_update_standard_price 12.0.1.0.2
[33ma96b512 [31mWed Jun 17 00:10:49 2020 +0000 [34mGRAP Bot[32m [mMerge PR #31 into 12.0
[33m6ae6dab [31mWed Jun 17 02:07:53 2020 +0200 [34mSylvain LE GAL[32m [m[FIX] remove useless hook
[33m46fb823 [31mWed Jun 17 01:49:09 2020 +0200 [34mSylvain LE GAL[32m [m[FIX] add missing images
[33m1d61c7e [31mTue Jun 16 23:38:52 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33mf01293c [31mTue Jun 16 23:38:32 2020 +0000 [34mGRAP Bot[32m [mproduct_notation 12.0.3.0.1
[33m214b999 [31mTue Jun 16 23:38:32 2020 +0000 [34mGRAP Bot[32m [m[UPD] README.rst
[33m76e8013 [31mTue Jun 16 23:38:22 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33ma04f4ab [31mTue Jun 16 23:22:00 2020 +0000 [34mGRAP Bot[32m [mMerge PR #29 into 12.0
[33mdffee6f [31mWed Jun 17 01:02:49 2020 +0200 [34mSylvain LE GAL[32m [m[ADD] product_notation module
[33m367b361 [31mWed Jun 3 07:43:34 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33m20ded9e [31mWed Jun 3 07:43:18 2020 +0000 [34mGRAP Bot[32m [msale_eshop 12.0.1.0.2
[33m9431f74 [31mWed Jun 3 07:43:18 2020 +0000 [34mGRAP Bot[32m [m[UPD] README.rst
[33mab3ad11 [31mWed Jun 3 07:43:11 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33m46b9678 [31mWed Jun 3 07:29:20 2020 +0000 [34mGRAP Bot[32m [mMerge PR #28 into 12.0
[33m9c9aa48 [31mMon Jun 1 12:14:11 2020 +0200 [34mSylvain LE GAL[32m [m[MIG] sale_eshop: Migration to 12.0
[33m12cacfc [31mMon Jun 1 12:14:10 2020 +0200 [34mSylvain LE GAL[32m [m[REF] sale_eshop: Black python code
[33m9ef509a [31mMon Jun 1 12:13:45 2020 +0200 [34mSylvain LE GAL[32m [m[COPY] from 8.0 last version
[33m3c6def6 [31mSat May 30 18:57:26 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33m95d5485 [31mSat May 30 18:57:11 2020 +0000 [34mGRAP Bot[32m [maccount_invoice_supplierinfo_update_standard_price 12.0.1.0.1
[33med7df02 [31mSat May 30 18:57:11 2020 +0000 [34mGRAP Bot[32m [m[UPD] README.rst
[33m8393d6a [31mSat May 30 18:57:05 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33m72d49aa [31mSat May 30 18:33:40 2020 +0000 [34mGRAP Bot[32m [mMerge PR #17 into 12.0
[33m87d9fbe [31mSun Nov 24 17:11:38 2019 +0100 [34mSylvain LE GAL[32m [m[MIG] account_invoice_supplierinfo_update_standard_price: Migration to 12.0
[33m9f50dce [31mSat May 30 18:29:26 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33m1cb5ed1 [31mSat May 30 18:29:09 2020 +0000 [34mGRAP Bot[32m [mproduct_print_category_food_report 12.0.1.0.1
[33m3448382 [31mSat May 30 18:29:09 2020 +0000 [34mGRAP Bot[32m [m[UPD] README.rst
[33me362b12 [31mSat May 30 18:29:03 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33mfe5a709 [31mSat May 30 18:16:46 2020 +0000 [34mGRAP Bot[32m [mMerge PR #24 into 12.0
[33m93d5c25 [31mWed May 27 13:58:17 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33m7964d84 [31mWed May 27 13:45:19 2020 +0000 [34mGRAP Bot[32m [mMerge PR #27 into 12.0
[33mb811346 [31mWed May 27 15:40:24 2020 +0200 [34mSylvain LE GAL[32m [m[REF] remove sale_line_change_custom. (maybe to redevelopp in V12)
[33m2e7b389 [31mWed May 27 15:39:10 2020 +0200 [34mSylvain LE GAL[32m [m[REF] remove stock_picking_mass_change. (maybe to redevelopp in V12)
[33m3b4849a [31mWed May 27 15:38:52 2020 +0200 [34mSylvain LE GAL[32m [m[REF] remove stock_picking_quick_edit. (maybe to redevelopp in V12)
[33m366010e [31mWed May 27 15:38:32 2020 +0200 [34mSylvain LE GAL[32m [m[REF] remove stock_picking_type_image. (maybe to redevelopp in V12)
[33mab51ecb [31mSun May 24 21:50:38 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33m2cd5434 [31mSun May 24 21:50:23 2020 +0000 [34mGRAP Bot[32m [mpurchase_package_qty 12.0.1.0.1
[33mac056fe [31mSun May 24 21:50:23 2020 +0000 [34mGRAP Bot[32m [m[UPD] README.rst
[33m11c9494 [31mSun May 24 21:50:18 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33mefc02b5 [31mSun May 24 21:36:21 2020 +0000 [34mGRAP Bot[32m [mMerge PR #13 into 12.0
[33m399b314 [31mSun May 24 21:05:33 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33md385546 [31mSun May 24 21:05:17 2020 +0000 [34mGRAP Bot[32m [mproduct_category_recursive_property 12.0.1.0.1
[33m00f910b [31mSun May 24 21:05:17 2020 +0000 [34mGRAP Bot[32m [m[UPD] README.rst
[33m64f29e3 [31mSun May 24 21:05:11 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33mc4277e8 [31mSun May 24 20:50:55 2020 +0000 [34mGRAP Bot[32m [mMerge PR #15 into 12.0
[33m6ac87f7 [31mSun May 24 22:50:13 2020 +0200 [34mSylvain LE GAL[32m [mUpdate oca_dependencies.txt
[33mad12355 [31mSun May 24 20:29:41 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33m2b2708a [31mSun May 24 20:29:18 2020 +0000 [34mGRAP Bot[32m [mstock_preparation_category 12.0.1.0.1
[33m0cfd026 [31mSun May 24 20:29:17 2020 +0000 [34mGRAP Bot[32m [msale_recovery_moment 12.0.1.0.1
[33m908c92b [31mSun May 24 20:29:17 2020 +0000 [34mGRAP Bot[32m [m[UPD] README.rst
[33m980dab4 [31mSun May 24 20:29:10 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33m12067ab [31mSun May 24 22:22:45 2020 +0200 [34mSylvain LE GAL[32m [m[REF] remove reference to merged branches
[33m76568fa [31mSun May 24 20:13:54 2020 +0000 [34mGRAP Bot[32m [mMerge PR #23 into 12.0
[33m0512859 [31mSun May 24 19:57:40 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33m58f7102 [31mSun May 24 19:57:23 2020 +0000 [34mGRAP Bot[32m [musers_partners_access 12.0.1.0.1
[33m47ae09a [31mSun May 24 19:57:23 2020 +0000 [34mGRAP Bot[32m [m[UPD] README.rst
[33mcd9617b [31mSun May 24 19:57:18 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33m38bdea2 [31mSun May 24 19:44:16 2020 +0000 [34mGRAP Bot[32m [mMerge PR #12 into 12.0
[33m4829ac0 [31mSun May 24 18:56:19 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33ma08353d [31mSun May 24 18:56:04 2020 +0000 [34mGRAP Bot[32m [maccount_move_change_number 12.0.1.0.1
[33m88a4a5b [31mSun May 24 18:56:04 2020 +0000 [34mGRAP Bot[32m [m[UPD] README.rst
[33meb4ce95 [31mSun May 24 18:56:00 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33m4632d20 [31mSun May 24 18:41:42 2020 +0000 [34mGRAP Bot[32m [mMerge PR #16 into 12.0
[33ma017b35 [31mSun May 24 18:39:52 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33m0ecdbbf [31mSun May 24 18:39:38 2020 +0000 [34mGRAP Bot[32m [mproduct_to_scale_bizerba 12.0.1.0.1
[33mfb13f3b [31mSun May 24 18:39:38 2020 +0000 [34mGRAP Bot[32m [m[UPD] README.rst
[33m672a590 [31mSun May 24 18:39:33 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33m3902913 [31mSun May 24 18:28:16 2020 +0000 [34mGRAP Bot[32m [mMerge PR #14 into 12.0
[33m35dc8e7 [31mFri Nov 22 20:49:43 2019 +0100 [34mSylvain LE GAL[32m [m[MIG] product_to_scale_bizerba: Migration to 12.0
[33m613d339 [31mSun Nov 24 15:08:52 2019 +0100 [34mSylvain LE GAL[32m [m[MIG] account_move_change_number: Migration to 12.0
[33mec6a2d1 [31mSun May 24 06:18:13 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33m1993488 [31mSun May 24 06:17:55 2020 +0000 [34mGRAP Bot[32m [mproduct_origin 12.0.1.0.1
[33madcbd58 [31mSun May 24 06:17:54 2020 +0000 [34mGRAP Bot[32m [mproduct_label 12.0.1.0.1
[33m70b3f8a [31mSun May 24 06:17:54 2020 +0000 [34mGRAP Bot[32m [mproduct_origin_l10n_fr_department 12.0.1.0.1
[33m0d96dbf [31mSun May 24 06:17:54 2020 +0000 [34mGRAP Bot[32m [mproduct_food 12.0.1.0.1
[33m225c62a [31mSun May 24 06:17:54 2020 +0000 [34mGRAP Bot[32m [m[UPD] README.rst
[33md23fdfd [31mSun May 24 06:17:50 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33mab09bdd [31mSun May 24 06:01:29 2020 +0000 [34mGRAP Bot[32m [mMerge PR #22 into 12.0
[33m6ceabee [31mSun May 24 06:00:44 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33m221e89c [31mSun May 24 06:00:29 2020 +0000 [34mGRAP Bot[32m [mrecurring_consignment_pos 12.0.1.0.1
[33m4a313e8 [31mSun May 24 06:00:29 2020 +0000 [34mGRAP Bot[32m [mrecurring_consignment 12.0.1.0.1
[33mf2db074 [31mSun May 24 06:00:29 2020 +0000 [34mGRAP Bot[32m [mrecurring_consignment_purchase 12.0.1.0.1
[33mf67a309 [31mSun May 24 06:00:29 2020 +0000 [34mGRAP Bot[32m [mrecurring_consignment_test 12.0.1.0.1
[33m1cb8bfb [31mSun May 24 06:00:29 2020 +0000 [34mGRAP Bot[32m [mrecurring_consignment_sale 12.0.1.0.1
[33me785ae8 [31mSun May 24 06:00:28 2020 +0000 [34mGRAP Bot[32m [m[UPD] README.rst
[33md7fec7a [31mSun May 24 06:00:25 2020 +0000 [34mGRAP Bot[32m [m[UPD] addons table in README.md
[33m088087e [31mSun May 24 05:46:30 2020 +0000 [34mGRAP Bot[32m [mMerge PR #18 into 12.0
[33me48e77f [31mMon Jan 6 15:49:32 2020 +0100 [34mSylvain LE GAL[32m [m[MIG] sale_recovery_moment: Migration to 12.0
[33mf2cf77e [31mMon Jan 6 15:49:31 2020 +0100 [34mSylvain LE GAL[32m [m[REF] sale_recovery_moment: Black python code
[33mf931ada [31mMon Jan 6 11:53:54 2020 +0100 [34mSylvain LE GAL[32m [m[MIG] stock_preparation_category: Migration to 12.0
[33mf825880 [31mMon Jan 6 11:53:54 2020 +0100 [34mSylvain LE GAL[32m [m[REF] stock_preparation_category: Black python code
[33m3a64466 [31mMon Jan 6 11:53:19 2020 +0100 [34mSylvain LE GAL[32m [m[WIP] stock_prepare_category
[33m8d83a0b [31mSat Apr 11 11:12:20 2020 +0200 [34mSylvain LE GAL[32m [m[ADD) allergens ; [UPD] fr translation ; [IMP] display of product labels
[33m1ff1aaf [31mFri Apr 10 21:12:13 2020 +0200 [34mSylvain LE GAL[32m [m[ADD] allergens items
[33m3910485 [31mFri Dec 20 16:14:19 2019 +0100 [34mSylvain LE GAL[32m [m[IMP] improve product_food product view
[33mdbe280f [31mMon Apr 27 14:22:59 2020 +0200 [34mQuentin Dupont[32m [m[FIX] weight field
[33maa3370f [31mWed Jan 29 17:07:54 2020 +0100 [34mQuentin Dupont[32m [m[FIX] Readme images
[33m137933f [31mWed Jan 8 11:24:45 2020 +0100 [34mQuentin Dupont[32m [msimplify css useless
[33m0943c04 [31mWed Jan 8 10:13:32 2020 +0100 [34mQuentin Dupont[32m [mfixes
[33ma347dae [31mTue Jan 7 17:06:08 2020 +0100 [34mQuentin Dupont[32m [mremove company id
[33m415b86b [31mTue Jan 7 16:53:58 2020 +0100 [34mQuentin Dupont[32m [majuste product print category
[33m86b4f51 [31mTue Jan 7 10:34:58 2020 +0100 [34mQuentin Dupont[32m [m[provisoire] oca dependencies for travis
[33m9eec432 [31mTue Jan 7 10:31:05 2020 +0100 [34mQuentin Dupont[32m [m[ADD] Food report with product_print_category
[33mc7cdefe [31mThu Mar 26 04:18:37 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] README.rst
[33mc85751c [31mThu Mar 26 04:18:31 2020 +0000 [34mGithub GRAP Bot[32m [m[UPD] addons table in README.md
[33m039445d [31mThu Mar 26 04:10:48 2020 +0000 [34mGithub GRAP Bot[32m [mMerge PR #25 into 12.0
[33mf34351c [31mThu Mar 26 04:53:03 2020 +0100 [34mSylvain LE GAL[32m [m[IMP] readme repository
[33mee87c9c [31mWed Dec 4 13:38:17 2019 +0100 [34mSylvain LE GAL[32m [m[MIG] recurring_consignment: Migration to 12.0
[33maa2175c [31mTue Jan 14 12:28:20 2020 +0100 [34mSylvain LE GAL[32m [mUpdate oca_dependencies.txt
[33m2de5629 [31mWed Jan 8 16:12:12 2020 +0100 [34mSylvain LE GAL[32m [m[REF] move pos_tare in OCA https://github.com/OCA/pos/pull/436
[33ma942f40 [31mMon Jan 6 10:57:10 2020 +0100 [34mSylvain LE GAL[32m [m8.0 imp sale eshop (#11)
[33m6457e50 [31mFri Dec 20 15:39:32 2019 +0100 [34mSylvain LE GAL[32m [m12.0 mig sale food (#19)
[33m3a1d584 [31mSat Nov 23 00:54:52 2019 +0100 [34mSylvain LE GAL[32m [mfixup! [MIG] product_category_recursive_property: Migration to 12.0
[33m7939277 [31mSat Nov 23 00:24:32 2019 +0100 [34mSylvain LE GAL[32m [m[MIG] product_category_recursive_property: Migration to 12.0
[33mba96fba [31mFri Nov 22 18:11:33 2019 +0100 [34mSylvain LE GAL[32m [mfixup! fixup! fixup! [MIG] purchase_package_qty: Migration to 12.0
[33mc5a1711 [31mFri Nov 22 14:33:35 2019 +0100 [34mSylvain LE GAL[32m [mfixup! fixup! [MIG] purchase_package_qty: Migration to 12.0
[33m60bb135 [31mFri Nov 22 14:25:24 2019 +0100 [34mSylvain LE GAL[32m [mfixup! [MIG] purchase_package_qty: Migration to 12.0
[33m6de589e [31mThu Nov 21 21:08:35 2019 +0100 [34mSylvain LE GAL[32m [m[MIG] purchase_package_qty: Migration to 12.0
[33m5a6d67f [31mThu Nov 21 21:05:39 2019 +0100 [34mSylvain LE GAL[32m [mfixup! fixup! [MIG] users_partners_access: Migration to 12.0
[33m1f811a8 [31mThu Nov 21 21:01:55 2019 +0100 [34mSylvain LE GAL[32m [mfixup! [MIG] users_partners_access: Migration to 12.0
[33m6d1f829 [31mThu Nov 21 20:37:33 2019 +0100 [34mSylvain LE GAL[32m [m[MIG] users_partners_access: Migration to 12.0
[33m6935137 [31mThu Nov 21 14:12:30 2019 +0100 [34mSylvain LE GAL[32m [m[INIT] repo V12
[33m675f40e [31mThu Nov 21 14:09:26 2019 +0100 [34mSylvain LE GAL[32m [m[REF] Update Travis file
[33mfc719c3 [31mThu Nov 21 14:08:09 2019 +0100 [34mSylvain LE GAL[32m [m[INIT] Branch V12. Disable modules
[33m5b09ec8 [31mMon Jul 29 12:47:40 2019 +0200 [34mSylvain LE GAL[32m [mUpdate .travis.yml
[33md6f0693 [31mMon Jul 29 12:02:32 2019 +0200 [34mSylvain LE GAL[32m [m[FIX] travis (postgresql)
[33m394a9c7 [31mWed Jul 10 10:51:20 2019 +0200 [34mSylvain LE GAL[32m [mwip - remove simple_tax_xxx (#9)
[33m8907655 [31mWed Jul 10 10:50:04 2019 +0200 [34mSylvain LE GAL[32m [mMerge pull request #8 from quentinDupont/8.0_IMP_avoid_divide_zero_error
[33mf9654bb [31mWed Jul 10 10:49:19 2019 +0200 [34mSylvain LE GAL[32m [mMerge pull request #6 from quentinDupont/8.0_IMP_notinvoice_consignor_purchase
[33mef0c5fc [31mMon Mar 4 12:27:19 2019 +0100 [34mQuentin Dupont[32m [m[8.0][IMP] patch to avoid zero division error
[33m610090c [31mTue Mar 26 17:49:57 2019 +0100 [34mSylvain LE GAL[32m [m[FIX] do not set required for new field, to avoid error on other module in demo mode.
[33md5223b9 [31mFri Feb 1 11:32:07 2019 +0100 [34mQuentin Dupont[32m [m[8.0][IMP] Purchase with consignor supplier are really not to be invoiced
[33mc637394 [31mThu Feb 7 18:37:06 2019 +0100 [34mSylvain LE GAL[32m [m[REF] readme
[33m38c6db5 [31mTue Feb 5 16:40:50 2019 +0100 [34mSylvain LE GAL[32m [m[REF] description
[33m93305e6 [31mTue Feb 5 16:05:35 2019 +0100 [34mSylvain LE GAL[32m [m[FIX] sale_recovery_moment bad import order
[33md083065 [31mTue Feb 5 13:24:59 2019 +0100 [34mSylvain LE GAL[32m [mMerge pull request #7 from legalsylvain/8.0_IMP_sale_recovery_moment_add_shipping_product
[33m7122fa7 [31mTue Feb 5 13:19:31 2019 +0100 [34mSylvain LE GAL[32m [mMerge pull request #3 from quentinDupont/8.0_IMP_trad_and_css
[33me521792 [31mFri Feb 1 18:14:57 2019 +0100 [34mSylvain LE GAL[32m [m[IMP] add shipping_product on sale.recovery.place
[33mbecbb36 [31mFri Feb 1 11:28:06 2019 +0100 [34mSylvain LE GAL[32m [m[FIX] restore possiblity to set images on eshop.category model
[33m684f521 [31mTue Jan 15 11:46:01 2019 +0100 [34mQuentin Dupont[32m [m[IMP] minor css et traduction
[33mceefd35 [31mMon Dec 17 17:54:27 2018 +0100 [34mSylvain LE GAL[32m [mMerge pull request #2 from quentinDupont/8.0_mass_change_bug
[33m6524075 [31mMon Dec 10 15:21:18 2018 +0100 [34mQuentin Dupont[32m [m[IMP] Change product_uos with mass change
[33m46b0d04 [31mFri Dec 7 17:03:55 2018 +0100 [34mSylvain LE GAL[32m [m[FIX] add tolerance to rounding method, to avoid floating rounding error
[33mcd4aa65 [31mTue Dec 4 16:51:30 2018 +0100 [34mSylvain LE GAL[32m [m[FIX] incorrect translation folder
[33mb5cf93a [31mTue Dec 4 12:18:28 2018 +0100 [34mSylvain LE GAL[32m [m[FIX] compatibility between sale_eshop and user_partner_access
[33m6830dcd [31mTue Dec 4 11:24:18 2018 +0100 [34mSylvain LE GAL[32m [m[FIX] do no send email in demo / test context
[33m4c4bed3 [31mTue Dec 4 03:37:09 2018 +0100 [34mSylvain LE GAL[32m [m[FIX] incorrect required value make travis failing (product.uom)
[33mca88029 [31mMon Dec 3 16:43:14 2018 +0100 [34mSylvain LE GAL[32m [m[FIX] incorrect required value make travis failing
[33m31b30b6 [31mMon Dec 3 16:23:14 2018 +0100 [34mSylvain LE GAL[32m [m[FIX] bad dependencies
[33m8995f1b [31mMon Dec 3 11:29:38 2018 +0100 [34mSylvain LE GAL[32m [m[REF] move sale_eshop from -misc to -business
[33m3815b50 [31mFri Nov 30 10:37:58 2018 +0100 [34mSylvain LE GAL[32m [m[IMP] description
[33m18d11f1 [31mThu Nov 29 18:57:50 2018 +0100 [34mSylvain LE GAL[32m [m[REF] readme files for stock_picking_type_image
[33mecd25c4 [31mThu Nov 29 18:57:41 2018 +0100 [34mSylvain LE GAL[32m [m[REF] readme files for stock_picking_type_image
[33me1994e0 [31mThu Nov 29 18:56:41 2018 +0100 [34mSylvain LE GAL[32m [m[REF] readme files for stock_picking_type_image
[33m8dd3ca4 [31mThu Nov 29 18:53:47 2018 +0100 [34mSylvain LE GAL[32m [m[REF] move two modules from -custom to -business
[33m44eeed3 [31mThu Nov 29 14:30:00 2018 +0100 [34mSylvain LE GAL[32m [m[REF] remove useless index html files
[33m7b9330a [31mThu Nov 29 14:29:05 2018 +0100 [34mSylvain LE GAL[32m [m[REF] remove useless file manage_recovery_moment, moved into sale_eshop
[33m84a155f [31mTue Nov 27 17:55:16 2018 +0100 [34mSylvain LE GAL[32m [mdescription
[33m11da4be [31mTue Nov 27 17:52:04 2018 +0100 [34mSylvain LE GAL[32m [mdescription
[33me28831c [31mTue Nov 27 17:49:02 2018 +0100 [34mSylvain LE GAL[32m [mdescription
[33mcad3b17 [31mTue Nov 20 12:12:25 2018 +0100 [34mSylvain LE GAL[32m [m[FIX] add hidden field to avoid not null error when validating. (weird Odoo ORM)
[33me07fbc3 [31mTue Nov 13 13:43:35 2018 +0100 [34mSylvain LE GAL[32m [mREF
[33m9b0ccce [31mTue Nov 13 13:15:47 2018 +0100 [34mSylvain LE GAL[32m [m[REF] move account_move_change_number from -grap into -business
[33mbc12afc [31mTue Nov 13 13:03:29 2018 +0100 [34mSylvain LE GAL[32m [m[REF] move users_partners_access from misc to business
[33m7611663 [31mTue Nov 13 12:45:52 2018 +0100 [34mSylvain LE GAL[32m [m[REF] move stock_picking_quick_edit and stock_picking_mass_change from odoo-addons-misc
[33mdb89c4e [31mWed Oct 31 18:17:44 2018 +0100 [34mSylvain LE GAL[32m [m[FIX] possibility to set the consignor in the supplier field. [IMP] auto assign suppliers onchange of consignors
[33me92a3fd [31mThu Jul 26 17:37:18 2018 +0200 [34mSylvain LE GAL[32m [m[FIX] travis
[33m0aa52ba [31mThu Jul 26 16:53:30 2018 +0200 [34mSylvain LE GAL[32m [m[REF] remove useless dependencies
[33m33e59ee [31mThu Jul 26 16:47:32 2018 +0200 [34mSylvain LE GAL[32m [m[REF] move module from grap-odoo-business
[33ma0f8415 [31mThu Jul 26 13:21:17 2018 +0200 [34mSylvain LE GAL[32m [mMerge pull request #1 from grap/8.0_ADD_account_product_fiscal_classification_restricted_usage
[33m57ff6cf [31mWed Jul 25 20:25:47 2018 +0200 [34mSylvain LE GAL[32m [m[FIX] remove useless files
[33m70219fe [31mWed Jul 25 20:15:44 2018 +0200 [34mSylvain LE GAL[32m [m[ADD] translation + [IMP] images
[33m5be8321 [31mWed Jul 25 20:06:37 2018 +0200 [34mSylvain LE GAL[32m [m[ADD] new module account_product_fiscal_classification_restricted_usage
[33m87b9c97 [31mWed Jul 25 20:25:06 2018 +0200 [34mSylvain LE GAL[32m [mUpdate .travis.yml
[33mf968a52 [31mTue Jul 17 10:27:35 2018 +0200 [34mSylvain LE GAL[32m [m[IMP] readme
[33m61d7615 [31mMon Jul 16 20:32:06 2018 +0200 [34mSylvain LE GAL[32m [m[REF] move product_taxes_group into odoo-addons-empty
[33me70fabf [31mFri Jul 13 21:32:18 2018 +0200 [34mSylvain LE GAL[32m [m[REF] move from odoo-addons-grap
[33m99a561a [31mWed Jul 11 18:01:34 2018 +0200 [34mSylvain LE GAL[32m [m[REF] still in grap-odoo-incubator
[33m3e605aa [31mTue Jul 10 11:00:17 2018 +0200 [34mSylvain LE GAL[32m [m[REF-WIP] product_simple_pricelist
[33m4aaaac2 [31mTue Jul 10 10:29:58 2018 +0200 [34mSylvain LE GAL[32m [m[REF] move product_simple_pricelist from odoo-addons-misc
[33m7252ec9 [31mTue Jul 10 10:27:26 2018 +0200 [34mSylvain LE GAL[32m [m[REF] light header
[33m4d56a5c [31mTue Jul 10 10:26:22 2018 +0200 [34mSylvain LE GAL[32m [m[REF] light header
[33m30bf804 [31mTue Jul 10 10:24:37 2018 +0200 [34mSylvain LE GAL[32m [m[MOVE] pos_tare
[33m43a9b8d [31mSun Jul 8 20:39:52 2018 +0200 [34mSylvain LE GAL[32m [m[TMP] disable recurring_consignment
[33mb880c1d [31mSun Jul 8 20:20:23 2018 +0200 [34mSylvain LE GAL[32m [m[ADD] test for purchase_package_qty
[33mb92607a [31mSun Jul 8 19:00:42 2018 +0200 [34mSylvain LE GAL[32m [m[REF] travis file + [FIX] flake8
[33md062d7c [31mFri Jul 6 02:29:56 2018 +0200 [34mSylvain LE GAL[32m [m[WIP] refactor purchase_package_qty
[33m0947e6a [31mWed Jul 4 17:03:14 2018 +0200 [34mSylvain LE GAL[32m [m[REF] move module purchase_package_qty from odoo-addons-cpo
[33m7167b15 [31mWed Jun 20 10:09:56 2018 +0200 [34mSylvain LE GAL[32m [m[FIX] add product_taxes_group security
[33m00cdfd2 [31mMon Jun 18 23:23:23 2018 +0200 [34mSylvain LE GAL[32m [m[PREPARE] migration product_taxes_group -> product_account_fiscal_classification
[33m105e425 [31mThu Jun 14 21:54:48 2018 +0200 [34mSylvain LE GAL[32m [m[IMP] add constrains for CRB people ;-)
[33md9d557a [31mThu Jun 14 21:23:48 2018 +0200 [34mSylvain LE GAL[32m [m[REF] recurring_consignement now depends on account_product_fiscal_classification
[33m5535ec6 [31mFri Jun 8 18:34:07 2018 +0200 [34mSylvain LE GAL[32m [m[REF] set copy=False to scale_group_id
[33m90fec52 [31mMon Jun 4 23:34:39 2018 +0200 [34mSylvain LE GAL[32m [m[ADD] file
[33m7d106bc [31mFri Jun 1 17:33:26 2018 +0200 [34mSylvain LE GAL[32m [m[FIX] flake8
[33mb3ae91d [31mFri Jun 1 15:24:36 2018 +0200 [34mSylvain LE GAL[32m [m[TEST] fucking pylint
[33m6807b15 [31mFri Jun 1 15:04:11 2018 +0200 [34mSylvain LE GAL[32m [m[TEST] travis
[33med95891 [31mFri Jun 1 14:11:12 2018 +0200 [34mSylvain LE GAL[32m [m[FIX] pylint
[33m3277363 [31mFri Jun 1 14:02:30 2018 +0200 [34mSylvain LE GAL[32m [m[FIX] flake8
[33m1d40b11 [31mFri Jun 1 13:57:41 2018 +0200 [34mSylvain LE GAL[32m [m[REF] move sale_recovery_moment from odoo-addons-misc
[33m66f019b [31mWed May 30 17:07:27 2018 +0200 [34mSylvain LE GAL[32m [m[ADD] constrains PoS in back office
[33m39d4b7e [31mTue Apr 24 13:26:44 2018 +0200 [34mSylvain LE GAL[32m [m[FIX] add new missingh files
[33mbb5e62b [31mTue Apr 24 12:39:14 2018 +0200 [34mSylvain LE GAL[32m [m[IMP] add security on commission product
[33md2a6a0f [31mTue Apr 24 12:00:14 2018 +0200 [34mSylvain LE GAL[32m [m[REF] remove for_consigned_product on pricelist and add alternative pricelist instead
[33mcbd7de0 [31mThu Apr 12 19:44:10 2018 +0200 [34mSylvain LE GAL[32m [m[FIX] incorrect call to log write
[33m9b8726e [31mThu Apr 12 19:24:16 2018 +0200 [34mSylvain LE GAL[32m [m[REF] restore expiration_date_day
[33mf0f69f3 [31mThu Apr 12 18:50:24 2018 +0200 [34mSylvain LE GAL[32m [m[FIX] bizerba
[33m2cd3fdd [31mThu Apr 12 14:39:02 2018 +0200 [34mSylvain LE GAL[32m [m[FIX] flake8
[33m04cc13a [31mThu Apr 12 14:13:23 2018 +0200 [34mSylvain LE GAL[32m [m[WIP] refactor product_to_scale_bizerba
[33m81064b5 [31mTue Mar 20 14:54:01 2018 +0100 [34mSylvain LE GAL[32m [m[FIX] add fresh_category
[33mf05c789 [31mWed Mar 14 14:45:31 2018 +0100 [34mSylvain LE GAL[32m [m[REF] product form
[33m4ed7650 [31mWed Mar 14 13:22:08 2018 +0100 [34mSylvain LE GAL[32m [m[REF] description
[33m6d37327 [31mWed Mar 14 13:21:49 2018 +0100 [34mSylvain LE GAL[32m [m[ADD] manage alcohol label
[33m33e7572 [31mTue Mar 13 21:22:01 2018 +0100 [34mSylvain LE GAL[32m [m[imp] description
[33m1558d8b [31mTue Mar 13 21:20:47 2018 +0100 [34mSylvain LE GAL[32m [m[imp] description
[33mef7414e [31mTue Mar 13 21:15:07 2018 +0100 [34mSylvain LE GAL[32m [m[ADD] description
[33m6ceedc4 [31mTue Mar 13 21:13:57 2018 +0100 [34mSylvain LE GAL[32m [m[ADD] description
[33m3630898 [31mTue Mar 13 21:12:48 2018 +0100 [34mSylvain LE GAL[32m [m[ADD] description
[33md0303b3 [31mTue Mar 13 19:57:10 2018 +0100 [34mSylvain LE GAL[32m [m[REF] finish refactoring
[33m8a5ac9f [31mTue Mar 13 17:48:35 2018 +0100 [34mSylvain LE GAL[32m [m[FIX] css import ; [FIX] add hook to populate new required fields
[33m4ed9766 [31mTue Mar 13 16:47:44 2018 +0100 [34mSylvain LE GAL[32m [m[WIP] refactor sale_food (and move from odoo-addons-misc
[33m3bf24dc [31mTue Mar 13 15:57:42 2018 +0100 [34mSylvain LE GAL[32m [m[WIP] move sale_food
[33m52b529c [31mFri Mar 9 01:59:41 2018 +0100 [34mSylvain LE GAL[32m [m[FIX] flake8
[33m94ba66b [31mFri Mar 9 01:02:55 2018 +0100 [34mSylvain LE GAL[32m [m[FIX] bad comparison if standard price are not correctly rounded
[33m7650ca1 [31mThu Mar 8 23:13:29 2018 +0100 [34mSylvain LE GAL[32m [m[ADD] Hook; [IMP] translation
[33mb20d5b7 [31mThu Mar 8 19:09:19 2018 +0100 [34mSylvain LE GAL[32m [mwip
[33m5022677 [31mThu Mar 8 16:25:30 2018 +0100 [34mSylvain LE GAL[32m [m[FIX] oca dependencies
[33m41a337a [31mThu Mar 8 16:24:32 2018 +0100 [34mSylvain LE GAL[32m [m[ADD] FINISH account_invoice_supplierinfo_update_standard_price
[33m79bbc55 [31mThu Mar 8 16:24:24 2018 +0100 [34mSylvain LE GAL[32m [m[ADD] FINISH account_invoice_supplierinfo_update_standard_price
[33m08f0b55 [31mThu Mar 8 15:45:33 2018 +0100 [34mSylvain LE GAL[32m [m[WIP] add account_invoice_supplierinfo_update_standard_price
[33mfafeaef [31mSat Mar 3 01:25:40 2018 +0100 [34mSylvain LE GAL[32m [m[FIX] set oldname to consignor_partner_id
[33m1fe1903 [31mFri Mar 2 18:23:37 2018 +0100 [34mSylvain LE GAL[32m [m[FIX] handle correctly 10% VAT
[33m9fa5755 [31mThu Mar 1 11:19:31 2018 +0100 [34mSylvain LE GAL[32m [m[REF] move recurring_consignment from incubator to business
[33mfeb3658 [31mThu Mar 1 11:17:24 2018 +0100 [34mSylvain LE GAL[32m [mdesc
[33me65c8f6 [31mThu Mar 1 10:59:05 2018 +0100 [34mSylvain LE GAL[32m [mInitial commit
