This module adds to accountant users: - new write access on
`res.company` model, to be able to write on all the company related
fields. - new read access on `ir.module.module` model, to prevent error
in the execution of `res.config.settings` `create()` core function.
