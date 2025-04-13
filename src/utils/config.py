"""src/utils/config.py"""


class AppConfig:
    """
    AppConfig: Application configuration.
    """
    
    APP_NAME: str = "Language predictor"
    
    @classmethod
    def initialize(cls) -> None:
        """
        Initialize the application configuration.
        """
        pass