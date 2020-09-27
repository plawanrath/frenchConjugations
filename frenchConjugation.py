"""
This is a simple script that can print the conjugations of French verbs.
Currently this script can open conjugations either in your browser
or in your terminal. In terminal it only supports 2 tenses Indicatif and Conditionnel
in all their forms. But it can be very easily extended to print out other tenses.

There are 2 modes to this script:
1. It will open https://www.the-conjugation.com/french/ in your browser and in there it will open the
        conjugations of the verb you provided.
    Requirements: This requires selenium package (pip install selenium)
                  This also requires chromedriver file (I have chrome driver exec for version 86 but you
                    might need to update the executable if your chrome version is something else.
    Usage: python frenchConjugation.py -w aller -b

2. This mode will print the conjugations in your terminal. This is the mode that currently only
supports Indicatif and Conditionnel.
    Requirements: This requires verbecc package (pip install verbecc)
    Usage: python frenchConjugation.py -w aller --conditionnel
           python frenchConjugation.py -w aller --indicatif --secondary-tense=présent
"""
from typing import Any, Dict
import time
import warnings
import argparse
from verbecc import Conjugator
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from constants import FRENCH_CONJUGATION
from constants import FRENCH
from constants import SECONDARY_TENSES
from constants import INDICATIF
from constants import CONDITIONNEL


def transform(conjugation: Dict[Any, Any], tense_primary: str = INDICATIF, tense_secondary: str = None) -> None:
    print('**********************************')
    print(tense_primary)
    print('**********************************')
    moods = conjugation['moods'][tense_primary]
    if tense_secondary:
        print('--------------------------------------')
        print(tense_secondary)
        print('--------------------------------------')
        verb_tenses = conjugation['moods'][tense_primary][tense_secondary]
        for vals in verb_tenses:
            print(vals)
    else:
        for key, value in moods.items():
            print('--------------------------------------')
            print(key)
            print('--------------------------------------')
            for vals in value:
                print(vals)


def openconjugation() -> None:
    parser = argparse.ArgumentParser(description="French Conjugation Tool")
    parser.add_argument(
        '-w',
        '--word',
        help='The French word you want conjugations for',
        required=True,
        type=str,
    )
    parser.add_argument(
        '--indicatif',
        help="Set if you only want to see the indicatif tenses",
        action="store_true",
    )
    parser.add_argument(
        '--conditionnel',
        help="Set if you only want to see the indicatif tenses",
        action="store_true",
    )
    parser.add_argument(
        '--secondary-tense',
        dest='secondary_tense',
        help="Set the secondary tense. For indicatif: présent, imparfait, "
             "futur-simple, passé-simple, passé-composé, plus-que-parfait,"
             " futur-antérieur, passé-antérieur \n For conditionnel: présent, passé",
        type=str,
        choices=sum(SECONDARY_TENSES.values(), []),
    )
    parser.add_argument(
        '-b',
        '--browser',
        help="Set to true if you want to open Conjugations in Chrome",
        action="store_true"
    )
    args = parser.parse_args()
    if args.browser:
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        window = webdriver.Chrome('./chromedriver', options=chrome_options)
        window.get(FRENCH_CONJUGATION)
        time.sleep(5)
        search_box = window.find_element_by_name("q")
        search_box.send_keys(args.word)
        search_box.submit()
    else:
        cg = Conjugator(lang=FRENCH)
        conjugation = cg.conjugate(args.word)
        if args.indicatif:
            if args.secondary_tense in SECONDARY_TENSES[INDICATIF]:
                transform(conjugation, tense_secondary=args.secondary_tense)
            else:
                transform(conjugation)
        elif args.conditionnel:
            if args.secondary_tense in SECONDARY_TENSES[CONDITIONNEL]:
                transform(conjugation, tense_primary=CONDITIONNEL, tense_secondary=args.secondary_tense)
            else:
                transform(conjugation, tense_primary='conditionnel')
        else:
            transform(conjugation)
            transform(conjugation, tense_primary='conditionnel')


if __name__ == '__main__':
    warnings.filterwarnings("ignore")
    openconjugation()
