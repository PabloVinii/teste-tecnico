# Teste-Técnico


Na primeira instalação configurar o ambiente

## Criar ambiente virtual
```
python -m venv .venv
```

## Ativar ambiente virtual
```
.\.venv\Scripts\activate
```

## Instalar dependências
```
pip install -r requirements.txt
```

## Configurar banco de dados
```
Importe o "dump.sql" para seu MySQL
Acesse o arquivo ".env" e preencha com os dados de acesso de seu banco
```

## Iniciar servidor
```
flask run
```

## Rodar Testes
```
python test_api.py
```
