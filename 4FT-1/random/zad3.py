import random


def main():
    team = []
    team.append(["Name", "Level", "Power", "CritChance", "Dexterity"])
    for i in range(12):
        team.append([Name(), Level(), Power(), CritChance(), Dexterity()])
    for i in team:
        print(i)
def Name():
    names = ["Galahad", "Lancelot", "Gawain", "Percivale", "Lionell", "Tristram de Lyones", "Gareth", "Bleoberis", "Lacotemale Taile", "Lucan", "Polomedes", "Lamorak", "Bors de Ganis", "Safer", "Pelleas", "Kay", "Ector de Maris", "Dagonet", "Degore", "Brunor le Noir", "Lebius Desconneu", "Alymere", "Mordred"]
    return names[random.randint(0, len(names) - 1)]
def Level():
    return random.randint(1, 20)
def Power():
    return random.randrange(10, 100, 5)
def CritChance():
    return f"{random.random():.0%}"
def Dexterity():
    return f"{random.uniform(5.0, 15.0):.2f}"
main()