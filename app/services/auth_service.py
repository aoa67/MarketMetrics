from datetime import datetime
from typing import Dict, Optional
from uuid import uuid4

from app.core.security import hash_password, verify_password

# TEMP storage (replace with DB in Phase 2)
_USERS_BY_EMAIL: Dict[str, dict] = {}


def register_user(email: str, password: str, display_name: str) -> dict:
    if email in _USERS_BY_EMAIL:
        raise ValueError("Email already registered")

    user = {
        "userID": str(uuid4()),
        "email": email,
        "passwordHash": hash_password(password),
        "displayName": display_name,
        "createdAt": datetime.utcnow(),
        "lastLoginAt": None,
    }
    _USERS_BY_EMAIL[email] = user
    return user


def authenticate_user(email: str, password: str) -> Optional[dict]:
    user = _USERS_BY_EMAIL.get(email)
    if not user:
        return None
    if not verify_password(password, user["passwordHash"]):
        return None

    user["lastLoginAt"] = datetime.utcnow()
    return user


def get_user_by_email(email: str) -> Optional[dict]:
    return _USERS_BY_EMAIL.get(email)
