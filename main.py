from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

produtos = [
    {"id": 1, "nome": "Teclado Mecânico", "preco": 250.0},
    {"id": 2, "nome": "Mouse Gamer", "preco": 120.0}
]

@app.get("/produtos")
def listar_produtos():
    return produtos

@app.post("/produtos/{id}/{nome}/{preco}")
def criar_produto(id: int, nome: str, preco: float):
    novo = {"id": id, "nome": nome, "preco": preco}
    produtos.append(novo)
    return {"mensagem": "Produto cadastrado!", "item": novo}

@app.put("/produtos/{id_procurado}")
def atualizar_preco(id_procurado: int, novo_preco: float):
    for p in produtos:
        if p["id"] == id_procurado:
            p["preco"] = novo_preco
            return {"mensagem": "Preço atualizado!", "produto": p}
    
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.delete("/produtos/{id_procurado}")
def deletar_produto(id_procurado: int):
    for index, p in enumerate(produtos):
        if p["id"] == id_procurado:
            removido = produtos.pop(index)
            return {"mensagem": f"O item {removido['nome']} foi removido."}
            
    raise HTTPException(status_code=404, detail="Produto não encontrado")