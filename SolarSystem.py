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
    Planet("Earth", "5.9722x10^24kg", 150, 12_756, 1, ("Moon",)),
    Planet("Mars", "6.4171x10^23kg", 228, 6_779, 2, ("Phobus", "Deimos" )),
    Planet("Jupiter", "1.8982×10^27kg", 778, 139_820, 95, ("Io", "Europa", "Ganymede", "Callisto")),
    Planet("Saturn", "5.6834×10^26kg", 1434, 116_460, 146, ("Titan", "Enceladus", "Rhea", "Iapetus")),
    Planet("Uranus", "8.6810×10^25kg", 2871, 50_724, 28, ("Titania", "Oberon", "Umbriel", "Ariel", "Miranda")),
    Planet("Neptune", "1.02413×10^26kg", 4495, 49_244, 16, ("Triton", "Nereid", "Proteus", "Larissa")),
]

PLANET_TEXT_COLOURS = {
    "Mercury": "#555555",
    "Venus": "#9C5700",
    "Earth": "#176B2C",
    "Mars": "#B22222",
    "Jupiter": "#8B4513",
    "Saturn": "#806000",
    "Uranus": "#007C91",
    "Neptune": "#2446A6",
}


def show_planet(planet, details_label):
    sample_moons = ", ".join(planet.moons) if planet.moons else "None"
    details_label.config(
        text=(
            f"{planet.name}\n"
            f"Mass: {planet.mass_kg}\n"
            f"Average distance from the Sun: {planet.distance_km:,} million km\n"
            f"Diameter: {planet.diameter_km:,} km\n"
            f"Number of moons: {planet.moon_count}\n"
            f"Sample moons: {sample_moons}"
        )
    )


def answer_question(planet, question):
    question = question.lower()

    if any(word in question for word in ("diameter", "big", "size", "wide")):
        return f"{planet.name} is {planet.diameter_km:,} km in diameter."
    if any(word in question for word in ("distance", "far", "sun")):
        return (
            f"{planet.name} is an average of "
            f"{planet.distance_km:,} million km from the Sun."
        )
    if any(word in question for word in ("mass", "heavy", "weigh")):
        return f"The mass of {planet.name} is {planet.mass_kg}."
    if "moon" in question:
        sample_moons = ", ".join(planet.moons) if planet.moons else "None"
        return (
            f"{planet.name} has {planet.moon_count} moons. "
            f"Some known moons are: {sample_moons}."
        )
    return (
        "I can answer questions about size, distance from the Sun, mass, "
        "or moons. Try asking, for example, “How big is this planet?”"
    )


if __name__ == "__main__":
    import tkinter as tk

    root = tk.Tk()
    root.title("Planet Explorer")
    root.geometry("520x390")
    selected_planet = [None]

    buttons_frame = tk.Frame(root)
    buttons_frame.pack(pady=10)

    details_label = tk.Label(
        root,
        text="Click on a planet's button to see its information.",
        justify="left",
        anchor="w",
    )
    details_label.pack(fill="x", padx=20, pady=10)

    def select_planet(planet):
        selected_planet[0] = planet
        show_planet(planet, details_label)
        answer_label.config(text=f"Ask a question about {planet.name}.")

    for index, planet in enumerate(PLANETS):
        button = tk.Button(
            buttons_frame,
            text=planet.name,
            width=10,
            fg=PLANET_TEXT_COLOURS[planet.name],
            command=lambda selected=planet: select_planet(selected),
        )
        button.grid(row=index // 4, column=index % 4, padx=3, pady=5)

    question_label = tk.Label(root, text="Ask a question about the selected planet:")
    question_label.pack(anchor="w", padx=20, pady=(10, 2))

    question_entry = tk.Entry(root)
    question_entry.pack(fill="x", padx=20)

    answer_label = tk.Label(root, text="", justify="left", anchor="w", wraplength=480)
    answer_label.pack(fill="x", padx=20, pady=10)

    def search_question(event=None):
        if selected_planet[0] is None:
            answer_label.config(text="Select a planet first.")
            return

        input_widget = event.widget if event is not None else question_entry
        question = input_widget.get().strip()
        if not question:
            answer_label.config(text="Type a question first.")
            return

        answer_label.config(text=answer_question(selected_planet[0], question))

    search_button = tk.Button(root, text="Ask", command=search_question)
    search_button.pack(anchor="w", padx=20)
    question_entry.bind("<Return>", search_question)

    root.mainloop()
