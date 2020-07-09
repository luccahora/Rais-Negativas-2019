#Desenvolvido por Lucca Felipe Hora

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time
import csv
import os
import urllib.request
import requests
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import selenium.webdriver.common.alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
global str
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_experimental_option("prefs", {
"download.default_directory": r"C:\Users\SEUCAMINHO\Desktop\Rais\Saida", #Definindo um diretorio padrão para fazer o download do pdf
"download.prompt_for_download": False,
"download.directory_upgrade": True,
"safebrowsing.enabled": True,
"pdfjs.disabled": True,
"plugins.plugins_list": [{"enabled":False,"name":"Chrome PDF Viewer"}],
"plugins.always_open_pdf_externally": True,
})
# options.add_argument("--headless")
options.add_argument("--window-size=1920x1080")
driver = webdriver.Chrome(chrome_options=options)

driver.maximize_window()

# esta funcao abre a pagina de login e receberá login e senha do csv para logar
def func_first_page(cnpj, razao, cnae, natureza_juridica, optante_simples, logradouro, cep, cidade):

    try:  # try /except para o caso de não carregar a tempo os elmentos abaixo, caso não ache, o expect cuidará de chamar a funçao novamente
        # entrando no site
        driver.get("http://www.rais.gov.br/sitio/negativa.jsf")

        time.sleep(2)
        print("  ")
        print("  ")
        print("Enviando RAIS da empresa:  ", razao)
        print("______")
        declaracao_retificadora = driver.find_element_by_xpath('//*[@id="form:indRetificacaoEmpresa:1"]').click()
        exerceu_atividade = driver.find_element_by_xpath('//*[@id="form:indAtividadeanoBase:0"]').click()
        
        field_cnpj = driver.find_element_by_xpath('//*[@id="form:cnpj"]')  # encontrando o campo do Cnpj
        field_cnpj.click()
        time.sleep(0.5)
        field_cnpj = field_cnpj.send_keys(cnpj)  #Inserindo o Cnpj
        
        field_razao = driver.find_element_by_xpath('//*[@id="form:razaosocial"]')
        field_razao = field_razao.send_keys(razao)
       
        field_cnae = driver.find_element_by_xpath('//*[@id="form:selcnae"]')
        field_cnae = field_cnae.send_keys(cnae)

        field_natureza_juridica = driver.find_element_by_xpath('//*[@id="form:selcnatjur"]')
        field_natureza_juridica = field_natureza_juridica.send_keys(natureza_juridica)

        porte_empresa = "micro" #Tamanho da empresa. obs: utilizar os tamanhos que aparecem como opção no site da Rais
        driver.find_element_by_xpath('//*[@id="form:porteEmpresa"]').send_keys(porte_empresa)

        if optante_simples == "sim":
            driver.find_element_by_xpath('//*[@id="form:indOptanteSimples"]').send_keys(optante_simples)
        elif optante_simples == "não":
            driver.find_element_by_xpath('//*[@id="form:indOptanteSimples"]').send_keys(optante_simples)
       

        time.sleep(5)
        aba_endereco = driver.find_element_by_xpath('//*[@id="navegacao"]/li[2]/a').click()

        #button_one = driver.find_element_by_xpath('//*[@id="tab1"]/div[9]/a').click()
       
        field_logradouro = driver.find_element_by_xpath('//*[@id="form:logradouro"]')
        field_logradouro = field_logradouro.send_keys(logradouro)

        field_cep = driver.find_element_by_xpath('//*[@id="form:cep"]')
        field_cep.click()
        time.sleep(0.5)
        field_cep = field_cep.send_keys(cep)

        #O estado está por padrão empresas da BAHIA, mas você pode alterar parar empresas do estado que deseja. Alterando na linha 97.
        form_estado = driver.find_element_by_xpath('//*[@id="form:estado"]').click()    
        estados = Select(driver.find_element_by_name('form:estado'))
        estados.select_by_visible_text('BA')
        
        time.sleep(10)
        form_municipio = driver.find_element_by_xpath('//*[@id="form:cidade"]').click()
        municipio = Select(driver.find_element_by_name('form:cidade'))
        municipio.select_by_visible_text(cidade)

        conteudo_complemento = "  " 
        driver.find_element_by_xpath('//*[@id="form:complemento"]').send_keys(conteudo_complemento)

        #________________________________________
        #Passando o telefone para contato padrão. 
        
        DDD = "71" 
        driver.find_element_by_xpath('//*[@id="form:ddd"]').send_keys(DDD)  

        Numero = "40028922"
        driver.find_element_by_xpath('//*[@id="form:telefone"]').send_keys(Numero)

        Email = "joaozinho@seuemail.com.br"
        driver.find_element_by_xpath('//*[@id="form:email"]').send_keys(Email)
        
        #PASSA PARA A PROXIMA PAGINA
        pagina_sindicais = driver.find_element_by_xpath('//*[@id="tab2"]/div[5]/a[2]').click()

        #Se a empresa for filiada a sindicato alterar o XPATH para a opção que deseja. 
        #Por padrão é "Não é filiada a sindicato"
        filiada_a_sindicato = driver.find_element_by_xpath('//*[@id="form:indFilicaoSindicato:1"]').click()

        #PASSA PARA A PROXIMA PAGINA
        pagina_responsavel = driver.find_element_by_xpath('//*[@id="tab3"]/div[6]/a[2]').click()

        time.sleep(5)

        #Insirindo as informações padrão
        #______________________

        cpf_responsavel = "123.456.789-00" #Insira as informações 
        
        field_responsavel = driver.find_element_by_xpath('//*[@id="form:cpfResponsavel"]')
        field_responsavel.click()
        time.sleep(0.5)
        field_responsavel = field_responsavel.send_keys(cpf_responsavel)
        
        datanascimento_responsalvel = "19/03/2019"

        field_datanascimento= driver.find_element_by_xpath('//*[@id="form:dataNascimentoResponsavel"]')
        field_datanascimento.click()
        time.sleep(0.5)
        field_datanascimento = field_datanascimento.send_keys(datanascimento_responsalvel)

        nome_responsavel = "Joaozinho"
        field_nomeresponsavel = driver.find_element_by_xpath('//*[@id="form:nomeResponsavel"]').send_keys(nome_responsavel)

        btn_finalizar = driver.find_element_by_xpath('//*[@id="form:enviar"]').click()
        time.sleep(0.5)
        print("  ")
        print("RAIS ENVIADO")
        print("______")
        print("______")
        print("  ")
        print("Fazendo o download da GUIA da empresa:   ", razao)
        btn_download = driver.find_element_by_xpath('//*[@id="form:imprimir"]').click()

        # O pdf vai esta no diretorio padrão que foi passado na linha 25
        btn_imprimir = driver.find_element_by_xpath('//*[@id="gerar-pdf"]').click()
        func_rename_arquivo(lista_razao[i],razao)
        print("  ")
        print("Guia emitida com sucesso:     ", razao)
        print("_")
        print("Proxima empresa... ")
        print("_")
        time.sleep(5)
       
    except:
        func_first_page(cnpj) 
 
        #Funções para pegar o CNPJ,RAZAO SOCIAL, CNAE, NATUREZA JURIDICA, OPTANTE PELO SIMPLES,LOGRADOURO,CEP E CIDADE de um arquivo em excel.
def read_csv_cnpj():
    Cnpj = [] #criando a lista
    with open('LISTA.csv','r',encoding='utf-8-sig') as csvfile: #Conf o nome do arquivo e formatação
        reader = csv.DictReader(csvfile,delimiter=";",lineterminator="\n")
        for row in reader:
            Cnpj.append(row['Cnpj'])       #add a coluna Cnpj na lista criada acima.
    return Cnpj # retornando a lista já preenchida

def read_csv_razao():
    Razao = [] 
    with open('LISTA.csv','r',encoding='utf-8-sig') as csvfile: 
        reader = csv.DictReader(csvfile,delimiter=";",lineterminator="\n")
        for row in reader:
            Razao.append(row['Razao'])       
    return Razao

def read_csv_cnae():
    Cnae = [] 
    with open('LISTA.csv','r',encoding='utf-8-sig') as csvfile: 
        reader = csv.DictReader(csvfile,delimiter=";",lineterminator="\n")
        for row in reader:
            Cnae.append(row['Cnae'])      
    return Cnae

def read_csv_natureza_juridica():
    Natureza_juridica = [] #criando a lista
    with open('LISTA.csv','r',encoding='utf-8-sig') as csvfile:
        reader = csv.DictReader(csvfile,delimiter=";",lineterminator="\n")
        for row in reader:
            Natureza_juridica.append(row['Natureza_juridica'])       
    return Natureza_juridica

def read_csv_optante_simples():
    Optante_simples = [] #criando a lista
    with open('LISTA.csv','r',encoding='utf-8-sig') as csvfile: 
        reader = csv.DictReader(csvfile,delimiter=";",lineterminator="\n")
        for row in reader:
            Optante_simples.append(row['Optante_simples'])    
    return Optante_simples

def read_csv_logradouro():
    Logradouro = [] #criando a lista
    with open('LISTA.csv','r',encoding='utf-8-sig') as csvfile: 
        reader = csv.DictReader(csvfile,delimiter=";",lineterminator="\n")
        for row in reader:
            Logradouro.append(row['Logradouro'])    
    return Logradouro

def read_csv_cep():
    Cep = [] #criando a lista
    with open('LISTA.csv','r',encoding='utf-8-sig') as csvfile: 
        reader = csv.DictReader(csvfile,delimiter=";",lineterminator="\n")
        for row in reader:
            Cep.append(row['Cep'])       
    return Cep

def read_csv_cidade():
    Cidade = [] 
    with open('LISTA.csv','r',encoding='utf-8-sig') as csvfile: 
        reader = csv.DictReader(csvfile,delimiter=";",lineterminator="\n")
        for row in reader:
            Cidade.append(row['Cidade'])      
    return Cidade

#FUNÇÃO PARA RENOMEAR O NOME DO ARQUIVO. Obs: O nome da empresa vai ser o nome do arquivo. Caso queira que o nome do arquivo seja outro, substituir a var "razao" na linha 243 pela var que você quer.
def func_rename_arquivo(nome_novo,razao):
    time.sleep(5)
    old_file = os.path.join(r"C:\Users\SEUCAMINHO\Desktop\Rais\Saida", "Recibo_de_Entrega_RAIS.pdf")    # O diretorio é o mesmo da linha 25
    new_file = os.path.join(r"C:\Users\SEUCAMINHO\Desktop\Rais\Saida",str(str(razao)+".pdf"))
    os.rename(old_file, new_file)
    return new_file

#PASSANDO A FUNÇÃO PARA VARIAVEL
lista_cnpj = read_csv_cnpj()
lista_razao = read_csv_razao()
lista_cnae = read_csv_cnae()
lista_natureza_juridica = read_csv_natureza_juridica()
lista_optante_simples = read_csv_optante_simples()
lista_logradouro = read_csv_logradouro()
lista_cep = read_csv_cep()
lista_cidade = read_csv_cidade()
#CONT
quantidade_empresas_csv = len(lista_cnpj)

#Loop para quando finalizar uma empresa, passar para outra.
for i in range(0,quantidade_empresas_csv):
    func_first_page(lista_cnpj[i],lista_razao[i],lista_cnae[i],lista_natureza_juridica[i],lista_optante_simples[i],lista_logradouro[i],lista_cep[i],lista_cidade[i])
