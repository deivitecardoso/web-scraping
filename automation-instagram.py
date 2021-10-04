# BIBLIOTECAS NECESSÁRIAS!!
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
import os
import wget
from termcolor import colored
import http.client as http_client
import logging
import contextlib

print(colored("\n### ABRINDO O BROWSER ###", 'red'))
navegador = webdriver.Chrome(
    executable_path="/path/chromedriver")#caminho do drive

# !!!!LOG
http_client.HTTPConnection.debuglevel = 0
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

navegador.get("http://instagram.com")
# print()

username = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='password']")))
# print()

username.send_keys("seu-usuario")
password.send_keys('sua-senha')
# print()

submit = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
# print()

submit.click()
# print()

not_now = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')))
# print()

not_now.click()
# print()

not_now2 = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')))
# print()

not_now2.click()
# print()

searchbox = WebDriverWait(navegador, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Pesquisar']")))
# print()

keyword = '#palavradeseada'

# DIGITANDO A HASHTAG...
searchbox.send_keys(keyword)

# ENVIANDO OS DADOS DIGITADOS...
element = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable(
    (By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div')))
element.click()
sleep(3)

# ADICIONANDO SCROOL, PARA PEGAR MAIS INFORMAÇÕES NA APLICAÇÃO
navegador.execute_script("window.scrollTo(0, document.body.scrollHeight);")

##########
images = navegador.find_elements_by_tag_name('img')

# CAPTURANDO IMAGENS
images = [image.get_attribute('src') for image in images]

path = os.getcwd()
path = os.path.join(path, keyword[1:])

# CRIANDO DIRETÓRIO
os.mkdir(path)

print(path)

counter = 0
# FOR + WGET PARA PEGAR AS IMAGENS E SALVAR NO DIREÓRIO CRIADO, IGNORANDO O PRIMEIRO ARGUMENTO [1:], DESCARTANDO "#"
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + '.jpg')
    wget.download(image, save_as)
    counter += 1

print(images)