import requests


def get_nearby_places(api_key, latitude, longitude, radius=1000, place_type=""):
    """
    Fetches nearby places using the Google Places API.

    :param api_key: Your Google Places API key.
    :param latitude: Latitude of the center point.
    :param longitude: Longitude of the center point.
    :param radius: Radius (in meters) around the center point to search for places.
    :param place_type: Optional filter for a specific type of place (e.g., "restaurant").
    :return: A list of nearby places as dictionaries with name, address, latitude, and longitude.
    """
    # Define the API endpoint URL
    base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?"

    # Create parameters for the API request
    params = {
        "location": f"{latitude},{longitude}",
        "radius": radius,
        "key": api_key,
    }

    if place_type:
        params["type"] = place_type

    try:
        # Send a GET request to the Google Places API
        response = requests.get(base_url, params=params)
        data = response.json()

        # Extract and format the results
        places = []
        for result in data.get("results", []):
            place = {
                "name": result.get("name"),
                "address": result.get("vicinity"),
                "latitude": result["geometry"]["location"]["lat"],
                "longitude": result["geometry"]["location"]["lng"],
            }
            places.append(place)
            print(places)
        return places
    except Exception as e:
        print(f"Error: {str(e)}")
        return []


# Example usage:
if __name__ == "__main__":
    # Replace 'YOUR_API_KEY' with your actual Google Places API key
    api_key = "AIzaSyARmKpW6QqvLco6sFwFz8ufnaA_FgHplzw"
    latitude = 8.98921  # Example latitude (San Francisco, CA)
    longitude = -7.18141  # Example longitude (San Francisco, CA)

    # Get nearby places (e.g., restaurants) within a 1000-meter radius
    nearby_places = get_nearby_places(api_key, latitude, longitude, radius=1000, place_type="restaurant")

    # Print the nearby places
    for place in nearby_places:
        print(f"Name: {place['name']}")
        print(f"Address: {place['address']}")
        print(f"Latitude: {place['latitude']}")
        print(f"Longitude: {place['longitude']}")
        print()
