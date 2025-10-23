In Odoo, a user has a partner associated. This feature is great to
manage commun fields, but it generates a lot of undesired partners, and
change that technical partners could have undesired side effect.
(specially in multi company context, if a user of a company A, change
the data of a technical partner related to the partner B).

With this module, the users partners will not be accessible by default.
This will force saler / purchaser to create new partner. (if the user is
a customer or a supplier too)

Only members of 'Administration / Access Rights' can update those
partners.
