import tkinter as tk


# Stores the facts and button text colour used for one planet.
class Planet:
    def __init__(self,name,mass_kg,distance_km,diameter_km,moon_count,moons,text_colour,):
        self.name = name
        self.mass_kg = mass_kg
        self.distance_km = distance_km
        self.diameter_km = diameter_km
        self.moon_count = moon_count
        self.moons = moons
        self.text_colour = text_colour


PLANETS = [
    # Planet distances are in millions of kilometres; figures are from NASA.
    Planet("Mercury", "3.3011×10^23kg", 58, 4_879, 0, (), "#555555"),
    Planet("Venus", "4.8675 × 10^24kg", 108, 12_104, 0, (), "#9C5700"),
    Planet("Earth", "5.9722x10^24kg", 150, 12_756, 1, ("Moon",), "#176B2C"),
    Planet("Mars", "6.4171x10^23kg", 228, 6_779, 2, ("Phobus", "Deimos"), "#B22222"),
    Planet("Jupiter", "1.8982×10^27kg", 778, 139_820, 95, ("Io", "Europa", "Ganymede", "Callisto"), "#8B4513"),
    Planet("Saturn", "5.6834×10^26kg", 1434, 116_460, 146, ("Titan", "Enceladus", "Rhea", "Iapetus"), "#806000"),
    Planet("Uranus", "8.6810×10^25kg", 2871, 50_724, 28, ("Titania", "Oberon", "Umbriel", "Ariel", "Miranda"), "#007C91"),
    Planet("Neptune", "1.02413×10^26kg", 4495, 49_244, 16, ("Triton", "Nereid", "Proteus", "Larissa"), "#2446A6"),
]


def answer_question(planet, question):
    # Match common keywords in the question to the planet fact being requested.
    question = question.lower()

    if "everything" in question or "all about" in question:
        sample_moons = ", ".join(planet.moons) if planet.moons else "None"
        return (
            f"{planet.name}\n"
            f"Mass: {planet.mass_kg}\n"
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
        return f"The mass of {planet.name} is {planet.mass_kg}."
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


# Builds the window and handles planet selection, questions, and reset.
class PlanetGui:
    def __init__(self, root):
        self.root = root
        self.selected_planet = None
        self.root.title("Solar Planets")
        self.root.geometry("520x420")
        self.create_widgets()

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
            text="Select a planet, then ask a question about it.",
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
                # Capture this planet so each button selects its own planet.
                command=lambda selected=planet: self.select_planet(selected),
            )
            button.grid(row=index // 4, column=index % 4, padx=5, pady=6)

        question_label = tk.Label(
            self.root,
            text="Ask a question about the selected planet:",
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

    def select_planet(self, planet):
        self.selected_planet = planet
        self.selection_label.config(text=f"Selected planet: {planet.name}")
        self.answer_label.config(text="")

    def reset(self):
        # Restore the prompt and clear the current selection and conversation.
        self.selected_planet = None
        self.selection_label.config(
            text="Select a planet, then ask a question about it."
        )
        self.question_entry.delete(0, tk.END)
        self.answer_label.config(text="")

    def search_question(self, event=None):
        if self.selected_planet is None:
            self.answer_label.config(text="Select a planet first.")
            return

        # Enter passes an event; the Ask button calls this without one.
        input_widget = event.widget if event is not None else self.question_entry
        question = input_widget.get().strip()
        if not question:
            self.answer_label.config(text="Type a question first.")
            return

        self.answer_label.config(
            text=answer_question(self.selected_planet, question)
        )


if __name__ == "__main__":
    root = tk.Tk()
    PlanetGui(root)
    root.mainloop()
