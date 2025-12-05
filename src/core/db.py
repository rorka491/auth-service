from src.core.config import DB_NAME, DB_PASSWORD, DB_USER, HOST_ADRESS



TORTOISE_ORM = {
    "connections": {
        "default": f"postgres://{DB_USER}:{DB_PASSWORD}@{HOST_ADRESS}/{DB_NAME}"
    },
    "apps": {
        "models": {
            "models": ["src.models", "aerich.models"],
            "default_connection": "default",
        }
    }
}
