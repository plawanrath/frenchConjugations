This is a simple script that can print the conjugations of French verbs.
Currently this script can open conjugations either in your browser
or in your terminal. In terminal it only supports 2 tenses Indicatif and Conditionnel
in all their forms. But it can be very easily extended to print out other tenses.

There are 2 modes to this script:
1. It will open https://www.the-conjugation.com/french/ in your browser and in there it will open the
        conjugations of the verb you provided.
    Requirements: This requires selenium package (`pip install selenium`)
                  This also requires chromedriver file (I have chrome driver exec for version 86 but you
                    might need to update the executable if your chrome version is something else.
    <br/><br/>Usage: <br/>`python frenchConjugation.py -w aller -b`

2. This mode will print the conjugations in your terminal. This is the mode that currently only
supports Indicatif and Conditionnel.
    Requirements: This requires verbecc package (`pip install verbecc`)
    <br/><br/>Usage: <br/>`python frenchConjugation.py -w aller --conditionnel`
           <br/>`python frenchConjugation.py -w aller --indicatif --secondary-tense=présent`