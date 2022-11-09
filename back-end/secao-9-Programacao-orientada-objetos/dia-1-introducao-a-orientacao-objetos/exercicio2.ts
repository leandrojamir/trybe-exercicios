// Exercício 2
// Dentro da classe Tv, crie o método turnOn, que imprimirá os atributos inicializados no construtor.

class Tv {
  brand: string;
  size: number;
  resolution: string;
  connections: string[];
  connectedTo?: string;

  constructor(brand: string, size: number, resolution: string, connections: string[]) {
    this.brand = brand;
    this.size = size;
    this.resolution = resolution;
    this.connections = connections;
  }

  turnOn():void {
    console.log(
      `TV ${this.brand}, ${this.size}", resolution: ${this.resolution} \n\
  available connections: ${this.connections}`,
    );
  }
}