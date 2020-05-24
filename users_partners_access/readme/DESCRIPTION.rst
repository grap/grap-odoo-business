In Odoo, a user has a partner associated. This feature is great to manage
commun fields, but generate some non desired behaviours in some multi company
cases:

If a user has multi company access, the company of the associated partner will
change when the user change company. So the associated partner will be
"available or not", depending of user configuration. This generates error
access.

With this module:

* the users partners will not be customer / supplier.
  This will force saler / purchaser to create new partner
  (if the user is a customer or a supplier too)

* the users partners will have no company, this will fix all bug access


**Technically**

All partners associated to a user:

* have ``customer``, ``supplier`` checkbox disabled;
* have ``company_id`` empty;

Only members of 'Administration / Access Rights' could update partners.
