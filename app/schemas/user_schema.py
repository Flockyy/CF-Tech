from pydantic import BaseModel, Field, EmailStr


class UserCreate(BaseModel):
    """
    User creation model that can be used for creating new users.
    This model can be extended with additional fields specific to different user roles.
    """

    first_name: str = Field(..., min_length=2, max_length=50)
    last_name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr = Field(..., unique=True, max_length=255)
    role: str = Field(default="user", max_length=20)


class UserUpdate(BaseModel):
    """
    User update model that can be used for updating existing users.
    This model can be extended with additional fields specific to different user roles.
    """

    first_name: str = Field(None, min_length=2, max_length=50)
    last_name: str = Field(None, min_length=2, max_length=50)
    email: EmailStr = Field(None, unique=True, max_length=255)
    is_active: bool = Field(None)
    role: str = Field(None, max_length=20)  # e.g., "user", "admin", "trainer"
