For more information about consigment see:
https://en.wikipedia.org/wiki/Consignment

This module manage recurring consignment: A product will allways be provided
by the same consignor and can not be provided by another way.

For other implementation of consigment you could see:

* (vendor_consignment_stock)[https://github.com/OCA/purchase-workflow];


**Functionality**

TODO :
- basic user can only change location and email.
Partner Model

* Add a 'is_consignor' field on Partner;

Product Model

* Add a consignor_partner_id field (res.partner), indicating which partner
  provide the product;
* if consignor_partner_id is defined:
    * The product can not have seller_ids defined;
    * The product has a special VAT defined;

TODO :

- Ajouter le justificatif de commission dans le mail à envoyer.
  (surcharger account.invoice ?)

- Ajouter blocage dans product. Interdire le changement de consignor, si
  il y a un stock move associé au produit.
  
- Créer nouveau module:
    * recurring_consignment_sale_margin
    * recurring_consignment_invoice_margin
    * recurring_consignment_pos_margin
