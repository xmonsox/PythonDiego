from dotenv import load_dotenv # permite que python explore los archivos 
import os # entiende las rutas segun el sistema operativo

# Obtener la ruta al archivo .env
dotenv_path = os.path.join(os.path.dirname(__file__),'..', '.env')
# Cargar variables de entorno desde el archivo .env
load_dotenv(dotenv_path)

class Settings:
    # atributos constantes
    PROJECT_NAME: str = "GastosIngresos"
    PROJECT_VERSION: str = "2.0.0"
    PROJECT_DESCRIPTION: str = "Administracion de gastos e ingresos"


    DB_HOST: str = os.getenv("DB_HOST")
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_NAME: str = os.getenv("DB_NAME")
    DB_PORT: str = os.getenv("DB_PORT")

    # para conectarnos a la base de datos postgres
    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

    # para encriptar datos esta en .env
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    TOKEN_EXPIRE_MIN = 960 #IN MINS
    #es para el algoritmo de encriptacion que vamos a usar esra en .env
    ALGORITHM: os.getenv("ALGORITHM")

    settings = Settings()