import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Settings:
    app_name : str = os.getenv("APP_NAME")
    app_version : str = os.getenv("APP_VERSION")
    app_description : str = os.getenv(
        "APP_DESCRIPTION",
    )

    app_env : str = os.getenv("APP_ENV")
    app_hosts : str = os.getenv("APP_HOSTS")
    app_port : int = int(os.getenv("APP_PORT"))


settings = Settings()