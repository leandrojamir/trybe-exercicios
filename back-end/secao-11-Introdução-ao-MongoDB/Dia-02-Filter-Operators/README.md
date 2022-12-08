Antes de iniciar os exercícios
Para os exercícios a seguir, utilizaremos um banco de dados de super-heróis. Faça o download do arquivo JSON aqui.

Após fazer o download do arquivo, importe-o para o MongoDB através da ferramenta mongoimport. No seu terminal, utilize o seguinte comando (lembre-se de substituir <caminho do arquivo> pelo caminho do arquivo na sua máquina):

  mongoimport --db class --collection superheroes <caminho_do_arquivo>

Pronto! Você já tem uma base de dados com 734 super-heróis. Para conferir, conecte-se à instância do seu banco de dados utilizando o Mongo Shell e execute os seguintes comandos:

  use class;
  db.superheroes.countDocuments({});

Os documentos têm a seguinte estrutura:

{
    "_id" : ObjectId("5e4ed2b2866be74b5b26ebf1"),
    "name" : "Abin Sur",
    "alignment" : "good",
    "gender" : "Male",
    "race" : "Ungaran",
    "aspects" : {
        "eyeColor" : "blue",
        "hairColor" : "No Hair",
        "skinColor" : "red",
        "height" : 185,
        "weight" : 40.82
    },
    "publisher" : "DC Comics"
}