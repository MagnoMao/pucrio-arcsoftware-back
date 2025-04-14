from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from datetime import datetime
from typing import Union

from  model import Base


class Endereco(Base):
    __tablename__ = 'endereco'

    id = Column(Integer, primary_key=True)
    cep = Column(String(140))
    logradouro = Column(String(140))
    bairro = Column(String(140))
    uf = Column(String(2))
    numero = Column(Integer)
    complemento = Column(String(140))
    endereco_de = Column(ForeignKey("usuario.id"))

    def __init__(self, cep:str, logradouro:str, bairro:str, uf:str, numero:int, complemento:str, endereco_de: int = None,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um endereço

        Arguments:
            cep: numero identificador do bairro e rua
            nome: nome da rua/avenida/estrada/etc...
            bairro: nome do bairro
            uf: sigla do estado
            endereco_de: id do usuário que mora neste endereço
        """
        self.cep = cep
        self.logradouro = logradouro
        self.bairro = bairro
        self.uf = uf
        self.numero = numero
        self.complemento = complemento
        self.endereco_de = endereco_de

