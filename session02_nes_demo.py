"""
SESSION 02 — NEXT EDIT SUGGESTIONS (NES) DEMO
==============================================
INSTRUCTOR INSTRUCTIONS:
  Step 1: Open this file in VS Code with Copilot active.
  Step 2: On line 17, change the variable name 'user_id' → 'account_id'
  Step 3: Press Tab at each ghost-text highlight — NES propagates the rename
          to EVERY other usage of user_id in this file automatically.
  Step 4: Show students the colour-coded ghost text appearing across the file.

NOTE: Enable NES in settings.json:
  "github.copilot.nextEditSuggestions.enabled": true
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass
class User:
    user_id: str          # ← RENAME THIS to 'account_id' and watch NES propagate
    username: str
    email: str
    created_at: datetime = field(default_factory=datetime.utcnow)
    is_active: bool = True


class UserRepository:
    """In-memory user store for demo purposes."""

    def __init__(self) -> None:
        self._store: dict[str, User] = {}

    def save(self, user: User) -> User:
        self._store[user.user_id] = user    # NES will suggest: account_id
        return user

    def find_by_id(self, user_id: str) -> Optional[User]:   # NES: account_id
        return self._store.get(user_id)     # NES: account_id

    def delete(self, user_id: str) -> bool:                  # NES: account_id
        if user_id in self._store:          # NES: account_id
            del self._store[user_id]        # NES: account_id
            return True
        return False

    def exists(self, user_id: str) -> bool:                  # NES: account_id
        return user_id in self._store       # NES: account_id


class UserService:
    """Business logic layer — calls repository."""

    def __init__(self, repo: UserRepository) -> None:
        self.repo = repo

    def create_user(self, user_id: str, username: str, email: str) -> User:
        if self.repo.exists(user_id):       # NES: account_id
            raise ValueError(f"User {user_id} already exists")  # NES: account_id
        user = User(user_id=user_id, username=username, email=email)  # NES ×2
        return self.repo.save(user)

    def get_user(self, user_id: str) -> User:                # NES: account_id
        user = self.repo.find_by_id(user_id)                 # NES: account_id
        if not user:
            raise KeyError(f"No user found with id={user_id}")  # NES: account_id
        return user

    def deactivate_user(self, user_id: str) -> User:         # NES: account_id
        user = self.get_user(user_id)                        # NES: account_id
        user.is_active = False
        return self.repo.save(user)


# ── Demo runner ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    repo = UserRepository()
    svc = UserService(repo)

    u = svc.create_user(
        user_id="u-001",          # NES: account_id=
        username="alice",
        email="alice@example.com"
    )
    print(f"Created: {u.user_id}")  # NES: u.account_id
    print(f"Active : {u.is_active}")

    svc.deactivate_user(u.user_id)  # NES: u.account_id
    fetched = svc.get_user(u.user_id)  # NES: u.account_id
    print(f"After deactivate: {fetched.is_active}")
