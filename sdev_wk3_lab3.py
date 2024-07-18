"""Python program that displays information about the 50 U.S. states"""
try:
    import matplotlib.pyplot as plt
    import matplotlib.image as mpimg
except ImportError as e:
    print(f"Unable to import {e.name}")

states_data = [  # Data for each state is stored in a dictionary
    # Dictionary for Alabama
    {"name": "Alabama",
     "capital": "Montgomery",
     "population": 196010,
     "flower": "Camellia",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/camellia-flower.webp"
     },
    # Dictionary for Alaska
    {"name": "Alaska",
     "capital": "Juneau",
     "population": 31534,
     "flower": "Forget-me-not",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/Alpineforgetmenot.webp"
     },
    # Dictionary for Arizona
    {"name": "Arizona",
     "capital": "Phoenix",
     "population": 1651344,
     "flower": "Saguaro cactus blossom",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/saguaroflowersFlickr.webp"
     },
    # Dictionary for Arkansas
    {"name": "Arkansas",
     "capital": "Little Rock",
     "population": 201029,
     "flower": "Apple blossom",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/AppletreeblossomArkansasflower.webp"
     },
    # Dictionary for California
    {"name": "California",
     "capital": "Sacramento",
     "population": 528306,
     "flower": "California poppy",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/CAflowerCaliforniaPoppy.webp"
     },
    # Dictionary for Colorado
    {"name": "Colorado",
     "capital": "Denver",
     "population": 699288,
     "flower": "Rocky Mountain columbine",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/Colorado_columbine2.webp"
     },
    # Dictionary for Connecticut
    {"name": "Connecticut",
     "capital": "Hartford",
     "population": 119817,
     "flower": "Mountain laurel",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/Mountain-Laural-flowers2.webp"
     },
    # Dictionary for Delaware
    {"name": "Delaware",
     "capital": "Dover",
     "population": 37892,
     "flower": "Peach blossom",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/peachblossomspeachflowers.webp"
     },
    # Dictionary for Florida
    {"name": "Florida",
     "capital": "Tallahassee",
     "population": 198631,
     "flower": "Orange blossom",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/OrangeBlossomsFloridaFlower.webp"
     },
    # Dictionary for Georgia
    {"name": "Georgia",
     "capital": "Atlanta",
     "population": 490270,
     "flower": "Cherokee rose",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/CherokeeRoseFlower.webp"
     },
    # Dictionary for Hawaii
    {"name": "Hawaii",
     "capital": "Honolulu",
     "population": 337088,
     "flower": "Hibiscus",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/yellowhibiscusPuaAloalo.webp"
     },
    # Dictionary for Idaho
    {"name": "Idaho",
     "capital": "Boise",
     "population": 240713,
     "flower": "Syringa, mock orange",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/syringaPhiladelphuslewisiiflower.webp"
     },
    # Dictionary for Illinois
    {"name": "Illinois",
     "capital": "Springfield",
     "population": 111711,
     "flower": "Violet",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/singlebluevioletflower.webp"
     },
    # Dictionary for Indiana
    {"name": "Indiana",
     "capital": "Indianapolis",
     "population": 871449,
     "flower": "Peony",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/PeonyPaeoniaflowers.webp"
     },
    # Dictionary for Iowa
    {"name": "Iowa",
     "capital": "Des Moines",
     "population": 208734,
     "flower": "Wild prairie rose",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/WildPrairieRose.webp"
     },
    # Dictionary for Kansas
    {"name": "Kansas",
     "capital": "Topeka",
     "population": 125353,
     "flower": "Sunflower",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/native-sunflowers.webp"
     },
    # Dictionary for Kentucky
    {"name": "Kentucky",
     "capital": "Frankfort",
     "population": 28523,
     "flower": "Goldenrod",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/stateflowergoldenrod-bloom.webp"
     },
    # Dictionary for Louisiana
    {"name": "Louisiana",
     "capital": "Baton Rouge",
     "population": 217665,
     "flower": "Magnolia",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/MagnoliagrandifloraMagnoliaflower.webp"
     },
    # Dictionary for Maine
    {"name": "Maine",
     "capital": "Augusta",
     "population": 19058,
     "flower": "White pine cone and tassel",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/whitepinemalecones.webp"
     },
    # Dictionary for Maryland
    {"name": "Maryland",
     "capital": "Annapolis",
     "population": 40397,
     "flower": "Black-eyed susan",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/FlowerMDBlack-eyedSusan.webp"
     },
    # Dictionary for Massachusetts
    {"name": "Massachusetts",
     "capital": "Boston",
     "population": 617459,
     "flower": "Mayflower",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/MayflowerTrailingArbutus.webp"
     },
    # Dictionary for Michigan
    {"name": "Michigan",
     "capital": "Lansing",
     "population": 112460,
     "flower": "Apple blossom",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/appleblossombeauty.webp"
     },
    # Dictionary for Minnesota
    {"name": "Minnesota",
     "capital": "Saint Paul",
     "population": 299830,
     "flower": "Pink and white lady's slipper",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/pinkwhiteladysslipperflower1.webp"
     },
    # Dictionary for Mississippi
    {"name": "Mississippi",
     "capital": "Jackson",
     "population": 143776,
     "flower": "Magnolia",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/magnoliablossomflower01.webp"
     },
    # Dictionary for Missouri
    {"name": "Missouri",
     "capital": "Jefferson City",
     "population": 42535,
     "flower": "Hawthorn",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/hawthornflowersblossoms1.webp"
     },
    # Dictionary for Montana
    {"name": "Montana",
     "capital": "Helena",
     "population": 34690,
     "flower": "Bitterroot",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/bitterrootfloweremblem.webp"
     },
    # Dictionary for Nebraska
    {"name": "Nebraska",
     "capital": "Lincoln",
     "population": 295222,
     "flower": "Goldenrod",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/goldenrodflowersyellow4.webp"
     },
    # Dictionary for Nevada
    {"name": "Nevada",
     "capital": "Carson City",
     "population": 59630,
     "flower": "Sagebrush",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/Nevada-Sagebrush-Artemisia-tridentata.webp"
     },
    # Dictionary for New Hampshire
    {"name": "New Hampshire",
     "capital": "Concord",
     "population": 44606,
     "flower": "Purple lilac",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/lilacflowerspurplelilac.webp"
     },
    # Dictionary for New Jersey
    {"name": "New Jersey",
     "capital": "Trenton",
     "population": 90048,
     "flower": "Violet",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/wood-violet.webp"
     },
    # Dictionary for New Mexico
    {"name": "New Mexico",
     "capital": "Santa Fe",
     "population": 89220,
     "flower": "Yucca flower",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/YuccaFlowersclose.webp"
     },
    # Dictionary for New York
    {"name": "New York",
     "capital": "Albany",
     "population": 97593,
     "flower": "Rose",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/redrosebeautystateflowerNY.webp"
     },
    # Dictionary for North Carolina
    {"name": "North Carolina",
     "capital": "Raleigh",
     "population": 472540,
     "flower": "Flowering dogwood",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/floweringdogwoodflowers2.webp"
     },
    # Dictionary for North Dakota
    {"name": "North Dakota",
     "capital": "Bismarck",
     "population": 75073,
     "flower": "Wild prairie rose",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/flowerwildprairierose.webp"
     },
    # Dictionary for Ohio
    {"name": "Ohio",
     "capital": "Columbus",
     "population": 907865,
     "flower": "Scarlet carnation",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/redcarnationOhioflower.webp"
     },
    # Dictionary for Oklahoma
    {"name": "Oklahoma",
     "capital": "Oklahoma City",
     "population": 697763,
     "flower": "Mistletoe",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/mistletoe_phoradendron_serotinum.webp"
     },
    # Dictionary for Oregon
    {"name": "Oregon",
     "capital": "Salem",
     "population": 181620,
     "flower": "Oregon grape",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/Oregongrapeflowers2.webp"
     },
    # Dictionary for Pennsylvania
    {"name": "Pennsylvania",
     "capital": "Harrisburg",
     "population": 50267,
     "flower": "Mountain laurel",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/Mt_Laurel_Kalmia_Latifolia.webp"
     },
    # Dictionary for Rhode Island
    {"name": "Rhode Island",
     "capital": "Providence",
     "population": 188877,
     "flower": "Violet",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/violetsflowers.webp"
     },
    # Dictionary for South Carolina
    {"name": "South Carolina",
     "capital": "Columbia",
     "population": 137996,
     "flower": "Yellow jessamine",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/CarolinaYellowJessamine101.webp"
     },
    # Dictionary for South Dakota
    {"name": "South Dakota",
     "capital": "Pierre",
     "population": 13954,
     "flower": "Pasque flower",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/Pasqueflower-03.webp"
     },
    # Dictionary for Tennessee
    {"name": "Tennessee",
     "capital": "Nashville",
     "population": 658525,
     "flower": "Iris",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/purpleirisflower.webp"
     },
    # Dictionary for Texas
    {"name": "Texas",
     "capital": "Austin",
     "population": 966292,
     "flower": "Bluebonnet",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/BluebonnetsBlueRed.webp"
     },
    # Dictionary for Utah
    {"name": "Utah",
     "capital": "Salt Lake City",
     "population": 202272,
     "flower": "Sego lily",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/SegoLily.webp"
     },
    # Dictionary for Vermont
    {"name": "Vermont",
     "capital": "Montpelier",
     "population": 7988,
     "flower": "Red clover",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/redcloverstateflowerWV.webp"
     },
    # Dictionary for Virginia
    {"name": "Virginia",
     "capital": "Richmond",
     "population": 226472,
     "flower": "American dogwood",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/floweringdogwoodflowers2.webp"
     },
    # Dictionary for Washington
    {"name": "Washington",
     "capital": "Olympia",
     "population": 56510,
     "flower": "Coast rhododendron",
     "flower_img": "path_to_image47.jpg"
     },
    # Dictionary for West Virginia
    {"name": "West Virginia",
     "capital": "Charleston",
     "population": 46692,
     "flower": "Rhododendron",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/flower_rhododendronWeb.webp"
     },
    # Dictionary for Wisconsin
    {"name": "Wisconsin",
     "capital": "Madison",
     "population": 269897,
     "flower": "Wood violet",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/wood-violet.webp"
     },
    # Dictionary for Wyoming
    {"name": "Wyoming",
     "capital": "Cheyenne",
     "population": 64831,
     "flower": "Indian paintbrush",
     "flower_img": "SDEV-Wk3-Lab3/State Flowers/indianpaintbrushWYflower.webp"
     }
]


def display_states():
    """Displays the states in alphabetical order as a table."""

    # Sort the data by state name
    states_data.sort(key=lambda x: x["name"])

    # Determine the maximum width of state names for formatting
    name_width = max(len(state["name"]) for state in states_data) + 2
    capital_width = max(len(state["capital"]) for state in states_data) + 2

    # Create a header for the table
    header = (
        f"\n{'State'.ljust(name_width)} | "
        f"{'Capital'.ljust(capital_width)} | "
        "Population | Flower"
    )
    print(header)
    print('-' * len(header))  # Print a divider

    # Print each state's information in table rows
    for state in states_data:
        print(
            f"{state['name'].ljust(name_width)} | "
            f"{state['capital'].ljust(capital_width)} | "
            f"{state['population']:>10} | "  # Right align population numbers
            f"{state['flower']}"
        )


def search_state():
    """Searches for a state by name and displays the state's information."""
    state_found = False
    while state_found is False:  # Loop until user enters a state name
        state_name = input("Enter state name: ").strip()
        for state in states_data:
            if state_name.lower() == state['name'].lower():  # Case insensitive
                state_found = True
                print(f"Capital: {state['capital']}, Population: {
                      state['population']}, Flower: {state['flower']}")
                # Display state information
                # Display state flower image
                img = mpimg.imread(state["flower_img"])
                plt.imshow(img)
                plt.show()
                return
        # Display error message if state not found
        print("\nState not found!\n")


def display_population_graph():
    """Displays a bar graph of the top 5 populated states."""
    # Sort states by population in descending order and get the top 5
    sorted_states = sorted(
        states_data, key=lambda x: x["population"], reverse=True)[:5]
    names = [state["name"] for state in sorted_states]
    populations = [state["population"] for state in sorted_states]

    # Display bar graph
    plt.bar(names, populations)
    plt.xlabel('States')
    plt.ylabel('Population')
    plt.title('Top 5 Populated States')
    plt.show()


def update_population():
    """Updates the population of a state."""
    state_found = False
    while state_found is False:  # Loop until user enters a state name
        state_name = input("\nEnter state name: ").strip()
        for state in states_data:
            if state_name.lower() == state['name'].lower():  # Case insensitive
                state_found = True
                # Data validation for population number
                while True:
                    try:
                        new_population = int(
                            input(f"Enter new population for {state_name}: "))
                        break
                    except ValueError:
                        print("Invalid input! Please enter an integer value.")
                state["population"] = new_population
                print(f"Population updated for {state_name}!")
                return
        print("\nState not found!")  # Display error message if state not found


def main():
    """Main function that displays the menu and calls the appropriate functions."""
    while True:
        print("\nWelcome to the U.S. State Information Application!\n")
        print("1. Display all states")
        print("2. Search for a specific state")
        print("3. Display a bar graph of top 5 populated states")
        print("4. Update state population")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            display_states()
        elif choice == "2":
            search_state()
        elif choice == "3":
            display_population_graph()
        elif choice == "4":
            update_population()
        elif choice == "5":
            print(
                "Exiting... Thank you for using the U.S State Information Application! Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")


main()
