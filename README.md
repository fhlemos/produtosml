# scrapy-ml
<h1> Busca simples de produto a partir de uma palavra-chave </h1>

## :hammer: Requisitos

- `Python 3`: (Ubuntu) sudo apt install python3-dev python3-pip
- `Scrapy`: (Ubuntu) pip install scrapy

## Configuração
Caso o user agent seja inválido, procurar no google digitando `my user agent` e adicionar na variável `USER_AGENT` do `settings.py`.
```bash
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
```
## Execução
Ao executar o comando `sh scrapy.sh` e informar o produto que deseja ser pesquisado, será criado um arquivo `result.json` com o resultado da pesquisa.
