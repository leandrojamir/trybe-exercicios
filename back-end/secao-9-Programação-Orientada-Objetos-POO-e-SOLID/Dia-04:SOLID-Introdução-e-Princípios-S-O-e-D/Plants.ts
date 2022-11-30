// Esse módulo controla um catálogo de plantas para um instituto de botânica. Você deverá usar o Typescript para adaptar o código de modo a transformá-lo em uma API respeitando os princípios SOLID. Para isso, você deverá modificar o arquivo Plants.ts, bem como criar um arquivo index.ts para criar sua API com Express.
// Foque nos princípios aprendidos hoje: Single Responsibility, Dependency Inversion e Open/Closed.
// Lembre-se de aproveitar os pilares da Orientação a Objetos quando precisar 😎
// Precisamos ter os endpoints:
// GET /plants: retorna todas as plantas;
// GET /plant/:id: retorna uma planta com o id;
// DELETE /plant/:id: deleta uma planta com o id;
// POST /plant/:id: sobrescreve a planta com id;
// POST /plant: cria uma planta nova;
// GET /sunny/:id: retorna uma planta que precisa de sol com o id.

import fs from 'fs/promises';
import { randomUUID } from 'crypto';
import path from 'path';

interface IPlant {
  id: string,
  breed: string,
  needsSun: boolean,
  origin: string,
  size: number,
  specialCare?: { waterFrequency: number }
}

interface IOpsInfo { createdPlants: number }

enum FileType {
  Plants,
  OpsInfo,
}

// callbacks
const plantsNeedSun = (id: string) => (plant: IPlant): boolean =>
  plant.id === id
    && plant.needsSun
    && (!plant.specialCare
      || plant.specialCare.waterFrequency > 2);

class Plants {
  private PLANTS_PATH = path.join(__dirname, 'plantsData.json');

  private OPS_INFO_PATH = path.join(__dirname, 'opsInfo.json');

  private async updateOpsInfo(incrementAmount = 1): Promise<void> {
    const opsInfoRaw = await fs.readFile(
      this.OPS_INFO_PATH,
      { encoding: 'utf8' },
    );
    const opsInfo: IOpsInfo = JSON.parse(opsInfoRaw);
    opsInfo.createdPlants += incrementAmount;
    this.saveFile(FileType.OpsInfo, opsInfo);
  }

  private async saveFile(type: FileType, data: IPlant[] | IOpsInfo) {
    let filePath: string;
    if (type === FileType.Plants) filePath = this.PLANTS_PATH;
    else if (type === FileType.OpsInfo) filePath = this.OPS_INFO_PATH;
    else return null;

    await fs.writeFile(filePath, JSON.stringify(data, null, 2));
  }

  public static initPlant(plant: IPlant): IPlant {
    const { id, breed, needsSun, origin, specialCare, size } = plant;

    const waterFrequency = needsSun
      ? size * 0.77 + (origin === 'Brazil' ? 8 : 7)
      : (size / 2) * 1.33 + (origin === 'Brazil' ? 8 : 7);

    const newPlant: IPlant = {
      id,
      breed,
      needsSun,
      origin,
      specialCare: {
        ...specialCare,
        waterFrequency,
      },
      size,
    };

    return newPlant;
  }

  public async getPlants(): Promise<IPlant[]> {
    const plantsRaw = await fs.readFile(this.PLANTS_PATH, { encoding: 'utf8' });
    const plants: IPlant[] = JSON.parse(plantsRaw);
    return plants;
  }

  public async getPlantById(
    id: string,
  ): Promise<IPlant | null> {
    const plants = await this.getPlants();

    const plantById = plants.find((plant) => plant.id === id);
    if (!plantById) return null;
    return plantById;
  }

  public async removePlantById(
    id: string,
  ): Promise<IPlant | null> {
    const plants = await this.getPlants();

    const removedPlant = plants.find((plant) => plant.id === id);
    if (!removedPlant) return null;

    const newPlants = plants.filter((plant) => plant.id !== id);
    this.saveFile(FileType.Plants, newPlants);

    await this.updateOpsInfo(-1);

    return removedPlant;
  }

  public async getPlantsThatNeedsSunWithId(
    id: string,
  ): Promise<IPlant[]> {
    const plants = await this.getPlants();

    const filteredPlants = plants.filter(plantsNeedSun(id));

    return filteredPlants;
  }

  public async editPlant(
    plantId: string,
    newPlant: IPlant,
  ): Promise<IPlant> {
    const plants = await this.getPlants();

    const updatedPlants = plants.map((plant) => {
      if (plant.id === plantId) return { ...newPlant, id: plant.id };
      return plant;
    });

    this.saveFile(FileType.Plants, updatedPlants);
    return newPlant;
  }

  public async savePlant(
    plant: IPlant,
  ): Promise<IPlant> {
    const plants = await this.getPlants();

    const newPlant = Plants.initPlant({ ...plant, id: randomUUID() });
    plants.push(newPlant);
    this.saveFile(FileType.Plants, plants);

    await this.updateOpsInfo(1);

    return newPlant;
  }
}

export default Plants;