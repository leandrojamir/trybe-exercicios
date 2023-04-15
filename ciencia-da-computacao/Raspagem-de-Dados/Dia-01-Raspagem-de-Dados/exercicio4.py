# Implemente em: src/scrape.py
import requests
import parsel


# Exercício
# Baseando-se em uma página contendo detalhes sobre um livro
# (http://books.toscrape.com/catalogue/the-grand-design_405/index.html)
# dentro da função scrape que recebe uma URL como parâmetro
def scrape(url: str) -> str:
    # (http://books.toscrape.com/catalogue/the-grand-design_405/index.html)
    url = "http://books.toscrape.com/catalogue/the-grand-design_405/index.html"
    data = requests.get(url)

    # faça a extração dos campos título (".product_main > h1::text")
    titulo = parsel.Selector(data.text).css(".product_main > h1::text").get()

    # preço (".price_color::text")
    preco = (
        parsel.Selector(data.text).css(".price_color::text")
        # O preço deve vir somente valores numéricos e ponto.
        # Ex: Â£13.76 -> 13.76.
        # método re_first c/ expressão regular para capturar numero antes do .
        .re_first(r"\d*\.\d{2}")
    )

    # descrição (".sub-header ~ p::text")
    descricao = parsel.Selector(data.text).css(".sub-header ~ p::text").get()

    # A descrição deve ter o sufixo “more…” removido quando existir.
    if descricao.endswith("...more"):
        descricao = descricao[: -len("...more")]

    # e url contendo a imagem (".item active img::attr(src)")
    # De olho na dica: no retorno do caminho da imagem lembre-se de apresentar
    # também a constante URL_BASE que aponta para a página inicial do site.
    URL_BASE = "http://books.toscrape.com/catalogue/"
    url_image = (
        URL_BASE
        + parsel.Selector(data.text)
        # sugestão do video, pegar pelo ID=product_gallery com "#"
        .css("#product_gallery img::attr(src)").get()
    )

    # Os campos extraídos devem ser apresentados separados por vírgula.
    print(titulo, preco, descricao, url_image, sep=",")

    # o teste espera que url seja iterável
    # o erro era simplesmente porque esqueci do return
    return (titulo, preco, descricao, url_image)

    # Ex: título,preço,descrição,capa.
    # Exemplo:
    # The Grand Design,13.76,THE FIRST MAJOR WORK IN NEARLY A DECADE...,
    # http://books.toscrape.com/catalogue/../../media/cache/9b/69/9b696c2064d6ee387774b6121bb4be91.jpg


# mesmo com erro deu para perceber que o titulo e preço estão OK
# descrição sem inform—and provoke—like no other. ...more também OK
# imagem esta com url completa NOK
# utilizado URL_BASE = "http://books.toscrape.com/catalogue/" OK

# tests/test_scrape.py::test_scrape The Grand Design,13.76,THE FIRST MAJOR
# WORK IN NEARLY A DECADE BY ONE OF THE WORLDâS GREAT THINKERSâA MARVELOUSLY
# CONCISE BOOK WITH NEW ANSWERS TO THE ULTIMATE QUESTIONS OF LIFEWhen and how
# did the universe begin? Why are we here? Why is there something rather than
# nothing? What is the nature of reality? Why are the laws of nature so finely
# tuned as to allow for the existence of beings like ours THE FIRST MAJOR WORK
# IN NEARLY A DECADE BY ONE OF THE WORLDâS GREAT THINKERSâA MARVELOUSLY
# CONCISE BOOK WITH NEW ANSWERS TO THE ULTIMATE QUESTIONS OF LIFEÂ When and
# how did the universe begin? Why are we here? Why is there something rather
# than nothing? What is the nature of reality? Why are the laws of nature so
# finely tuned as to allow for the existence of beings like ourselves? And,
# finally, is the apparent âgrand designâor does science offer another
# explanation? The most fundamental questions about the origins of the
# universe and of life itself, once the province of philosophy, now occupy the
# territory where scientists, philosophers, and theologians meetâif only to
# disagree. In their new book, Stephen Hawking and Leonard Mlodinow present
# the most recent scientific thinking about the mysteries of the universe, in
# nontechnical language marked by both brilliance and simplicity. In The Grand
# Design they explain that according to quantum theory, the cosmos does not
# have just a single existence or history, but rather that every possible
# history of the universe exists simultaneously. When applied to the universe
# as a whole, this idea calls into question the very notion of cause and
# effect. But the âtop-downâmultiverseâthe idea that ours is just one of many
# universes that appeared spontaneously out of nothing, each with different
# laws of nature.Along the way Hawking and Mlodinow question the conventional
# concept of reality, posing a âmodel-dependentâtheory of everything.âand
# provokeâlike no other. ,
# http://books.toscrape.com/catalogue/the-grand-design_405/index.html../../media/cache/9b/69/9b696c2064d6ee387774b6121bb4be91.jpg
# FAILED

# no other. ,
# http://books.toscrape.com/catalogue/../../media/cache/9b/69/9b696c2064d6ee387774b6121bb4be91.jpg
# PASSED
