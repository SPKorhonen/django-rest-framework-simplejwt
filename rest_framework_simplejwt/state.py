from django.contrib.auth import get_user_model

from .backends import TokenBackend
from .settings import api_settings

User = get_user_model()
token_backend = TokenBackend(
    algorithm=.ALGORITHM,
    signing_key=api_settings.SIGNING_KEY,
    verifying_key=api_settings.VERIFYING_KEY,
    secret_key=api_settings.JWT_SECRET_KEY,
    get_user_secret_key=api_settings.GET_USER_SECRET_KEY)
    audience=api_settings.AUDIENCE,
    issuer=api_settings.ISSUER
)
