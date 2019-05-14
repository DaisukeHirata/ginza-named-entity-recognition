import spacy
nlp = spacy.load('ja_ginza_nopn')

msg = '''
4月22日(月)、一般社団法人WAOJE TokyoによるWAOJE Tokyo Global Business Award 2019が開催され、

第2部講演である「注目の海外展開企業3社のパネルディスカッション」にて、
株式会社ネオキャリア代表取締役 西澤氏をファシリテーターとして、AnyMind Group CEO十河氏と共に弊社代表鮄川が登壇いたしました。  

■ノミネート企業 (五十音順)
株式会社I-ne／株式会社アイスタイル／株式会社ispace／AnyMindGroup／Omise Holdings Pte., Ltd.／株式会社テラモーターズ／株式会社ファインドスター／株式会社Preferred Networks／株式会社モンスター・ラボ／株式会社Liquid
'''
doc = nlp(msg)

# for sent in doc.sents:
#   for token in sent:
#     print(token.i, token.orth_, token.lemma_, token.pos_, token.dep_, token.head.i, token.tag_)
#   print('EOS')

for ent in doc.ents:
  print(ent.text, ent.start_char, ent.end_char, ent.label_)
print('EOS')

