## Python

### Gerenciador de Pacotes
```
pip freeze > requirements.txt       # gerar o arquivo a partir do ambiente atual
pip install -r requirements.txt     # instalar as dependências listadas no arquivo
```

```
pip install pipreqs
pipreqs ~/caminho_ate_pasta_projeto
pipreqs .                           # pasta raiz do seu projeto para gerar o arquivo requirements.txt
pipreqs . --force                   # sobrescreve o arquivo requirements.txt existente
```