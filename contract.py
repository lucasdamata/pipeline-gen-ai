from datetime import datetime
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProductEnum(str, Enum):
    product_1 = "ZapFlow com Gemini"
    product_2 = "ZapFlow com chatGPT"
    product_3 = "ZapFlow com Llama3.0"

class Sales(BaseModel):
    """
    Modelo de dados para as vendas.

    Args:
        email (EmailStr): email do comprador
        data (datetime): data da compra
        valor (PositiveFloat): valor da compra
        produto (PositiveInt): nome do produto
        quantidade (PositiveInt): quantidade de produtos
        produto (ProdutoEnum): categoria do produto
    """

    email: EmailStr 
    date: datetime
    value: PositiveFloat
    quantity: PositiveInt
    product: ProductEnum