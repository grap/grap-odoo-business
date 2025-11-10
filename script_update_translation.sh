#!/bin/bash
set -e

sudo chgrp -R odoo16 ./

# Install all modules
(cd ../../../ && odoo_16_run -d grap_business_all_modules -i grap_business_all_modules --stop-after-init)

# Update po / pot files
(cd cd ../../../ && sudo su odoo16 -c "./env/bin/python -m click_odoo_contrib.makepot -d grap_business_all_modules --addons-dir=/grap_dev/odoo_envs/grap-odoo-env-16.0/src/grap/grap-odoo-business --msgmerge --msgmerge-if-new-pot  --purge-old-translations -c ./odoo.cfg")

# Delete pot files
find . -name "*.pot" -type f -print0 | xargs -0 sudo /bin/rm -f
