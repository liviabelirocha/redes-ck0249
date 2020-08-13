## OBJETIVO:

● Compreender como os recursos de comunicação em redes são utilizados na
construção de aplicações.

## TAREFA 1 - SERVIDOR HTTP

Nesta tarefa, você desenvolverá um servidor Web simples em Python ou Java, capaz de processar apenas uma requisição. Seu servidor Web:

● criará um socket de conexão quando contatado por um cliente (navegador);
● receberá a requisição HTTP dessa conexão;
● analisará a requisição para determinar o arquivo específico sendo requisitado;
● obterá o arquivo requisitado do sistema de arquivo do servidor;
● criará uma mensagem de resposta HTTP consistindo no arquivo requisitado
precedido por linhas de cabeçalho; e
● enviará a resposta pela conexão TCP ao navegador requisitante. Se um navegador
requisitar um arquivo que não está presente no seu servidor, seu servidor deverá
retornar uma mensagem de erro “404 Not Found”.

No site de apoio, oferecemos o código estrutural para o seu servidor escrito em Python. Sua tarefa é concluir o código, rodar seu servidor e depois testá-lo enviando requisições de navegadores rodando em hospedeiros diferentes. Se você rodar seu servidor em um hospedeiro que já tem um servidor Web rodando nele, então deverá usar uma porta diferente da porta 80 para o seu servidor.

## Algumas dicas:

● Os arquivos podem ser apenas do tipo .txt.
● É importante que os arquivos a serem acessados e o código do servidor estejam na
mesma máquina. Pode facilitar um pouco.
● Para acessar os arquivos por meio do browser, caso ele esteja no mesmo
computador em que o servidor está sendo executado, basta usar o endereço
localhost/nome_arquivo.extensão.

### Para rodar o código:

`$ python3 web-server.py`

O servidor estará rodando em `localhost:3333`

Daí é só acessar o servidor, colocando o arquivo desejado depois de uma `/`:

`Ex: localhost:3333/README.md`
