from collections import deque

potions = {
    "Brew of Immortality": 110,
    "Essence of Resilience": 100,
    "Draught of Wisdom": 90,
    "Potion of Agility": 80,
    "Elixir of Strength": 70
}

substances = [int(x) for x in input().split(", ")]
crystals = deque(int(x) for x in input().split(", "))

crafted = []
crafted_set = set()

while substances and crystals:

    substance = substances[-1]
    crystal = crystals[0]
    total_energy = substance + crystal

    possible = [
        (name, energy)
        for name, energy in potions.items()
        if energy <= total_energy and name not in crafted_set
    ]

    if any(energy == total_energy and name not in crafted_set
           for name, energy in potions.items()):
        for name, energy in potions.items():
            if energy == total_energy and name not in crafted_set:
                crafted.append(name)
                crafted_set.add(name)
                substances.pop()
                crystals.popleft()
                break

    elif possible:
        name, energy = max(possible, key=lambda x: x[1])
        crafted.append(name)
        crafted_set.add(name)
        substances.pop()
        crystals.popleft()
        new_energy = crystal - 20
        if new_energy > 0:
            crystals.append(new_energy)

    else:
        substances.pop()
        crystals.popleft()
        new_energy = crystal - 5
        if new_energy > 0:
            crystals.append(new_energy)

    if len(crafted) == 5:
        break

if len(crafted) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted:
    print(f"Crafted potions: {', '.join(crafted)}")

if substances:
    print(f"Substances: {', '.join(map(str, reversed(substances)))}")

if crystals:
    print(f"Crystals: {', '.join(map(str, crystals))}")
