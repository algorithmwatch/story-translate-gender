from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys

from concepts import concepts
from translation_db import Translation, db

import time

# Makes a list of languages, removing English
languages = list(concepts[0].keys())
languages.remove('en')

# Connects over Tor
PROXY = "127.0.0.1:8118"
webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",

}

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

for source_lang in languages.copy():
	for target_lang in languages[:]:
		print("source: ", source_lang, " -- target_lang: ", target_lang)
		if target_lang != source_lang:
			url = "https://translate.google.com/#view=home&op=translate&sl=%s&tl=%s" % (source_lang, target_lang)

			driver.get(url)

			for concept in concepts:
				for gender in ["m", "f"]:

					phrase_source = concept[source_lang][gender][0]

					# Check if language pair is already in the DB
					query = Translation.select().where((Translation.source_lang == source_lang) 
						                             & (Translation.target_lang == target_lang)
						                             & (Translation.source_gender == gender)
						                             & (Translation.concept == concept['en']))

					if not query.exists():
						time.sleep(1)

						q = driver.find_element_by_id("source")

						q.clear()

						# Type in the query
						for letter in phrase_source:
						    q.send_keys(letter)
						    time.sleep(.05)

						time.sleep(3)

						a = driver.find_element_by_class_name("result-shield-container")

						translation = a.text

						# checks if translation is correct
						correct = 0
						if translation.lower() in (phrase.lower() for phrase in concept[target_lang][gender]):
							correct = 1

						# case for languages that do not have articles
						if source_lang in ["pl"]:
							for phrase in concept[target_lang][gender]:
								if translation.lower() in phrase.lower().replace("'", " ").split(" "):
									correct = 1

						verified = driver.find_element_by_class_name("trans-verified-button").is_displayed()

						print(source_lang, target_lang, verified)

						Translation(
								concept = concept['en'],
								source_lang = source_lang,
								source_gender = gender,
								target_lang = target_lang,
								original = phrase_source,
								translation = translation,
								verified = verified,
								correct = correct
							).save()

						time.sleep(2)

driver.close()
