import uuid
from typing import List, Dict, Optional

class MockDatabase:
    def __init__(self):
        self._users: List[Dict[str, str]] = [
            {
                "id": "a1b2c3d4-e5f6-7a8b-9c0d-1e2f3a4b5c6d",
                "nome": "Ana Silva",
                "email": "ana.silva@connect.com",
            },
            {
                "id": "b2c3d4e5-f6a7-8b9c-0d1e-2f3a4b5c6d7e",
                "nome": "Carlos Oliveira",
                "email": "carlos.oliveira@connect.com",
            },
        ]

    def _generate_id(self) -> str:
        return str(uuid.uuid4())

    def get_all_users(self) -> List[Dict[str, str]]:
        return self._users

    def get_user_by_id(self, user_id: str) -> Optional[Dict[str, str]]:
        for user in self._users:
            if user["id"] == user_id:
                return user
        return None

    def create_user(self, nome: str, email: str) -> Dict[str, str]:
        new_user = {"id": self._generate_id(), "nome": nome, "email": email}
        self._users.append(new_user)
        return new_user

    def update_user(self, user_id: str, nome: Optional[str] = None, email: Optional[str] = None) -> Optional[Dict[str, str]]:
        user = self.get_user_by_id(user_id)
        if not user:
            return None
        if nome is not None:
            user["nome"] = nome
        if email is not None:
            user["email"] = email
        return user

    def delete_user(self, user_id: str) -> bool:
        user = self.get_user_by_id(user_id)
        if user:
            self._users.remove(user)
            return True
        return False

db = MockDatabase()
