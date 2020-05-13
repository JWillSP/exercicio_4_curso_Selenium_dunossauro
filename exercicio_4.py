import re
import time
from selenium import webdriver
from funcs_uteis import decode_url, preencher_form

dict_from_url = {}

path = r"C:\Users\Public\Downloads\geckodriver.exe"

nav = webdriver.Firefox(executable_path=path)

nav.get('https://selenium.dunossauro.live/exercicio_04.html')

time.sleep(2)

preencher_form(
    nav,
    nome='anon',
    email='anon@mail.edu',
    senha='123232',
    telefone='(77)987654321')

nav.find_element_by_name('btn').click()

time.sleep(2)

text_url = re.search(r'.+\?(.+)', nav.current_url).groups(1)[0]

lista_desejada = decode_url(text_url).split("&")[:-1]

for par in lista_desejada:
    npar = par.split('=')
    dict_from_url.update({npar[0]: npar[1]})

dict_from_result = eval(nav.find_element_by_tag_name('textarea').text)

assert dict_from_url == dict_from_result
