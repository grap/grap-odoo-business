.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

=========
Sale Food
=========

This module extends the functionality of sale module to support food features.

# TODO
Allow users to put ethical notations on products and print pricetags
====================================================================

Functionnalities :
------------------
    * Add concept of label (organic, ...) and possibility to associate product
    to labels ;
    * Add notation on products and various information about origin, makers,
    etc...
TODO
----

new model:
* res.company.certification
    * company_id
    * organization_id
    * date_start (default = get last end date);
    * date_end (default = 31/12/Current_year);

* res.partner.certification
    * partner_id
    * organization_id
    * date_start (default = get last end date);
    * date_end (default = 31/12/Current_year);



Configuration
=============

To configure this module, you need to:

* Go to ...

.. figure:: path/to/local/image.png
   :alt: alternative description
   :width: 600 px

Usage
=====

To use this module, you need to:

* Go to ...


Known issues / Roadmap
======================

* ...

Credits
=======

Contributors
------------

* Julien WESTE
* Sylvain LE GAL (https://www.twitter.com/legalsylvain)

Do not contact contributors directly about support or help with technical issues.

Funders
-------

The development of this module has been financially supported by:

* GRAP, Groupement Régional Alimentaire de Proximité (http://www.grap.coop)
