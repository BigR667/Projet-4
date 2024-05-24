from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurer le WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Demander à l'utilisateur d'entrer le lien du profil GitHub
github_profile_url = input("Veuillez entrer le lien du profil GitHub: ")

# Naviguer vers le profil GitHub
driver.get(github_profile_url)

# Attendre que la page se charge et que l'image de profil soit présente
try:
    profile_image = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "img.avatar-user"))
    )
    image_url = profile_image.get_attribute('src')
    print(f"L'URL de l'image de profil est: {image_url}")

    # Afficher l'image de profil dans le navigateur
    driver.get(image_url)

    # Attendre quelques secondes pour afficher l'image
    time.sleep(5)

finally:
    # Fermer le navigateur
    driver.quit()
