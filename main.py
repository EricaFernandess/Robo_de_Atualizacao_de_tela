import time
import pyautogui
from playwright.sync_api import sync_playwright

# Defina as URLs que você deseja abrir
urls = ['https://www.example1.com', 'https://www.example2.com', 'https://www.example3.com']

# Inicialize o contexto do Playwright
with sync_playwright() as playwright:
    # Inicialize o navegador em modo "headed"
    browser = playwright.chromium.launch(headless=False)

    # Crie uma nova página
    page = browser.new_page()

    # Definindo a resolução da tela: 4K {"width": 3840, "height": 2160} ou FullHD {"width": 1920, "height": 1080}
    page.set_viewport_size({"width": 1920, "height": 1080})

    # Aguarde por 5 segundos
    time.sleep(5)

    # Simula o pressionamento da tecla F11
    pyautogui.hotkey('F11')

    # Loop infinito para a navegação contínua
    while True:
        # Percorra as URLs
        for url in urls:
            # Abra a URL na página
            page.goto(url)

            # Aguarde por 1 minuto
            time.sleep(60)

    # Feche o navegador
    browser.close()
