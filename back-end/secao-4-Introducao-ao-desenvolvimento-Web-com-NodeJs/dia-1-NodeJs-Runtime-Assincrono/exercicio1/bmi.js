// 🚀 Crie um código para calcular o índice de massa corporal(IMC) de uma pessoa.
// OBS: a sigla IMC, traduzida para o inglês, equivale a BMI(Body Mass Index). Vamos adotar este padrão nos códigos para começarmos a nos acostumar com o formado que aparecerá no mercado de trabalho!

// Armazene o código no arquivo bmi.js.
// A fórmula para calcular o IMC é weight / height ^ 2.
// Obs: Lembre-se que a altura é em metros, caso deseje usar em centímetros a conversão para metros será necessária.
// Comece criando um novo pacote Node com npm init e respondendo às perguntas do npm.
// Por enquanto, não se preocupe em pedir input do usuário. Utilize valores fixos para weight e height.

const weightInKg = 80; // Você pode utilizar o valor que desejar aqui
const heightInCm = 178; // Você pode utilizar o valor que desejar aqui

function handleBMI(weight, height) {
  console.log(`Weight: ${weight}, Height: ${height}`);

  const heightInMeters = height / 100;
  const heightSquared = heightInMeters ** 2;

  const bmi = height / heightSquared;
  
  return bmi;
}

// A função main é o ponto de partida do nosso programa
function main() {
  const bmi = handleBMI(weightInKg, heightInCm);

  console.log(`BMI: ${bmi.toFixed(2)}`);
}

main();
