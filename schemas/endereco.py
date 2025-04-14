from pydantic import BaseModel
from model.endereco import Endereco
from typing import List

class EnderecoSchema(BaseModel):
    """ Define como um novo encereço a ser inserido deve ser representado
    """
    cep: str = "CEP"
    logradouro: str = "Logradouro"
    bairro: str = "Bairro"
    uf: str = "UF"
    numero: int = 0
    complemento: str = "Complemento"
    endereco_de: str = "id do usuario"

class EnderecoViewSchema(BaseModel):
    """ Define como um endereço será retornado
    """
    id: int = 1
    cep: str = "CEP"
    logradouro: str = "Logradouro"
    bairro: str = "Bairro"
    uf: str = "UF"
    numero: int = 0
    complemento: str = "Complemento"
    endereco_de: str = "id do usuario"

class ListagemEnderecosSchema(BaseModel):
    """ Define como uma listagem de enderecos será retornada.
    """
    livros:List[EnderecoViewSchema]

def apresenta_enderecos(enderecos: List[Endereco]):
    """ Retorna uma representação dos enderecos seguindo o schema definido em
        EnderecoViewSchema.
    """
    result = []
    for endereco in enderecos:
        result.append({
            "id": endereco.id,
            "cep": endereco.cep,
            "logradouro": endereco.logradouro,
            "bairro": endereco.bairro,
            "uf": endereco.uf,
            "numero": endereco.numero,
            "complemento": endereco.complemento,
            "endereco_de": endereco.endereco_de
        })

    return {"livros": result}