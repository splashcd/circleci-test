class AppConfig:
    DB: str
    logging = "Test"

    def __init__(self):
        print("In AppConfig")


class DevConfig(AppConfig):
    DB = "dev"

    def __init__(self):
        print(" InDevConfig")


class StagingConfig(AppConfig):
    DB = "staging"

    def __init__(self):
        print("In StagingConfig")


class ProdConfig(AppConfig):
    DB = "Prod"

    def __init__(self):
        print("In ProdConfig")
