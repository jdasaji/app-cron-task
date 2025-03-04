# Cargar variables de entorno desde el archivo .env
import os
import logging
import logging
import sys

from dotenv import load_dotenv
from applogic.BackupLogic import BackupLogic

# Determinar el entorno
environment = os.getenv("ENVIRONMENT", "dev")  # Valor por defecto es "dev" si no está configurado

# Cargar el archivo .env correspondiente
if environment == "prod":
    load_dotenv("env/prod.env")
elif environment == "uat":
    load_dotenv("env/uat.env")
else:
    load_dotenv("env/dev.env")


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def lambda_handler(event, context):
    logger.info("lambdaBackupDatabase:init - lambda_handler %s")        
    backupServices=BackupLogic()
    backupServices.generateBackupFromFirebase()
    logger.info("lambdaBackupDatabase:end%s")        
    return {
        "statusCode": 200,
        "body": f"Archivo subido a S3 exitosamente."
    }

lambda_handler({}, {})  