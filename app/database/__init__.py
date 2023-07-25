from app.config.DatabaseConfig import DatabaseConfig

db = DatabaseConfig.load().connection
