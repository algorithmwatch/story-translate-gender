# Google Translate Audit

This code lets you check whether or not Google Translate translates phrases truthfully.

The file concepts.py contains the phrases to be tested.

The results are stored in a sqlite database.

## Usage

Install tor:

    sudo apt install tor

Start tor:

	tor --HTTPTunnelPort 8118

Run script:

	python3 scrape.py