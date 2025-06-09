# 📘 Dicionário de Dados

Este dicionário descreve as tabelas do sistema Your Cross, com seus respectivos campos, tipos, obrigatoriedade, chaves e descrições.

---

## 🧑‍🎓 Aluno

| Campo            | Tipo     | Obrigatório | Chave | Descrição                      |
|------------------|----------|-------------|-------|--------------------------------|
| id               | integer  | sim         | PK    | Identificador único do aluno   |
| nome             | string   | sim         | -     | Nome completo do aluno         |
| email            | string   | sim         | -     | Email do aluno                 |
| data_nascimento  | date     | não         | -     | Data de nascimento             |
| plano_id         | integer  | sim         | FK    | Plano financeiro vinculado     |
| usuario_id       | integer  | sim         | FK    | Usuário de login vinculado     |

---

## 🧑‍🏫 Professor

| Campo      | Tipo     | Obrigatório | Chave | Descrição                    |
|------------|----------|-------------|-------|------------------------------|
| id         | integer  | sim         | PK    | Identificador do professor  |
| nome       | string   | sim         | -     | Nome completo do professor  |
| email      | string   | sim         | -     | Email do professor          |
| usuario_id | integer  | sim         | FK    | Usuário vinculado           |

---

## 📋 Treino

| Campo        | Tipo     | Obrigatório | Chave | Descrição                         |
|--------------|----------|-------------|-------|-----------------------------------|
| id           | integer  | sim         | PK    | Identificador do treino           |
| titulo       | string   | sim         | -     | Título ou nome do treino          |
| descricao    | string   | não         | -     | Descrição detalhada               |
| aluno_id     | integer  | sim         | FK    | Aluno ao qual o treino pertence   |
| professor_id | integer  | sim         | FK    | Professor responsável             |

---

## 💳 Pagamento

| Campo        | Tipo     | Obrigatório | Chave | Descrição                      |
|--------------|----------|-------------|-------|--------------------------------|
| id           | integer  | sim         | PK    | Identificador do pagamento    |
| valor        | decimal  | sim         | -     | Valor pago                     |
| data         | date     | sim         | -     | Data do pagamento              |
| aluno_id     | integer  | sim         | FK    | Aluno que realizou o pagamento |
| metodo       | string   | sim         | -     | Forma de pagamento             |

---

## 🔐 Usuário

| Campo      | Tipo     | Obrigatório | Chave | Descrição                        |
|------------|----------|-------------|-------|----------------------------------|
| id         | integer  | sim         | PK    | Identificador do usuário         |
| username   | string   | sim         | -     | Nome de login                    |
| senha      | string   | sim         | -     | Hash da senha                    |
| tipo       | string   | sim         | -     | Tipo: admin, secretaria, aluno…  |

