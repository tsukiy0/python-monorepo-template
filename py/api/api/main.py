from api.app import app


def main():
    return app


# poetry run uvicorn api.main:main --reload --port 5000
