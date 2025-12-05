from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "admin" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(32) NOT NULL UNIQUE,
    "password" VARCHAR(128) NOT NULL,
    "is_active" BOOL NOT NULL DEFAULT True
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "admin";"""


MODELS_STATE = (
    "eJztl21v2jAQx78K4lUrdRMEuqK9A7RpnVqQujJNqqrIJCZYOHZqO31QxXefzwlxEgiCdq"
    "gw8Y78786++8l3J17rIfcxlZ+7fkhY/Wvttc5QiPWPouGsVkdRZGUQFBpT44kyl7FUAnlK"
    "ixNEJdaSj6UnSKQIh9NZTCmI3NOOhAVWihl5iLGreIDVFAttuLvXMmE+fsZy8RnN3AnB1C"
    "8kSny42+iueomMdsnUd+MIt41dj9M4ZNY5elFTzjJvwhSoAWZYIIXheCViSB+yS8tcVJRk"
    "al2SFHMxPp6gmKpcuRsy8DgDfjobaQoM4JZPTrN90e60vrQ72sVkkikX86Q8W3sSaAgMbu"
    "tzY0cKJR4Go+UWSyzM7yV6/SkSq/HlY0oQdepliAtkH0oxRM8uxSxQU/3ZctYg+9296f/o"
    "3py0nFOohOunnDzwQWpxjAmoWooRkvKJixVvsJpiPubfUFwIFqNtwF1wbDqdDUBqr0qSxl"
    "ZESaSrhwd5XPEie5xTjFhFT+fjSjzHOnBXQLOX+iaga/j1hsMrSDqU8oEa4fK2xHF03fum"
    "ARu82okobJseJuVklut5EMbImz0h4btLFu7wKt9lU+iEZQUxFBhCUCdUlW6OkTRzfGmjGH"
    "3tQoEpI48L5bhQ9n+hOOfnGwxC7VU5CI2tOAhxiAjdhmIW8CaEKaD/ieBxK79rK+/JBuli"
    "Qbzpqh2SWtZuEWR9jmvkgNbIo17+kNIWrZsLOczO3ckQhNbYAmLqfpgAm43GJqOv0agefW"
    "ArAtQ3Kpz0YBHiz1/DwWqIuZASyBHTBd75xFNnNUqkut9PrGsoQtWFvyULeCfX3T9lrv2r"
    "Yc9Q4FIFwpxiDuh99HqZ/wWRdQlU"
)
