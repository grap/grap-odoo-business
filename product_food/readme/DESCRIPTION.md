This module extends the functionality of sale module to support food
features.

It provides a new model `product.allergen`

It also adds many fields on product models. (templates and variants)

- `is_alimentary`, boolean for analysis purpose.
- `best_before_date_day` that mentions for how many days a product can
  be eaten, after having packed. (for cheese, meats, etc.)
- `has_alcohol`, boolean to mention if the product contains alcohol.
- `allergen_ids` to mention the list of allergens.
- `ingredients`. (free text).

Alls the fields are defined on `product.product` model and can be set
also on `product.template` models, in a mono variant context.
