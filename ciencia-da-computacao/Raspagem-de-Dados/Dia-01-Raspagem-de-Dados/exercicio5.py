#  Exercício 5:
# Modifique o exercício anterior para retornar também quantos livros estão
# disponíveis, apresentando como último campo no retorno.

# Exemplo:
# The Grand Design,13.76,THE FIRST MAJOR WORK IN NEARLY A DECADE BY ONE OF THE
# WORLDâS GREAT THINKERSâA MARVELOUSLY CONCISE BOOK WITH NEW ANSWERS TO THE
# ULTIMATE QUESTIONS OF LIFEWhen and howdid the universe begin? Why are we
# here? Why is there something rather than nothing? What is the nature of
# reality? Why are the laws of nature so finely tuned as to allow for the
# existenceof beings like ours THE FIRST MAJOR WORK IN NEARLY A DECADE BY ONE
# OF THE WORLDâS GREAT THINKERSâA MARVELOUSLY CONCISE BOOK WITH NEW ANSWERS TO
# THE ULTIMATE QUESTIONS OF LIFEÂ When and howdid the universe begin? Why are
# we here? Why is there something rather than nothing? What is the nature of
# reality? Why are the laws of nature so finely tuned as to allow for the
# existenceof beings like ourselves? And, finally, is the apparent âgrand
# designâor does science offer another explanation? The most fundamental
# questions about the origins of the universe and of lifeitself, once the
# province of philosophy, now occupy the territory where scientists,
# philosophers, and theologians meetâif only to disagree. In their new book,
# Stephen Hawking and LeonardMlodinow present the most recent scientific
# thinking about the mysteries of the universe, in nontechnical language
# marked by both brilliance and simplicity. In The Grand Design they
# explainthat according to quantum theory, the cosmos does not have just a
# single existence or history, but rather that every possible history of the
# universe exists simultaneously. When applied tothe universe as a whole, this
# idea calls into question the very notion of cause and effect. But the
# âtop-downâmultiverseâthe idea that ours is just one of many universes that
# appearedspontaneously out of nothing, each with different laws of nature.
# Along the way Hawking and Mlodinow question the conventional concept of
# reality, posing a âmodel-dependentâtheory ofeverything.âand provokeâlike no
# other. ,
# http://books.toscrape.com/catalogue/../../media/cache/9b/69/9b696c2064d6ee387774b6121bb4be91.jpg,5

# Importe o arquivo books.json no MongoDB antes de responder as próximas
# questões.

# 🦜 Comando usado para instalação local do mongo

# mongoimport --db library --jsonArray books.json

# 🐋 Deixamos abaixo os comandos para usar no Docker caso já tenha baixado a
# imagem do mongo e criado o container

# docker cp books.json <container-name-or-id>:/tmp/books.json
# docker exec <container-name-or-id> mongoimport --db library --jsonArray
# --file /tmp/books.json

import requests
import parsel

URL_BASE = "http://books.toscrape.com/catalogue/"
response = requests.get(URL_BASE + "the-grand-design_405/index.html")
selector = parsel.Selector(response.text)

title = selector.css("h1::text").get()

price = selector.css(".product_main > .price_color::text").re_first(
    r"\d*\.\d{2}"
)

description = selector.css("#product_description ~ p::text").get()
suffix = "...more"
if description.endswith(suffix):
    description = description[: -len(suffix)]

cover = URL_BASE + selector.css("#product_gallery img::attr(src)").get()
availability = selector.css(".product_main .availability::text").re_first("\d")

print(title, price, description, cover, availability, sep=",")
