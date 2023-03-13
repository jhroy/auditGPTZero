# ©2023 Jean-Hugues Roy. GNU GPL v3.
# coding : utf-8

import json, requests, csv
from bs4 import BeautifulSoup

fichier = "jennifer-dowty.csv"

for n in range(0,300,20):
	# print(n)

	url = "https://www.theglobeandmail.com/pf/api/v3/content/fetch/content-search?query=%7B%22contentQuery%22%3A%22credits.by.name%253A%2522Jennifer%20Dowty%2522%2520OR%2520credits.by.slug%253A%2522jennifer-dowty%2522%22%2C%22from%22%3A{}%2C%22size%22%3A20%2C%22sort%22%3A%22display_date%3Adesc%22%7D&d=313&_website=tgam".format(n)

	tout = requests.get(url)
	articles = tout.json()

	for article in articles["content_elements"]:
		url2 = "https://www.theglobeandmail.com" + article["canonical_url"]
		date = article["display_date"]
		titre = article["headlines"]["basic"]

		print(url2)

		x = 0
		yo = requests.get(url2)
		page = BeautifulSoup(yo.text, "html.parser")

		skript = page.find("script", id="fusion-metadata").text
		sections = skript.split("Fusion")
		lejson = json.loads(sections[6].replace(".globalContent=","").strip(";"))

		texte = ""
		# print(type(lejson))
		for parag in lejson["content_elements"]:

			try:
				# print(parag["content"])
				if parag["content"] == "<b>TODAY'S HEADLINES</b>":
					x = 1
			except:
				pass
			try:
				if parag["content"][0] != "<" and x == 0:
					print(BeautifulSoup(parag["content"],"html.parser").text)
					texte = texte + BeautifulSoup(parag["content"],"html.parser").text + " "
			except:
				pass

		texte = texte.strip()
		print(len(texte))

		infos = ["Jennifer Dowty", url2, date, titre, texte]

		globe = open(fichier,"a")
		mail = csv.writer(globe)
		mail.writerow(infos)