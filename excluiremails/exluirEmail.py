from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Defina o caminho correto do chromedriver
chromedriver_path = 'K:\downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe'  # Certifique-se de que o caminho está correto

# Inicializar o WebDriver com o Service
service = Service(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

# Função para fazer login
def login_to_email(driver, username, password):
    driver.get('https://mail.hostinger.com/')  # Substitua pela URL correta da página de login
    time.sleep(5)  # Aguarda o carregamento da página

    # Localizar os campos de usuário e senha e preenchê-los
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "rcmloginuser"))
    )
    username_input.send_keys(username)

    password_input = driver.find_element(By.ID, "rcmloginpwd")
    password_input.send_keys(password)

    # Submeter o formulário de login
    login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()

    # Esperar que a página de e-mails carregue após o login
    time.sleep(5)

# Função para acessar a página de e-mails (após o login)
def open_email_page(driver):
    driver.get('https://mail.hostinger.com/?_task=mail&_mbox=INBOX&_page=1000')  # Substitua pela URL correta da página de e-mails
    time.sleep(5)  # Espera o carregamento da página

# Função para selecionar todos os e-mails da página atual
def select_all_emails(driver):
    # Aguardar até que o botão "Selecionar" esteja clicável
    select_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.select.active"))
    )
    select_button.click()
    time.sleep(2)  # Espera o menu de seleção abrir

    # Aguardar até que o botão "Página atual" esteja clicável
    select_page_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.select.page.active"))
    )
    select_page_button.click()
    time.sleep(2)  # Espera os e-mails serem selecionados

# Função para deletar e-mails com a tecla Delete
def delete_selected_emails(driver):
    # Pressionar a tecla Delete no teclado
    body = driver.find_element(By.TAG_NAME, "body")  # Seleciona o corpo da página para enviar o comando
    body.send_keys(Keys.DELETE)  # Envia o comando Delete
    time.sleep(3)  # Espera a exclusão ser processada

# Função para ir para a página anterior
def go_to_previous_page(driver):
    try:
        # Clicar no botão "Página Anterior"
        prev_page_button = driver.find_element(By.CSS_SELECTOR, "a.prevpage")
        prev_page_button.click()
        time.sleep(5)  # Aguarda o carregamento da página anterior
    except Exception as e:
        print("Não foi possível voltar para a página anterior:", e)
        return False  # Indica que não conseguiu voltar para a página anterior
    return True  # Indica que conseguiu voltar para a página anterior

# Função principal para repetir o processo de exclusão por 950 vezes
def delete_emails_in_multiple_pages(driver, repetitions):
    open_email_page(driver)  # Abre a página de e-mails
    for i in range(repetitions):
        print(f"Processando a página {i + 1} de {repetitions}")
        select_all_emails(driver)  # Seleciona todos os e-mails da página atual
        delete_selected_emails(driver)  # Deleta os e-mails selecionados
        time.sleep(2)  # Pausa para garantir que o processo esteja completo

        # Verifica se consegue ir para a página anterior
        if not go_to_previous_page(driver):
            print("Não há mais páginas anteriores. Encerrando o processo.")
            break  # Sai do loop se não houver mais páginas anteriores

# Executar o processo de login e exclusão de e-mails
username = "email"  # Substitua pelo seu e-mail
password = "senha"  # Substitua pela sua senha

login_to_email(driver, username, password)  # Faz login no site
delete_emails_in_multiple_pages(driver, 950)  # Executa a exclusão dos e-mails

# Fechar o driver ao final
driver.quit()
