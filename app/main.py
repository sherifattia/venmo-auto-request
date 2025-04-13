import logging
import os
from pathlib import Path
from dotenv import load_dotenv
import asyncio

from app.models.config import AppConfig, VenmoConfig, EmailConfig, GoogleSheetsConfig
from app.services.container import ServiceContainer
from app.services.email_service import EmailService
from app.services.sheets_service import SheetsService

# Load environment variables
load_dotenv()

def create_config() -> AppConfig:
    """Create application configuration from environment variables"""
    return AppConfig(
        venmo=VenmoConfig(
            access_token=os.getenv("VENMO_ACCESS_TOKEN"),
            client_id=os.getenv("VENMO_CLIENT_ID"),
            client_secret=os.getenv("VENMO_CLIENT_SECRET")
        ),
        email=EmailConfig(
            smtp_user=os.getenv("EMAIL_USER"),
            smtp_app_password=os.getenv("EMAIL_APP_PASSWORD"),
            notification_email=os.getenv("NOTIFICATION_EMAIL")
        ),
        google_sheets=GoogleSheetsConfig(
            credentials_path=Path(os.getenv("GOOGLE_SHEETS_CREDENTIALS_PATH")),
            spreadsheet_id=os.getenv("GOOGLE_SHEETS_SPREADSHEET_ID")
        ),
        log_level=os.getenv("LOG_LEVEL", "INFO")
    )

async def main():
    # Configure logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    try:
        # Load configuration
        config = AppConfig.load()
        
        # Create and connect service container
        container = ServiceContainer(config)
        await container.__connect__()
        
        # Get services from container
        email_service = container.email_service
        sheets_service = container.sheets_service
        
        # TODO: Implement payment processing
        logger.info("Starting payment processing...")

    except Exception as e:
        logger.error(f"Error in main: {str(e)}")
        if 'container' in locals():
            await container.__disconnect__()
            container.email_service.send_error_notification(e, "main execution")

if __name__ == "__main__":
    asyncio.run(main())
