import psycopg2
from app.config import settings


def get_db_connection():
    """
    Creates and returns a PostgreSQL database connection.
    
    Uses configuration from settings object which loads from environment variables.
    This approach:
    - Keeps credentials out of code
    - Makes it easy to switch between environments (dev/staging/prod)
    - Follows security best practices
    
    Returns:
        psycopg2.connection: Active database connection
        
    Example:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users")
        conn.close()
    """
    conn = psycopg2.connect(
        host=settings.DB_HOST,
        database=settings.DB_NAME,
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        port=settings.DB_PORT
    )
    return conn
