# ©2023 Jean-Hugues Roy. GNU GPL v3.
# coding : utf-8

import json, requests, csv
from cleGPTZero import cle

fichiers = ["textes_français_avecGPT.csv", "textes_anglais_avecGPT.csv"]

for fichier in fichiers:
	f = open(fichier)
	textes = csv.reader(f)
	# next(textes)

	for texte in textes:
		document = texte[4]
		print(texte[:-2])

		url = "https://api.gptzero.me/v2/predict/text"
		headers = {
			"accept":"application/json",
			"X-Api-Key": cle,
			"Content-Type":"application/json"
		}
		data = {"document": document}

		r = requests.post(url, headers=headers, json=data)

		reponse = r.json()

		# print(reponse)

		perp = p = 0

		for phrase in reponse["documents"][0]["sentences"]:
			p += 1
			perp += phrase["perplexity"]

		perplexite = round((perp/p),2)

		prob_moy = reponse["documents"][0]["average_generated_prob"]
		prob_complete = reponse["documents"][0]["completely_generated_prob"]

		print(perplexite, prob_complete, prob_moy)

		infos = texte

		infos.append(perplexite)
		infos.append(prob_complete)
		infos.append(prob_moy)

		print(infos)
		
		etron = open(fichier.replace("avecGPT.csv","avecGPT_avecGPTZero.csv"),"a")
		musk = csv.writer(etron)
		musk.writerow(infos)

		print("~"*25)
