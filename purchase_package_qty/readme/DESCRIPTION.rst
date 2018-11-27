This module extends the functionality of purchase module to support package
quantity.

In the product supplierinfo, add a "Qty per Package" field to register how many
purchase UoM of the product there are in the package the supplier uses.
All purchase lines for this product+supplier must have a quantity that is a
multiple of that package quantity.

For example:
I purchase beer bootles.
The supplier sells them with a price per unit, thus the purchase UoM is PCE.
But the supplier put them in 6pcs boxes, and I have to buy a multiple of 6.
