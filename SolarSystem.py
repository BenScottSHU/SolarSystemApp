class Planet:
    def __init__(self, name, mass_kg, distance_km, diameter_km, moon_count, moons):
        self.name = name
        self.mass_kg = mass_kg
        self.distance_km = distance_km
        self.diameter_km = diameter_km
        self.moon_count = moon_count
        self.moons = moons


PLANETS = [
    #information from science.nasa.gov
    Planet("Mercury", "3.3011×10^23kg", 58 , 4_879, 0, ()),
    Planet("Venus", "4.8675 × 10^24kg", 108, 12_104, 0, ()),
    Planet("Earth", "5.9722x10^24kg", 150, 12_756, 1, ("Moon")),
    Planet("Mars", "6.4171x10^23kg", 228, 6_779, 2, ("Phobus", "Deimos" )),
    Planet("Jupiter", "1.8982×10^27kg", 778, 139_820, 95, ("Io", "Europa", "Ganymede", "Callisto")),
    Planet("Saturn", "5.6834×10^26kg", 1434, 116_460, 146, ("Titan", "Enceladus", "Rhea", "Iapetus")),
    Planet("Uranus", "8.6810×10^25kg", 2871, 50_724, 28, ("Titania", "Oberon", "Umbriel", "Ariel", "Miranda")),
    Planet("Neptune", "1.02413×10^26kg", 4495, 49_244, 16, ("Triton", "Nereid", "Proteus", "Larissa")),
]


# --- TEST STAGE 1 ---
if __name__ == "__main__":
    print(f"Loaded {len(PLANETS)} planets successfully!")
    for planet in PLANETS:
        print(f"- {planet.name}, Mass: {planet.mass_kg}, Average distance from sun (million,km): {planet.distance_km}, Diameter: {planet.diameter_km}, Number of Moons: {planet.moon_count}, Sample moons: {planet.moons}")
