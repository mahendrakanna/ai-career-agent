from __future__ import annotations

from uuid import UUID

from sqlalchemy.orm import Session

from app.models.company import Company
from app.schemas.company import CompanyCreate, CompanyUpdate


class CompanyService:
    """
    Handles all company-related database operations.
    """

    @staticmethod
    def create_company(
        db: Session,
        company_data: CompanyCreate,
    ) -> Company:
        company = Company(
            name=company_data.name,
            website=company_data.website,
            linkedin_url=company_data.linkedin_url,
        )

        db.add(company)
        db.commit()
        db.refresh(company)

        return company

    @staticmethod
    def get_company(
        db: Session,
        company_id: UUID,
    ) -> Company | None:
        return (
            db.query(Company)
            .filter(Company.id == company_id)
            .first()
        )

    @staticmethod
    def get_companies(
        db: Session,
    ) -> list[Company]:
        return db.query(Company).all()

    @staticmethod
    def update_company(
        db: Session,
        company: Company,
        company_data: CompanyUpdate,
    ) -> Company:

        update_data = company_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(company, key, value)

        db.commit()
        db.refresh(company)

        return company

    @staticmethod
    def delete_company(
        db: Session,
        company: Company,
    ) -> None:

        db.delete(company)
        db.commit()