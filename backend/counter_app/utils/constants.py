import enum
import os

LOGIN_PATH = "/auth/login"


class YashishEnv(str, enum.Enum):
    Development = "Development"
    Production = "Production"


ENV = os.environ.get("YASHISH_ENV", YashishEnv.Development.value)
DB_URL = os.environ.get("DB_URL", "localhost")
DB_USERNAME = os.environ.get("DB_USERNAME", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "mysecretpassword")

COMMIT_SHA = os.environ.get("COMMIT_SHA")

SENTRY_DSN = "https://b9c04adac4c248b39b2a878e4c53634e@o419060.ingest.sentry.io/5956671"

DEV_ENV = ENV == YashishEnv.Development.value


class ApiTags(str, enum.Enum):
    Auth = "Auth"
    Users = "Users"
    Seniors = "Seniors"
    Interactions = "Interactions"
