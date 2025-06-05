# Como instalar

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/your-cross
cd your-cross
```

2. Ative o ambiente com Poetry:

```bash
poetry install --with dev,docs
poetry shell
```

3. Rode o servidor local Django:

```bash
poetry run python src/manage.py runserver
```