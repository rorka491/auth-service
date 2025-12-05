from tortoise import BaseDBAsyncClient

RUN_IN_TRANSACTION = True


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "users" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "username" VARCHAR(255) NOT NULL UNIQUE,
    "email" VARCHAR(255) UNIQUE,
    "password" VARCHAR(128) NOT NULL
);"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "users";"""


MODELS_STATE = (
    "eJztlW9r2zAQxr9K8KsOupF46Rr2Lg2MbWwpdOsYlGIutmKLyJIrndeW4u9enezEjvOHpL"
    "R0GXvnPPecdPeLpHvwUhUxYd5dGqa9j50HT0LK7MeSftzxIMtqlQSEiXDG3DqcAhODGkK0"
    "4hSEYVaKmAk1z5AraVWZC0GiCq2Ry7iWcslvchagihkmrpCraytzGbE7ZuY/s1kw5UxES3"
    "XyiPZ2eoD3mdO+SPzkjLTbJAiVyFNZm7N7TJRcuLlEUmMmmQZktDzqnMqn6qo25x2VldaW"
    "ssRGTsSmkAtstLsjg1BJ4merMa7BmHZ56/f6p/3B+w/9gbW4ShbKaVG2V/deJjoC459e4e"
    "KAUDocxpob/W3ue4XeKAG9Hl8zpwXRlt6GOEf2qhRTuAsEkzEmhO7kZAuzX8OL0efhxZF1"
    "vaFelD3M5REfVyG/jBHYGiRLgYt9KC4SnoSwAvQvEczAmFul11zkzRCbOc9zFOdCTbJ+xV"
    "4CZc8f7IDSujaidLGioKdxOmtcchImEM5uQUfBSkT5apN3NZT6aVsBCbHDQ01SB9WkGDLN"
    "w2TdDKkiW6cI1J7/Y+SAxsgfO/yppD2ubiPlMG/uizyCdDX2gFjZDxNgr9vd5enrdjc/fR"
    "RbBmh3RFbewWWIX3+cj9dDbKS0QF5K2+BVxEM87ghu8PrvxLqFInVNRafG3IgmvKPvw99t"
    "rqNv52eOgjIYa7eKW+DstcdL8Qj65AUg"
)
