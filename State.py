# Dictionary to store state information using a hash table
states_info = {
    "Michigan": {
        "Capital": "Lansing",
        "Area": "96,716 sq mi",
        "Population": "10.03 million",
    },
    "Indiana": {
        "Capital": "Indianapolis",
        "Area": "236,420 sq mi",
        "Population": "6.833 million",
    },
    "Florida": {
        "Capital": "Tallahassee",
        "Area": "65,758 sq mi",
        "Population": "21.48 million",
    },
    "New York": {
        "Capital": "Albany",
        "Area": "54,555 sq mi",
        "Population": "19.45 million",
    }
}

# get and display state info
def get_state_info(state_name):
    # get state information using dictionary
    state_info = states_info.get(state_name)
    if state_info:
        print(f"Information for {state_name}:")
        for key, value in state_info.items():
            print(f"{key}: {value}")
    else:
        print(f"No information found for {state_name}.")

# main 
if __name__ == "__main__":
    user_input = input("Enter the name of a state: ")
    get_state_info(user_input)
