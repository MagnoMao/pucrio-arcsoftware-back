# Biblioteca - API


A idéia inicial é um pequeno sistema de biblioteca onde é possível adicionar usuários e livros, bem como removê-los. Também é possível que um usuário pegue um livro emprestado, embora essa funcionalidade ainda não tenha sido implementada no Front end, é possível utilizar no back end via swagger por exemplo.
A persistência dos dados é feita através de um banco SQLite. Caso queira um banco de dados sem registros basta deletar o arquivo dele que o servidor cria um novo ao inicializar.

Eu utilizei a API externa ViaCEP [https://viacep.com.br/] para através do cep recuperar o nome do logradouro, bairro e estado. Implementei ela para autocompletar no front end e no back end. Infelizmente por causa de um problema utilizando o flask não consigo adicionar um endereço diretamente a partir do front via post; embora consigo adicionar novos livros e usuários.
Porém é possível adicionar novos endereços via swagger utilizando a API viaCEP.


---
## Como executar

Como está em Docker, basta simplesmente na pasta raiz do projeto (onde encontra-se o app.py) executar
flask run --host 0.0.0.0 --port 5000 para o servidor estar funcionando;
para utilizar e utilizar o swagger através do endereço
[http://localhost:5000/#/](http://localhost:5000/#/)

Se não fosse pelo Docker, seria necessário instalar as dependências através do comando

```
pip install -r requirements.txt
```
Observe que o terminal deve estar no mesmo diretório que o arquivo 'requirements.txt', caso contrário, imediatamente antes dele colocar o caminho apropriado.
Será necessário ter todas as libs python listadas no `requirements.txt` instaladas.
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.


Caso queria alterar os arquivos recomendo executar flask em modo desenvolvimento, pois assim ele reinicia o servidor toda vez que salvar uma alteração em algum arquivo.

```
flask run --host 0.0.0.0 --port 5000 --reload
```
