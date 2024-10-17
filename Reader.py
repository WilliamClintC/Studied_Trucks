import pickle
from config import pkl_name, pattern,detect_encoding

def get_unique_zoning_locations(file_path):
    # Step 1: Load the dataset from the .pkl file
    with open(file_path, 'rb') as file:
        dummy_data = pickle.load(file)

    # Step 2: Extract the "Zoning Location" values
    zoning_locations = [entry["Zoning Location"] for entry in dummy_data]

    # Step 3: Find unique entries using a set
    unique_zoning_locations = set(zoning_locations)

    return unique_zoning_locations

# Example usage
print("Unique Zoning Locations:", get_unique_zoning_locations(pkl_name))

with open(pkl_name, 'rb') as file:
    data = pickle.load(file)

# Filter the data
filtered_data = [item for item in data if item.get("Zoning Location") == "AL_Athens"]

# Print or process the filtered data
for item in filtered_data:
    print(item)