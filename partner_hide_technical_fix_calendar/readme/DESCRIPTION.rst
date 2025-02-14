This is a glue module to be installed when ``partner_hide_technical_abstract``
and ``calendar`` module are installed.

It avoid an hugly error in the ``_compute_meeting`` function, that are failing
due to an SQL request bad designed.
