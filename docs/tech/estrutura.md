# Estrutura do Projeto

```text
your-cross/
├── pyproject.toml
├── mkdocs.yml
├── src/
│   ├── config/         ← Projeto Django
│   └── your_cross/     ← Pacote do sistema
├── tests/              ← Testes automatizados
├── docs/               ← Documentação do projeto
└── .venv/              ← Ambiente virtual (via poetry)
```

## Diagrama de arquitetura (Mermaid)

```mermaid
graph TD
    subgraph Backend
        A[Django Views] --> B[Camada de Aplicação]
        B --> C[Modelos Django]
        C --> D[(PostgreSQL)]
    end

    subgraph Frontend
        E[htmx] --> A
        F[Alpine.js] --> A
    end

    G[Usuário] --> E