import tkinter as tk


# Stores the facts for one planet.
class Planet:
    def __init__(
        self,
        name,
        mass_earths,
        distance_km,
        diameter_km,
        moon_count,
        moons,
        text_colour,
    ):
        self.name = name
        self.mass_earths = mass_earths
        self.distance_km = distance_km
        self.diameter_km = diameter_km
        self.moon_count = moon_count
        self.moons = moons
        self.text_colour = text_colour


# Holds the planet facts used by the app.
PLANETS = [
    # Distances are average distances from the Sun, measured in millions of km.
    Planet("Mercury", 0.055274, 58, 4_879, 0, (), "#555555"),
    Planet("Venus", 0.81503, 108, 12_104, 0, (), "#9C5700"),
    Planet("Earth", 1.0, 150, 12_756, 1, ("Moon",), "#176B2C"),
    Planet("Mars", 0.10745, 228, 6_779, 2, ("Phobus", "Deimos"), "#B22222"),
    Planet("Jupiter", 317.84, 778, 139_820, 95, ("Io", "Europa", "Ganymede", "Callisto"), "#8B4513"),
    Planet("Saturn", 95.164, 1434, 116_460, 146, ("Titan", "Enceladus", "Rhea", "Iapetus"), "#806000"),
    Planet("Uranus", 14.536, 2871, 50_724, 28, ("Titania", "Oberon", "Umbriel", "Ariel", "Miranda"), "#007C91"),
    Planet("Neptune", 17.148, 4495, 49_244, 16, ("Triton", "Nereid", "Proteus", "Larissa"), "#2446A6"),
]


# Displays a planet's mass in Earth-mass units.
def format_mass(mass_earths):
    unit = "Earth" if mass_earths == 1 else "Earths"
    return f"{mass_earths:g} {unit}"


# Answers questions that compare planets or ask about Pluto.
def answer_general_question(question):
    question = question.lower()

    if "pluto" in question:
        return (
            "Pluto got reclassified as a dwarf planet in 2006. "
            "Pluto is about half the size of the USA, but is still a part of our solar system"
        )

    if any(word in question for word in ("heaviest", "most massive", "mass", "weight")):
        planet = max(PLANETS, key=lambda item: item.mass_earths)
        return (
            f"{planet.name} is the heaviest planet, with a mass of "
            f"{format_mass(planet.mass_earths)}."
        )
    if any(word in question for word in ("lightest", "least massive")):
        planet = min(PLANETS, key=lambda item: item.mass_earths)
        return (
            f"{planet.name} is the lightest planet, with a mass of "
            f"{format_mass(planet.mass_earths)}."
        )

    if any(word in question for word in ("furthest", "farthest", "most distant")):
        planet = max(PLANETS, key=lambda item: item.distance_km)
        return (
            f"{planet.name} is furthest from the Sun, at an average distance "
            f"of {planet.distance_km:,} million km."
        )
    if any(word in question for word in ("nearest", "closest")):
        planet = min(PLANETS, key=lambda item: item.distance_km)
        return (
            f"{planet.name} is closest to the Sun, at an average distance "
            f"of {planet.distance_km:,} million km."
        )

    if "moon" in question and any(word in question for word in ("most", "many")):
        planet = max(PLANETS, key=lambda item: item.moon_count)
        return f"{planet.name} has the most moons in this list: {planet.moon_count}."
    if "moon" in question and any(word in question for word in ("fewest", "least")):
        planet = min(PLANETS, key=lambda item: item.moon_count)
        return f"{planet.name} has the fewest moons in this list: {planet.moon_count}."

    if any(word in question for word in ("biggest", "largest", "diameter", "size")):
        planet = max(PLANETS, key=lambda item: item.diameter_km)
        return (
            f"{planet.name} is the biggest planet by diameter, "
            f"at {planet.diameter_km:,} km."
        )

    return (
        "Try asking which planet is biggest, furthest from the Sun, heaviest, "
        "or has the most moons. You can also ask why Pluto isn't on the list."
    )


# Answers questions about the selected planet.
def answer_question(planet, question):
    question = question.lower()

    if "everything" in question or "all about" in question:
        sample_moons = ", ".join(planet.moons) if planet.moons else "None"
        return (
            f"{planet.name}\n"
            f"Mass: {format_mass(planet.mass_earths)}\n"
            f"Average distance from the Sun: {planet.distance_km:,} million km\n"
            f"Diameter: {planet.diameter_km:,} km\n"
            f"Number of moons: {planet.moon_count}\n"
            f"Known sample moons: {sample_moons}"
        )
    if any(word in question for word in ("diameter", "big", "size", "wide")):
        return f"{planet.name} is {planet.diameter_km:,} km in diameter."
    if any(word in question for word in ("distance", "far", "sun")):
        return (
            f"{planet.name} is an average of "
            f"{planet.distance_km:,} million km from the Sun."
        )
    if any(word in question for word in ("mass", "heavy", "weigh")):
        return f"The mass of {planet.name} is {format_mass(planet.mass_earths)}."
    if "moon" in question:
        sample_moons = ", ".join(planet.moons) if planet.moons else "None"
        return (
            f"{planet.name} has {planet.moon_count} moons. "
            f"Some known moons are: {sample_moons}."
        )
    return (
        "I can answer questions about size, distance from the Sun, mass, "
        "or moons. You can also ask “Tell me everything.”"
    )


# Creates the app window and connects its controls.
class PlanetGui:
    # Sets up the window and initial state.
    def __init__(self, root):
        self.root = root
        self.selected_planet = None
        self.root.title("Solar Planets")
        self.root.geometry("520x420")
        self.create_widgets()

    # Creates the labels, planet buttons, and question controls.
    def create_widgets(self):
        banner = tk.Label(
            self.root,
            text="The 8 Planets of the Solar System",
            font=("TkDefaultFont", 20, "bold"),
            bg="#14213D",
            fg="white",
            pady=12,
        )
        banner.pack(fill="x")

        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(pady=10)

        self.selection_label = tk.Label(
            self.root,
            text=(
                "Select a planet to ask about it, or use General question "
                "to compare planets."
            ),
            font=("TkDefaultFont", 12, "bold"),
            justify="left",
            anchor="w",
        )
        self.selection_label.pack(fill="x", padx=20, pady=10)

        for index, planet in enumerate(PLANETS):
            button = tk.Button(
                buttons_frame,
                text=planet.name,
                width=12,
                height=2,
                fg=planet.text_colour,
                # Keep each button connected to its own planet.
                command=lambda selected=planet: self.select_planet(selected),
            )
            button.grid(row=index // 4, column=index % 4, padx=5, pady=6)

        question_label = tk.Label(
            self.root,
            text=(
                "Ask about the selected planet (e.g. 'How big is it?'). "
                "To compare planets, enter your question and click "
                "General question."
            ),
            justify="left",
            wraplength=480,
        )
        question_label.pack(anchor="w", padx=20, pady=(10, 2))

        self.question_entry = tk.Entry(self.root)
        self.question_entry.pack(fill="x", padx=20)

        self.answer_label = tk.Label(
            self.root,
            text="",
            justify="left",
            anchor="w",
            wraplength=480,
        )
        self.answer_label.pack(fill="x", padx=20, pady=10)

        button_frame = tk.Frame(self.root)
        button_frame.pack(anchor="w", padx=20)

        search_button = tk.Button(
            button_frame,
            text="Ask",
            width=12,
            height=2,
            command=self.search_question,
        )
        search_button.pack(side="left", padx=(0, 8))

        general_button = tk.Button(
            button_frame,
            text="General question",
            width=16,
            height=2,
            command=self.search_general_question,
        )
        general_button.pack(side="left", padx=(0, 8))

        reset_button = tk.Button(
            button_frame,
            text="Reset",
            width=12,
            height=2,
            command=self.reset,
        )
        reset_button.pack(side="left")
        self.question_entry.bind("<Return>", self.search_question)

        credit_label = tk.Label(
            self.root,
            text="By Ben Scott",
            font=("TkDefaultFont", 9),
            fg="#555555",
        )
        credit_label.pack(side="bottom", anchor="e", padx=12, pady=6)

    # Sets the selected planet and clears the previous answer.
    def select_planet(self, planet):
        self.selected_planet = planet
        self.selection_label.config(text=f"Selected planet: {planet.name}")
        self.answer_label.config(text="")

    # Clears the selection, question, and answer.
    def reset(self):
        self.selected_planet = None
        self.selection_label.config(
            text=(
                "Select a planet to ask about it, or use General question "
                "to compare planets."
            )
        )
        self.question_entry.delete(0, tk.END)
        self.answer_label.config(text="")

    # Answers a question about the selected planet.
    def search_question(self, event=None):
        if self.selected_planet is None:
            self.answer_label.config(text="Select a planet first.")
            return

        # Use the entry field whether called by Enter or the Ask button.
        input_widget = event.widget if event is not None else self.question_entry
        question = input_widget.get().strip()
        if not question:
            self.answer_label.config(text="Type a question first.")
            return

        self.answer_label.config(
            text=answer_question(self.selected_planet, question)
        )

    # Answers a general question without requiring a selected planet.
    def search_general_question(self):
        question = self.question_entry.get().strip()
        if not question:
            self.answer_label.config(text="Type a question first.")
            return

        self.answer_label.config(text=answer_general_question(question))


# Starts the app when this file is run directly.
if __name__ == "__main__":
    root = tk.Tk()
    PlanetGui(root)
    root.mainloop()
