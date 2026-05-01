from uuid import UUID, uuid4
from pydantic import BaseModel, Field, EmailStr

class Usuario(BaseModel):
    nome: str
    email: EmailStr
    senha: str
    id: UUID = Field(default_factory=uuid4)

    def to_dict(self):
        return {
            "nome": self.nome,
            "email": self.email,
            "senha": self.senha,
            "id": self.id
        }