# Google Translate Audit

This code lets you check whether or not Google Translate translates phrases truthfully.

The file concepts.py contains the phrases to be tested.

The results are stored in a sqlite database.

## Analysis

The data in the data forlder was checked and corrected by hand for additional translations that were not in the file concepts.py.

In the final analysis, the occupation of "computer scientist"was removed, because many forms of female computer scientist ("l'informatica" in Italian) are homographs of "computer science" ("l'informatica" in Italian).

## Usage

Install tor:

    sudo apt install tor

Start tor:

	tor --HTTPTunnelPort 8118

Run script:

	python3 scrape.py
