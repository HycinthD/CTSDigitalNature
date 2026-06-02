import configparser

class Config:
    def __init__(self, filename):
        self.filename = filename
        self.config = configparser.ConfigParser()

    def load(self):
        self.config.read(self.filename)

class DatabaseConfig(Config):
    def validate(self):
        required_keys = ["host", "user", "password", "database"]

        if "DATABASE" not in self.config:
            print("DATABASE section missing")
            return False

        for key in required_keys:
            if key not in self.config["DATABASE"]:
                print(f"Missing key: {key}")
                return False

        return True

db_config = DatabaseConfig("db.ini")
db_config.load()

if db_config.validate():
    print("Database Configuration Loaded")
    print(dict(db_config.config["DATABASE"]))