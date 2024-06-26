from sqlalchemy.orm import Session

from src.database.models import ApiKey


def get_user_ai_model_names(db: Session, user_id: int) -> list[str]:
    """
    Retrieves all AI model names associated with the user from the database based on the user's ID.

    Args:
        db (Session): The database session.
        user_id (int): The user's ID.

    # Returns:
    #     list[str]: A list of AI models.
    """

    ai_models = (
        db.query(ApiKey.ai_model)
        .filter(ApiKey.user_id == user_id)  # noqa
        .order_by(ApiKey.id.asc())
        .all()
    )

    return [ai_model[0] for ai_model in ai_models]
