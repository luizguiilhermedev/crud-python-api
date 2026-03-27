from fastapi import FastAPI, HTTPException
from typing import Optional

app = FastAPI()

produtos = [
    {"id": 1, "nome": "Teclado Mecânico", "preco": 250.0},
    {"id": 2, "nome": "Mouse Gamer", "preco": 120.0}
]

@app.get("/produtos")
def listar_produtos():
    try:
        return produtos
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao listar: {str(e)}")

@app.post("/produtos/{id}/{nome}/{preco}")
def criar_produto(id: int, nome: str, preco: float):
    try:
        if preco < 0:
            raise ValueError("O preço não pode ser negativo")
            
        novo = {"id": id, "nome": nome, "preco": preco}
        produtos.append(novo)
        return {"mensagem": "Produto cadastrado!", "item": novo}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro interno ao cadastrar")

@app.put("/produtos/{id_procurado}")
def atualizar_preco(id_procurado: int, novo_preco: float):
    try:
        for p in produtos:
            if p["id"] == id_procurado:
                p["preco"] = novo_preco
                return {"mensagem": "Preço atualizado!", "produto": p}
        
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail="Erro ao atualizar produto")

@app.delete("/produtos/{id_procurado}")
def deletar_produto(id_procurado: int):
    try:
        for index, p in enumerate(produtos):
            if p["id"] == id_procurado:
                removido = produtos.pop(index)
                return {"mensagem": f"O item {removido['nome']} foi removido."}
        
        raise HTTPException(status_code=404, detail="Produto não encontrado