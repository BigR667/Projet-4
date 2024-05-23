# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# def main():
#     # Demandez à l'utilisateur de saisir un nom d'utilisateur GitHub
#     github_user = input("Input GitHub user: ")

#     # URL du profil GitHub
#     url = f"https://github.com/{github_user}"

#     # Configuration de Selenium pour utiliser Chrome
#     chrome_options = Options()
#     chrome_options.add_argument("--headless")  # Exécute Chrome en mode headless (sans interface graphique)
    
#     # Utilisation de webdriver_manager pour gérer ChromeDriver
#     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

#     try:
#         # Ouvre la page de profil GitHub
#         driver.get(url)

#         # Attendre que la page soit entièrement chargée
#         time.sleep(2)  # Vous pouvez utiliser WebDriverWait pour des solutions plus robustes

#         # Trouver l'élément image de profil par son attribut 'alt'
#         profile_image_element = driver.find_element(By.XPATH, "//img[@alt='Avatar']")
#         profile_image_url = profile_image_element.get_attribute('src')

#         # Afficher l'URL de l'image de profil
#         print(f"The avatar URL for GitHub user '{github_user}' is: {profile_image_url}")

#     except Exception as e:
#         print(f"An error occurred: {e}")

#     finally:
#         # Fermer le navigateur
#         driver.quit()

# if __name__ == "__main__":
#     main()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

def main():
    # Demandez à l'utilisateur de saisir un nom d'utilisateur GitHub
    github_user = input("Input GitHub user: ").strip()
    
    # Si l'utilisateur a entré une URL complète, on extrait le nom d'utilisateur
    if github_user.startswith("https://github.com/"):
        github_user = github_user.split("/")[-1]

    # URL du profil GitHub
    url = f"https://github.com/{github_user}"

    # Configuration de Selenium pour utiliser Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Exécute Chrome en mode headless (sans interface graphique)
    
    # Utilisation de webdriver_manager pour gérer ChromeDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Ouvre la page de profil GitHub
        driver.get(url)

        # Attendre que la page soit entièrement chargée
        time.sleep(2)  # Vous pouvez utiliser WebDriverWait pour des solutions plus robustes

        # Trouver l'élément image de profil
        profile_image_element = driver.find_element(By.CSS_SELECTOR, "img.avatar-user")
        profile_image_url = profile_image_element.get_attribute('src')

        # Afficher l'URL de l'image de profil
        print(f"The avatar URL for GitHub user '{github_user}' is: {profile_image_url}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Fermer le navigateur
        driver.quit()

if __name__ == "__main__":
    main()
