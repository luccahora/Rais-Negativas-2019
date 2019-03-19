# Rais Negativas 2019 Web
Script para automatizar o preenchimento da rais negativas 2019 utilizando a linguagem Python e a Biblioteca Selenium.

<h3>O que o script faz.</h3>
<p>O script entra no site (http://www.rais.gov.br/sitio/negativa.jsf), e preenche os campos com informações retiradas de um arquivo csv.

<h3> Como utilizar</h3>
<b>Adicione a biblioteca Selenium</b>
<pre>pip install selenium</pre>

<b>Prepare o arquivo csv</b>

Campo Logradouro -  Não pode ter caracteres especiais.<br>
Campo Optante_simples - Se a empresa for Optante pelo Simples "sim". De resto "não"<br>
Campo cidade - A cidade deve está em maiúsculo e sem caracteres especiais. EXEMPLO (Ç,',^,´)<br>
Campo Razao Social - Deve está sem caracteres especiais.<br>
<b>Obs:</b> O estado está por padrão empresas da BAHIA, mas você pode alterar parar empresas do estado que deseja. Alterando na linha 97.<br>

O formato do CSV é "CSV (separado por vírgulas) (*.csv)"<br>
Logo após ter salvo o CSV, abra o arquivo com o bloco de notas e salve com a Codificação para <b>UTF-8.</b> <br>
<b>O nome por padrão do arquivo é LISTA. </b> <br>
  
![alt text](https://i.imgur.com/JPbJzx8.png)

<h3>Observações</h3>
<p> As informações fixas podem ser alteradas dentro do código.</p>
Em caso de dúvidas ao utilizar o Python com o Selenium, recomendo acessar.

[esse tutorial](http://pythonclub.com.br/selenium-parte-1.html#instalacao)
