from pathlib import Path

import mkdocs_gen_files

# Define o nome do pacote Python principal (src/your_cross)
SRC_PACKAGE = "your_cross"

# Caminho absoluto para o diretório onde está o código-fonte
SRC_PATH = Path("src") / SRC_PACKAGE

# Caminho onde serão gerados os arquivos de documentação (.md)
DOCS_REF_PATH = Path("docs/reference")

# Percorre recursivamente todos os arquivos .py dentro de src/your_cross
for py_file in sorted(SRC_PATH.rglob("*.py")):
    # Ignora arquivos __init__.py, pois geralmente não contêm conteúdo útil isoladamente
    if py_file.name == "__init__.py":
        continue

    # Converte o caminho do arquivo Python para um caminho relativo sem extensão .py
    # Exemplo: src/your_cross/core/utils.py → core/utils
    module_path = py_file.relative_to(SRC_PATH).with_suffix("")

    # Converte esse caminho em formato de módulo Python
    # Exemplo: core/utils → core.utils
    module_name = ".".join(module_path.parts)

    # Define o caminho final do arquivo Markdown a ser criado
    # Exemplo: docs/reference/core/utils.md
    doc_file_path = DOCS_REF_PATH / module_path.with_suffix(".md")

    # Garante que o diretório onde o arquivo será salvo existe
    doc_file_path.parent.mkdir(parents=True, exist_ok=True)

    # Escreve o conteúdo Markdown do arquivo de documentação
    # O bloco ::: é usado pelo plugin mkdocstrings para gerar a documentação automaticamente
    with mkdocs_gen_files.open(doc_file_path, "w") as f:
        f.write(f"# `{module_name}`\n\n")
        f.write(f"::: {SRC_PACKAGE}.{module_name}\n")
