para executar o script no google chrome é necessário o chrome driver para executar scripts de automação.
você pode insta-lo diretamente do site da google em: https://googlechromelabs.github.io/chrome-for-testing/
também será necessário instalar o package do selenium em seu interpretador de preferência.

alterações no código:

na linha 10 você terá que colocar o caminho onde você baixou o chrome driver.
na linha 39 você terá que trocar o link onde o script irá começar a excluir os emails, normalmente será necessário trocar somente o número que está localizado a última página.
na linha 92 e 93 você colocará o email e a senha para o script acessar a conta do hostinger para iniciar o processo.
e finalmente na linha 96 você colocará quantas vezes o script repetirá o processo.
