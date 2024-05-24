import requests

# Demande à l'utilisateur de saisir un nom d'utilisateur GitHub
github_user = input("Input GitHub user: ")

# URL de l'API GitHub pour obtenir les informations de l'utilisateur
url = f"https://api.github.com/users/{github_user}"

# Effectue une requête GET à l'API GitHub
response = requests.get(url)

if response.status_code == 200:
    # Parse la réponse JSON
    data = response.json()

    # Récupère l'URL de l'avatar
    avatar_url = data['avatar_url']

    # Affiche l'URL de l'avatar
    print(f"The avatar URL for GitHub user '{github_user}' is: {avatar_url}")
else:
    print(f"Could not find the avatar for GitHub user '{github_user}'.")