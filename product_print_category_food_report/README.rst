.. image:: https://img.shields.io/badge/licence-AGPL--3-blue.svg
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

===================
GRAP - QWeb Reports
===================

* Redefine default odoo qweb reports for GRAP.
* Add some computed field on models for that purpose.

Models changes
--------------

* account.invoice
    * add ```has_discount``` field

* account.tax
    * add ```report_short_code``` field

* product.product
    * add ```report_extra_food_info``` field that maps ```country_id``` and
      ```fresh_category``` field
    * add ```report_label_ids_info``` field that maps ```label_ids.code```
      field

report changes
--------------

* account.invoice
    * optionaly display ```discount``` column on invoice lines.
    * display short text for taxes.
    * display short text for labels.
    * allway display unit price vat Exlc.

* purchase.order
    * display short text for taxes.

* sale.order
    * display short text for taxes.

* pos.order bill
    * display VAT details
    * display customer name
    * display pricelist if it does'nt contain "catalogue in the name"

ROADMAP
--------

At the moment, price should not be longer than 4 numbers and one dot
→ When wkhtmltopdf will works with grid system, we would be able to use fit-content

INSTALL
---------


    Update WKHTMLTOPDF:

        I had version 0.12.1 so I updated to version 0.12.5

    A new System parameter:

        I added another System Parameter:

            Key: web.base.url.freeze

            Value: True

    Change my report definition:

  Utiliser web basic layout

  <t t-call="web.basic_layout">
        <t t-foreach="docs" t-as="objs">
            <div class="page">
                <!--REPORT CODE...-->
            </div>
        </t>
    </t>
</template>


BIEN NOMMER DIFFERENT LE PREMIER DIV POUR FAIRE LE CSS CAR TOUT EST PARTAGE APRES

Credits
=======

Contributors
------------

* Sylvain LE GAL <https://twitter.com/legalsylvain>

Funders
-------

* GRAP, Groupement Régional Alimentaire de Proximité <http://www.grap.coop>
