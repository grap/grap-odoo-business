import logging
import re

from bs4 import BeautifulSoup
from unidecode import unidecode

_logger = logging.getLogger(__name__)


def get_allergen_data(env, allergen_html, all_allergens):
    soup = BeautifulSoup(allergen_html, features="lxml")
    allergen_text = unidecode(soup.get_text(strip=True).lower())
    if not allergen_text:
        return False, False, False, False, False

    the_text = _clean_text(" " + allergen_text + " ")
    if "==TRACE==" in the_text:
        allergen_split = the_text.split("==TRACE==")
        allergen_part_text = allergen_split[0]
        allergen_trace_text = allergen_split[1]
        if len(allergen_split) > 2:
            _logger.info("WARNING, many 'trace' found")
    else:
        allergen_part_text = the_text
        allergen_trace_text = ""

    # Handle main allergens
    allergens, residual = _find_allergens(env, allergen_part_text, all_allergens)
    trace_allergens, trace_residual = _find_allergens(
        env, allergen_trace_text, all_allergens
    )
    return allergen_text, allergens, residual, trace_allergens, trace_residual


def _find_allergens(env, allergen_text, all_allergens):
    reg = r"-([Œ|\w]+)-"
    code_list = re.findall(reg, allergen_text)
    allergens = all_allergens.filtered(lambda x: x.code in code_list)
    residual = re.sub(reg, "", allergen_text).strip()
    return allergens, residual


def _clean_text(allergen_text):
    result = allergen_text
    for replace in _REPLACE:
        if type(replace) is list or type(replace) is tuple:
            result = re.sub(replace[0], replace[1], result)
        else:
            result = re.sub(replace, " ", result)
    return result


_REPLACE = [
    # Make 'trace' that is THE split
    (r"traces?", "==TRACE=="),
    # removal of punctuation
    r"\.",
    r"\,",
    r"\/",
    # ###############
    # Corner cases
    # ###############
    # beurre de cacao doesn't contain lactose
    r"\sbeurre de cacao\s",
    # ###############
    # ARACHIDE
    # ###############
    (r"arachides?", "-ARA-"),
    (r"cacahuetes?", "-ARA-"),
    # ###############
    # FRUITS A COQUES
    # ###############
    (r"fruits? a coques?", "-FAC-"),
    (r"amandes?", "-FAC-"),
    (r"noisettes?", "-FAC-"),
    (r"(noix de )?cajou", "-FAC-"),
    (r"noix de pecan", "-FAC-"),
    (r"noix de macadamia", "-FAC-"),
    (r"noix du bresil", "-FAC-"),
    (r"noix du queensland", "-FAC-"),
    (r"pistaches?", "-FAC-"),
    (r"noix", "-FAC-"),
    # ###############
    # GLUTEN
    # ###############
    (r"gluten", "-GLU-"),
    (r"\s(gluten de)?ble( dur)?\s", " -GLU- "),
    (r"seigle", "-GLU-"),
    (r"orge", "-GLU-"),
    (r"avoine", "-GLU-"),
    (r"epeautre", "-GLU-"),
    (r"kamut", "-GLU-"),
    (r"cereales?", "-GLU-"),
    # ###############
    # LAIT
    # ###############
    (r"lait", "-LAIT-"),
    (r"beurre", "-LAIT-"),
    (r"lactose", "-LAIT-"),
    # ###############
    # POISSONS
    # ###############
    (r"poissons?", "-POI-"),
    (r"thon", "-POI-"),
    # ###############
    # OTHER ALLERGENS
    # ###############
    (r"celeri(-rave)?", "-CEL-"),
    (r"crustaces?", "-CRU-"),
    (r"lupin", "-LUP-"),
    (r"(graines? de )?moutarde", "-MOU-"),
    (r"mollusques?", "-MOL-"),
    (r"oeufs?", "-ŒUF-"),
    (r"(graines? de )?sesame?", "-SES-"),
    (r"soja", "-SOJA-"),
    (r"sulfites?", "-SUL-"),
    # Remove little words
    r"\sl'",
    r"\sd'",
    r"\sles?\s",
    r"\sla\s",
    r"\sdes?\s",
    r"\sdu\s",
    r"\sune?\s",
    r"\set\s",
    r"\sou\s",
    # Remove recurring words
    r"\speut\s",
    r"\spresence\s",
    r"\scontenir\s",
    r"\scontient\s",
    r"\scontenant\s",
    r"\sfabrique\s",
    r"\sdans\s",
    r"\satelier\s",
    r"\squi\s",
    r"\sutilise\s",
    r"\spossibles?\s",
    r"\seventuelles?\s",
    r"\sautres?\s",
]
