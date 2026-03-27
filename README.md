# 🛒 CRUD Python API - FastAPI

Esta é uma API robusta para gerenciamento de produtos, desenvolvida com **FastAPI**. O projeto foca em boas práticas de programação, utilizando tratamento de exceções e validação de dados para garantir que o sistema seja resiliente e seguro.

---

## 🚀 Tecnologias Utilizadas

* **Linguagem:** Python 3.14+
* **Framework:** FastAPI
* **Servidor:** Uvicorn (ASGI)
* **Ambiente:** Fedora Linux

---

## 🛠️ Como Executar o Projeto

Siga os passos abaixo para rodar a aplicação localmente:

### 1. Ative o ambiente virtual (venv)

```bash
source venv/bin/activate
```

### 2. Instale as dependências

```bash
pip install fastapi uvicorn
```

### 3. Inicie o servidor de desenvolvimento

```bash
uvicorn main:app --reload
```

### 4. Acesse a documentação interativa

O FastAPI gera automaticamente uma interface para testes:

👉 http://127.0.0.1:8000/docs

---

## 🛡️ Tratamento de Erros e Validação

O diferencial desta API está na implementação de segurança nas rotas, garantindo estabilidade e previsibilidade:

* **Try/Except:**
  Utilizado em todas as rotas para capturar falhas inesperadas (**Erro 500**), evitando que o servidor trave.

* **`raise HTTPException`:**
  Usado para validar regras de negócio.
  Exemplo: ao tentar cadastrar um produto com preço negativo, a API retorna **Erro 400 (Bad Request)** com mensagem personalizada.

* **Tratamento de 404:**
  Caso um produto não seja encontrado nas rotas de atualização ou remoção, a API responde corretamente com:

  ```
  Produto não encontrado
  ```

---

## 🛣️ Endpoints Disponíveis

| Método | Rota                            | Descrição                                   |
| ------ | ------------------------------- | ------------------------------------------- |
| GET    | `/produtos`                     | Lista todos os produtos cadastrados         |
| POST   | `/produtos/{id}/{nome}/{preco}` | Cadastra um novo produto (valida preço > 0) |
| PUT    | `/produtos/{id_procurado}`      | Atualiza o preço de um produto existente    |
| DELETE | `/produtos/{id_procurado}`      | Remove um produto da lista de forma segura  |

---

## 👨‍💻 Autor

Desenvolvido por **luizguiilhermedev** no Fedora Linux.
