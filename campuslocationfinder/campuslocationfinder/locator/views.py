import gmaps.datasets
from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
import requests
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm


def signup_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(homepage)  # Replace 'home' with the URL name of your home page
    else:
        form = RegistrationForm()
    return render(request, 'locator/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(homepage)  # Replace 'home' with the URL name of your home page
    else:
        form = LoginForm()
    return render(request, 'locator/login.html', {'form': form})


def debug_view(request):
    origin = request.GET.get('origin')
    destination = request.GET.get('destination')

    print(destination)
    # Check if origin and destination are provided.
    if not origin or not destination:
        return JsonResponse({"error": "Origin and destination are required."}, status=400)

    # Process the directions request using the retrieved origin and destination.
    # ...
    # Return the origin and destination as JSON for debugging.
    return JsonResponse({"origin": origin, "destination": destination})


def actual_view(request):
    # Fetch the JSON data from the debug view.
    debug_view_response = debug_view(request)

    # Check if the debug view returned an error.
    if debug_view_response.status_code == 400:
        return debug_view_response  # Return the error response.

    # Parse the JSON data from the response.
    data = json.loads(debug_view_response.content)

    # Extract origin and destination from the parsed data.
    origin = data.get("origin")
    destination = data.get("destination")
    print(origin)
    print(destination)
    # Now you can use the origin and destination for further processing.
    # For example, you can make a directions API request or perform any necessary calculations.

    # ...

    # Return a response with the processed data.
    return JsonResponse({"message": "Directions processed successfully"})


def fetch_directions_from_api(origin, destination):
    # Implement code to fetch directions from the Google Maps API or your preferred provider.
    # Ensure you include your API key.
    # This is a simplified example; replace it with your implementation.
    api_url = 'https://maps.googleapis.com/maps/api/directions/json'
    api_key = 'AIzaSyDcN0JzbGjzIm8HAKFdiQnz5f3vd5AfP-s'

    params = {
        'origin': origin,
        'destination': destination,
        'key': api_key,
    }

    response = requests.get(api_url, params=params)
    data = response.json()

    return data


def index(request):
    if request.method == 'GET':
        # Fetch the JSON data from the debug view.
        debug_view_response = debug_view(request)

        # Check if the debug view returned an error.
        if debug_view_response.status_code == 400:
            return debug_view_response  # Return the error response.

        # Parse the JSON data from the response.
        data = json.loads(debug_view_response.content)

        # Extract origin and destination from the parsed data.
        origin = data.get("origin")
        destination = data.get("destination")

        print(origin)
        print(destination)
        if origin and destination:
            directions_data = fetch_directions_from_api(origin, destination)
            response_data = f"updateMapWithDirections({json.dumps(directions_data)});"
            return JsonResponse(data)
        else:
            return JsonResponse({'error': 'Origin and destination are required.'}, status=400)

    return JsonResponse({'error': 'Invalid request method.'}, status=405)


def debug_view(request):
    return JsonResponse(request.GET)

def homepage(request):
    return render(request, 'locator/index.html')