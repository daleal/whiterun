from fintoc import Fintoc

from whiterun.config import settings


FINTOC_CLIENT = Fintoc(settings.fintoc_secret_key)
