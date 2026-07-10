from __future__ import annotations

from uuid import UUID

from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate

class UserService:
    """
    Handles all user-related database operations.
    """

    @staticmethod
    def create_user(db: Session, user_data: UserCreate) -> User:
        """
        Create a new user.
        """

        user = User(
            full_name=user_data.full_name,
            email=user_data.email,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    
    @staticmethod
    def get_user(db: Session, user_id: UUID) -> User | None:
        """
        Get a user by ID.
        """

        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )
    
    @staticmethod
    def get_users(db: Session) -> list[User]:
        """
        Return all users.
        """

        return db.query(User).all()
    
    @staticmethod
    def update_user(
        db: Session,
        user: User,
        user_data: UserUpdate,
    ) -> User:
        """
        Update an existing user.
        """

        update_data = user_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(user, key, value)

        db.commit()
        db.refresh(user)

        return user
    
    @staticmethod
    def delete_user(
        db: Session,
        user: User,
    ) -> None:
        """
        Delete a user.
        """

        db.delete(user)
        db.commit()