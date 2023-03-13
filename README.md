# GPTZero est-il efficace pour détecter l'utilisation de textes journalistiques créés en tout ou en partie avec ChatGPT?

Le [programme de journalisme de l'UQAM](https://journalisme.uqam.ca/) procèdera bientôt aux épreuves de sélection pour les personnes qui y font une demande d'admission. L'une de ses épreuves consiste à rédiger deux textes en réponse à deux questions, au choix, parmi une douzaine de questions sur l'actualité récente.

Mais voilà&nbsp;: les personnes candidates répondront à ces questions *à distance*. Comment vérifier si elles se seront servi de ChatGPT? Un outil, [GPTZero](https://gptzero.me/), prétend être en mesure de détecter les textes générés par des systèmes de rédaction automatique assistés par intelligence artificielle, comme ChatGPT.

L'expérience ci-dessous sert à vérifier l'efficacité de cet outil dans le cas de textes de nature journalistique rédigés en français.

## Étape 1

Pour la réaliser, j'ai confectionné trois corpus.

### 1 - 300 textes en français:
  * 100 textes récents de journalistes québécois:
    * 20 textes d'[Améli Pineda](https://www.ledevoir.com/auteur/ameli-pineda), journaliste judiciaire au *Devoir*, que j'ai moisonnés dans le cadre d'un exercice pour le cours de [journalisme de données II](https://journalisme-uqam.gitbook.io/edm4466-h2023/)
    * 20 textes d'[Emilie Nicolas](https://www.ledevoir.com/auteur/emilie-nicolas), chroniqueuse au *Devoir*, moissonnés par Sandrine Côté, étudiante en journalisme à l'UQAM
    * 20 textes de [Hugo Dumas](https://www.lapresse.ca/auteurs/hugo-dumas), chroniqueur télévision à *La Presse*, moissonnés par Marianne Dubé, étudiante en journalisme à l'UQAM
    * 20 textes de [Thomas Gerbet](https://ici.radio-canada.ca/profil/22553/thomas-gerbet), journaliste d'enquête à Radio-Canada, moissonnés par Jérémy L'Allier, étudiant en journalisme à l'UQAM, et moi
    * 20 textes d'[Éric Leblanc](https://www.rds.ca/experts/eric-leblanc-1.160032), chroniqueur à RDS, moissonnés par Siméon Dumont, étudiant en journalisme à l'UQAM, et moi
    
  * 100 textes générés par [GPT-3](https://platform.openai.com/docs/api-reference/completions) avec la commande suivante:
    * *Rédigez, en français, pour un journal du Québec, **{A}** d'une longueur d'environ 4500 à 5000 caractères, dont le titre est **{B}**. Ne répétez pas les mêmes concepts (mots, verbes, idées) d'une phrase à l'autre. Ne pas inclure le titre dans votre texte.*
    * Ici, {B} correspond au titre de 100 autres articles des cinq journalistes identifiés à l'étape précédente (20 chacun; les titres sont différents des articles colligés à cette étape précédente) et {A} correspond à un type de texte journalistique correspondant à leur spécialité:
      * «&nbsp;un reportage judiciaire&nbsp;», dans le cas d'un titre issu du moissonnage des textes d'Améli Pineda
      * «&nbsp;une chronique société&nbsp;», dans le cas d'un titre issu du moissonnage des textes d'Emilie Nicolas
      * «&nbsp;une chronique télévision &nbsp;», dans le cas d'un titre issu du moissonnage des textes de Hugo Dumas
      * «&nbsp;un reportage&nbsp;», dans le cas d'un titre issu du moissonnage des textes de Thomas Gerbet
      * «&nbsp;une chronique sportive &nbsp;», dans le cas d'un titre issu du moissonnage des textes d'Éric Leblanc
      
  * 100 textes générés *en partie* par [GPT-3](https://platform.openai.com/docs/api-reference/completions), avec la commande suivante:
    * *Complétez, en français, **{A}** pour un journal du Québec dont le titre est **{B}** et qui commence ainsi: «**{C}**». Votre ajout doit faire environ 1500 à 2500 caractères. Ne pas répéter les mêmes concepts (mots, verbes, idées) d'une phrase à l'autre. Ne me fournissez que votre ajout.*
    * Ici, {A} et {B} correspondent aussi à des types de texte et des titres issus des moissonnages des articles des cinq mêmes journalistes qu'aux étapes précédentes et {C} correspond à la première moitié d'un de leurs articles. GPT-3 devait compléter cet article.
    
### 2 - 300 textes en anglais:
  * 100 textes récents de journalistes du *Globe and Mail* sélectionnés au hasard:
    * 20 textes de la columnist culturelle [Johanna Schneller](https://www.theglobeandmail.com/authors/johanna-schneller/)
    * 20 textes du correspondant parlementaire [Ian Bailey](https://www.theglobeandmail.com/authors/ian-bailey/)
    * 20 textes du journaliste [Tu Thanh Ha](https://www.theglobeandmail.com/authors/tu-thanh-ha/), basé au Québec
    * 20 textes du chroniqueur [André Picard](https://www.theglobeandmail.com/authors/andre-picard/), spécialisé en santé
    * 20 textes de la chroniqueuse financière [Jennifer Dowty](https://www.theglobeandmail.com/authors/jennifer-dowty/)
    
  * 100 textes générés par GPT-3 avec la commande suivante:
    * *Write a 4500 to 5000-character **{A}** for a Canadian newspaper which title is **{B}**. Do not repeat similar concepts (words, verbs, ideas) one phrase to the next. Do not include the title in your output.*
    * Comme en français, les titres correspondent à d'autres textes rédigés par les mêmes journalistes et les types d'articles correspondent à leur spécialité respective (*Health story*, dans le cas des titres des articles d'André Picard, par exemple)
    
  * 100 textes générés *en partie* par GPT-3 avec la commande suivante:
    * *Complete the following **{A}** for a Canadian newspaper which title is **{B}** with 1500 to 2000 characters : «**{C}**». Do not repeat similar concepts (words, verbs, ideas) one phrase to the next. Only include your completion.*
    * Comme en français, les débuts de textes fournis à GPT-3 correspondent à des textes différents des textes utilisés aux étapes précédentes. Ils ont été rédigés par les mêmes cinq journalistes du *Globe and Mail*.
    
### 3 - 300 textes traduits en anglais
  * Afin de comparer les performances de GPTZero avec des textes en français et en anglais, les 300 textes en français du premier corpus ont été traduits en anglais à l'aide de [DeepL](https://www.deepl.com/pro-api).

## Étape 2

J'ai ensuite soumis les textes de chacun de ces trois corpus à GPTZero. Dans ses résultats, GPTZero donne trois variables&nbsp;:

* *Perplexity* : Décrit par l'auteur de GPTZero comme un indice du caractère aléatoire d'un texte
* `completely_generated_prob` : Décrit par l'auteur de GPTZero comme un indice *that specifies the probability the entire document was AI-generated*. Il recommande d'ailleurs de se servir surtout de cet indice&nbsp;: *using this score when deciding whether or not there is a significant use of AI in generating the text*.
* `average_generated_prob` : GPTZero mesure également, pour chacune des phrases dans un texte, la probabilité qu'elle soit produite par un système d'IA. L'indice `average_generated_prob` fait la moyenne de ces indices pour toutes les phrases.

## Résultats

Première constatation : GPTZero ne fonctionne pas avec des textes en français. Le tableau ci-dessous répartit les scores moyens de la variable `completely_generated_prob`, qui est une évaluation de la probabilité qu'un texte ait été rédigé par GPT-3 ou ChatGPT, pour chacun des sous-groupes de mon échantillon.

| **Rédigé par :point_down: \\ Corpus :point_right:**         | **Corpus de textes<br>en français** | **Corpus de textes<br>en anglais** | **Corpus de textes<br>en français<br>traduits en anglais** | **Ensemble des corpus** |
|----------------------------------|----------:|--------:|--------:|--------:|
| Journaliste                      | 0,0000 %  | 3,66 %  | 4,22 %  | 2,63 %  |
| Moitié journaliste, moitié GPT-3 | 0,0000 %  | 21,63 % | 23,69 % | 15,11 % |
| GPT-3                            | 0,0098 %  | 91,43 % | 70,06 % | 53,83 % |
| *Ensemble des rédacteurs•trices* | *0,0033 %* | *38,90 %* | *32,66 %* | *23,85 %* |

### Textes en français

On voit que les scores du corpus de textes en français sont faméliques. GPTZero considère qu'ils ont tous été rédigés par un être humain.

Cela dit, quand on classe les textes en français en fonction du score que leur a attribué GPTZero, les 18 textes qui ont obtenu les scores les plus élévés pour la variable `completely_generated_prob` ont été rédigés par GPT-3 en tout ou en partie.

Quand on les classe **en fonction de la perplexité**, ce sont les 78 textes obtenant le score le plus faible qui ont été rédigés par GPT-3 en tout ou en partie. Cette variable semble donc meilleure pour détecter l'utilisation de l'IA générative. Je vais donc m'en servir pour sépare les 300 textes en cinq quintiles en fonction de cette variable&nbsp;:
 * Le premier quintile des scores de perplexité les plus faibles sera constitué des 60 textes dont GPTZero estime qu'ils ont été très probalement été rédigé par une machine.
 * À l'autre extrême, le dernier quintile des scores de perplexité les plus élevés sera constitué des 60 textes dont GPTZero estime qu'ils ont été très probablement été rédigés par un être humain.

 L'ensemble des textes est réparti par quintile et par «&nbsp;auteur•trice&nbsp;» dans le tableau suivant.

| **Quintile (selon perplexité) :point_down: \\ Rédigé par :point_right:**       | **Journaliste** | **Moitié journaliste,<br>moitié GPT-3** | **GPT-3** | **_Total_** |
|----------------|--------------:|-------------------------------:|------:|---------------:|
| 1 - Texte très probablement rédigé par une machine    |  1 | 14 | 45 | _60_ |
| 2 - Texte probablement rédigé par une machine         |  7 | 27 | 26 | _60_ |
| 3 - Texte impossible à classer                           | 21 | 26 | 13 | _60_ |
| 4 - Texte probablement rédigé par un être humain      | 27 | 19 | 14 | _60_ |
| 5 - Texte très probablement rédigé par un être humain | 44 | 14 |  2 | _60_ |
| _Total_ | _100_           | _100_ | _100_     | _300_            |

Les faux positifs (ou faux négatifs) sont les suivants:
* Le texte classé comme étant très probablement rédigé par une machine, mais rédigé en fait par un humain, est [une chronique d'Éric Leblanc](https://www.rds.ca/hockey/canadiens/mailloux-assure-tout-faire-pour-devenir-une-meilleure-personne-1.15953395)
* Les textes inversement classés comme étant très probablement rédigés par un être humain, mais générés par GPT-3, avaient pour titre  *Mamadi Camara et ses proches poursuivent le SPVM et le DPCP pour 1,2 million de dollars* et *LAH : Xavier Simoneau ne recule pas devant des géants, il inspire déjà ses coéquipiers du Rocket*. Il est particulièrement étonnant que ce dernier texte ait été classé ainsi, car il s'achève par une série de phrases très semblables et répétitives&nbsp;:
```Xavier Simoneau est un jeune joueur très talentueux qui a déjà fait ses preuves dans la LAH. Il est très motivé et a le désir de devenir le meilleur joueur possible. Il est un leader par l'exemple et il inspire ses coéquipiers. Il est très respectueux et sait comment motiver ses coéquipiers. Xavier Simoneau est un jeune joueur très talentueux qui a déjà fait ses preuves dans la LAH. Il est le plus jeune capitaine de l'histoire de la ligue et il est très bien placé pour devenir un joueur étoile. Il est un leader par l'exemple et il inspire ses coéquipiers. Il est très conscient de ses responsabilités et sait comment les assumer. Xavier Simoneau est un jeune joueur très talentueux qui ne recule pas devant des géants. Il est très athlétique et a une excellente vision du jeu. Il est très intelligent et sait comment tirer le meilleur parti de ses coéquipiers.```

### Textes français traduits en anglais

GPTZero donne-t-il des résultats plus convaincants si on traduit des textes du français vers l'anglais? Si on répartit les résultats en quintiles en fontion du score de perplexité, il semble que oui.

| **Quintile (selon perplexité) :point_down: \\ Rédigé par :point_right:**       | **Journaliste** | **Moitié journaliste,<br>moitié GPT-3** | **GPT-3** | **_Total_** |
|----------------|--------------:|-------------------------------:|------:|---------------:|
| 1 - Texte très probablement rédigé par une machine    |  0 | 8 | 52 | _60_ |
| 2 - Texte probablement rédigé par une machine         |  4 | 27 | 29 | _60_ |
| 3 - Texte impossible à classer                           | 17 | 30 | 13 | _60_ |
| 4 - Texte probablement rédigé par un être humain      | 38 | 17 | 5 | _60_ |
| 5 - Texte très probablement rédigé par un être humain | 41 | 18 |  1 | _60_ |
| _Total_ | _100_           | _100_ | _100_     | _300_            |

Le seul faux négatif (texte classé comme très probablement rédigé par un humain, mais ayant été entièrement rédigé par GPT-3) avait pour titre *Big Brother Célébrités | Un McTrio pour une double-double élimination*.

Les quatre faux positifs (textes classés comme probablement rédigés par une machine, mais en réalité rédigés par des journalistes) sont:
* [Cette chronique d'Emilie Nicolas](https://ledevoir.com/opinion/chroniques/748797/chronique-la-haine-tranquille) et
* Trois reportages d'Améli Pineda: [celui-ci](https://www.ledevoir.com/societe/613263/agression-sexuelle-le-processus-judiciaire-a-ete-reparateur-pour-lea-clermont-dion), [celui-ci](https://www.ledevoir.com/societe/589799/profilage-racial-la-police-de-repentigny-se-veut-plus-inclusive) et [celui-là](https://www.ledevoir.com/societe/587599/poursuite-quebec-jean-charest)


### Textes en anglais

La répartition des textes en anglais montre encore plus clairement que GPTZero est conçu pour traiter des textes dans la langue de Hunter S. Thompson.

| **Quintile (selon perplexité) :point_down: \\ Rédigé par :point_right:**       | **Journaliste** | **Moitié journaliste,<br>moitié GPT-3** | **GPT-3** | **_Total_** |
|----------------|--------------:|-------------------------------:|------:|---------------:|
| 1 - Texte très probablement rédigé par une machine    |  0 | 1 | 59 | _60_ |
| 2 - Texte probablement rédigé par une machine         |  2 | 26 | 32 | _60_ |
| 3 - Texte impossible à classer                           | 18 | 33 | 9 | _60_ |
| 4 - Texte probablement rédigé par un être humain      | 37 | 23 | 0 | _60_ |
| 5 - Texte très probablement rédigé par un être humain | 43 | 17 |  0 | _60_ |
| _Total_ | _100_           | _100_ | _100_     | _300_            |

Et quand on répartit les quintiles en fontion de la variable proposée par le créateur de GPTZero, `completely_generated_prob`, l'outil donne des résultats à peu près semblables.

| **Quintile (selon `completely_generated_prob`) :point_down: \\ Rédigé par :point_right:**       | **Journaliste** | **Moitié journaliste,<br>moitié GPT-3** | **GPT-3** | **_Total_** |
|----------------|--------------:|-------------------------------:|------:|---------------:|
| 1 - Texte très probablement rédigé par une machine    |  0 |  2 | 58 | _60_ |
| 2 - Texte probablement rédigé par une machine         |  4 | 19 | 37 | _60_ |
| 3 - Texte impossible à classer                        | 18 | 37 |  5 | _60_ |
| 4 - Texte probablement rédigé par un être humain      | 19 | 31 |  0 | _60_ |
| 5 - Texte très probablement rédigé par un être humain | 49 | 11 |  0 | _60_ |
| _Total_ | _100_           | _100_ | _100_     | _300_            |

J'ai réparti les textes des deux précédents corpus en fonction de cette variable et on trouve encore plus de faux négatifs et de faux positifs que si on effectue la répartition par la perplexité.

## Conclusion

Pour détecter si des textes en français ont été fabriqués à l'aide de ChatGPT ou de GPT-3, GPTZero n'est pas utile. Si on traduit ces textes en anglais, on améliore ses performances qui se rapprochent de ce qu'on obtient avec des textes rédigés directement en anglais. Mais on ne réussit jamais à être absolument certain qu'un texte a été généré par un système reposant sur l'IA.

Au mieux, on peut classer un groupe de textes en fonction de différents scores fournis par GPTZero et s'intéresser aux premier quintile des textes obtenant les plus faibles scores de perplexité ou les plus grands scores de la variable `completely_generated_prob`. Il faut au préalable les traduire en anglais.

## Méthodologie (code et données)

* Les articles ayant servi à cette expérience ont été moissonnés à l'aide de la bibliothèque python [BeautifulSoup](https://bit.ly/jhroybs4). Voici un exemple d'un script ayant permis de recueillir un échantillon des 300 textes les plus récents de la journaliste Jennifer Dowty à partir d'un API non-documenté du *Globe and Mail*: [**globe-dowty.py**](globe-dowty.py)

* Pour chaque journaliste, 60 textes étaient aléatoirement sélectionnés&nbsp;: 20 conservés entièrement (rédigés par *journaliste*); 20 conservés partiellement (rédigés *moitié moitié*); 20 dont on ne conservait que le titre (rédigés par *GPT-3*). 

* Les textes générés par GPT-3 l'ont été à l'aide du script [**redaction.py**](redaction.py) Dans ceux qui étaient rédigés *moitié moitié*, le début est rédigé par des journalistes et la partie se trouvant après le symnbole **`|`** est générée par GPT-3.

* Les textes traduits du français vers l'anglais l'ont été grâce à ce script: [**trad.py**](trad.py)

* Enfin, tous les textes ont été soumis à GPTZero à l'aide du script [**triche.py**](triche.py)

* Le corpus complet et les résultats fournis par GPTZero se trouve dans le fichier [**corpusComplet_avecURL.csv**](corpusComplet_avecURL.csv)
