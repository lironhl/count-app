import enum
import os


class CounterAppEnv(str, enum.Enum):
    Development = "Development"
    Production = "Production"


ENV = os.environ.get("YASHISH_ENV", CounterAppEnv.Development.value)
DB_URL = os.environ.get("DB_URL", "localhost")
DB_USERNAME = os.environ.get("DB_USERNAME", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "mysecretpassword")

COMMIT_SHA = os.environ.get("COMMIT_SHA")

DEV_ENV = ENV == CounterAppEnv.Development.value


class ApiTags(str, enum.Enum):
    Count = "Count"
