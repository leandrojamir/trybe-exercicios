Para os exercícios você utilizará um dataset pequeno com alguns filmes. Para isso, conecte-se à sua instância e utilize o trecho de código abaixo para criar o banco de dados e inserir os documentos:

use cinema;
db.movies.drop();
db.movies.insertMany([
  {
    title: "Batman",
    category: [
      "action",
      "adventure",
    ],
    imdbRating: 7.7,
    budget: 35,
  },
  {
    title: "Godzilla",
    category: [
      "action",
      "adventure",
      "sci-fi",
    ],
    imdbRating: 6.6,
    budget: 1,
  },
  {
    title: "Home Alone",
    category: [
      "family",
      "comedy",
    ],
    imdbRating: 7.4,
  },
]);

Para cada execução, utilize o método find() para conferir as alterações nos documentos.

O MongoDB possui diversas ferramentas, como mongo, mongosh, Compass, além de outras ferramentas de terceiros. Você pode utilizar o que achar melhor para executar as queries. O importante é realizá-las.