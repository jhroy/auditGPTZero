# ©2023 Jean-Hugues Roy. GNU GPL v3.
# coding : utf-8

import openai, json, csv, time
from cleOpenAI import cle

openai.api_key = cle

fichIn = "textes_français.csv"
fichOut = "textes_français_avecGPT.csv"

f = open(fichIn)
textes = csv.reader(f)
next(textes)

for texte in textes:
	if texte[0] == "GPT-3":
		commande = "Rédigez, en français, pour un journal du Québec, {} d'une longueur d'environ 4500 à 5000 caractères, dont le titre est {}. Ne répétez pas les mêmes concepts (mots, verbes, idées) d'une phrase à l'autre. Ne pas inclure le titre dans votre texte.".format(texte[1],texte[3])

		rep = openai.Completion.create(
			model="text-davinci-003",
			prompt= commande,
			temperature = 0.0,
			max_tokens = 1500,
			top_p = 1.0,
			frequency_penalty = 0.0,
			presence_penalty = 0.0
		)

		articleGPT = rep["choices"][0]["text"]
		articleGPT = articleGPT.replace("\n", " ").replace("\xa0", " ")
		while "  " in articleGPT:
			articleGPT = articleGPT.replace("  ", " ")

		infos = [texte[0],texte[1],texte[2],texte[3],articleGPT,len(articleGPT)]

		time.sleep(5)

	elif texte[0] == "moitié":
		commande = "Complétez, en français, {} pour un journal du Québec dont le titre est {} et qui commence ainsi: «{}». Votre ajout doit faire environ 1500 à 2500 caractères. Ne pas répéter les mêmes concepts (mots, verbes, idées) d'une phrase à l'autre. Ne me fournissez que votre ajout.".format(texte[1],texte[3],texte[4])

		rep = openai.Completion.create(
			model="text-davinci-003",
			prompt= commande,
			temperature = 0.0,
			max_tokens = 1500,
			top_p = 1.0,
			frequency_penalty = 0.0,
			presence_penalty = 0.0
		)

		articleGPT = rep["choices"][0]["text"]

		articleFinal = texte[4] + " | " + articleGPT

		articleFinal = articleFinal.replace("\n", " ").replace("\xa0", " ")
		while "  " in articleFinal:
			articleFinal = articleFinal.replace("  ", " ")

		infos = [texte[0],texte[1],texte[2],texte[3],articleFinal,len(articleFinal)]
		
		time.sleep(5)

	else:
		articleOriginal = texte[4].replace("\n", " ").replace("\xa0", " ")
		while "  " in articleOriginal:
			articleOriginal = articleOriginal.replace("  ", " ").strip()

		infos = texte[:4]
		infos.append(articleOriginal)
		infos.append(len(articleOriginal))

	print(infos)

	he = open(fichOut,"a")
	ho = csv.writer(he)
	ho.writerow(infos)
