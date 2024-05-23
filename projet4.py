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


# import requests
# from bs4 import BeautifulSoup as bs 

# github_user = input("input github user: ")
# url = "https://github.com/" +github_user 
# r = requests.get(url)
# soup = bs(r.content, 'html.parser')
# profile_image = soup.find("img", {'alt': 'Avatar'})['src']

# print(profile_image)

# import os
# def main():
#     i=0
#     path = "C:/Users/akeit/OneDrive/Documents/PROJET CALCULATOR/IMAGE"
#     for filesname in os.listdir(path):
#         my_dest = "image" + str(i) + ".jpg"
#         my_source= path + filesname
#         my_dest = path + my_dest
#         os.rename(my_source, my_dest)
#         i += 1

# if __name__ == '__main__':
#     main()   












# import os

# def main():
#     i = 0
#     path = "C:/Users/akeit/OneDrive/Documents/PROJET CALCULATOR/IMAGE/"

#     # Vérifiez que le chemin existe
#     if not os.path.exists(path):
#         print(f"Le chemin '{path}' n'existe pas.")
#         return

#     # Parcourez tous les fichiers dans le répertoire
#     for filename in os.listdir(path):
#         if os.path.isfile(os.path.join(path, filename)):
#             # Construisez les chemins source et destination
#             my_source = os.path.join(path, filename)
#             my_dest = os.path.join(path, f"img{i}.jpg")
            
#             # Renommez le fichier
#             os.rename(my_source, my_dest)
#             print(f"Renommage de {my_source} à {my_dest}")
            
#             i += 1

# if __name__ == '__main__':
#     main()

