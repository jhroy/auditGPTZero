# ©2023 Jean-Hugues Roy. GNU GPL v3.
# coding : utf-8

import deepl, csv
from cleDeepL import cle

fIn = "textes_français_avecGPT.csv"
fOut = "textes_français_avecGPT_tradDeepL.csv"

trad = deepl.Translator(cle)

f = open(fIn)
textes = csv.reader(f)
next(textes)

n = nbcar = 0

for texte in textes:
	n += 1
	nbcar += len(texte[4])
	print(n,nbcar)

	resultat = trad.translate_text(texte[4], target_lang="EN-US")

	nouveauTexte = [texte[0],texte[1],texte[2],texte[3],resultat.text,len(resultat.text)]

	print(nouveauTexte)

	kirikou = open(fOut,"a")
	geant = csv.writer(kirikou)
	geant.writerow(nouveauTexte)

	print("•"*33)
