
import json
import os
import logging
from common.helper import getDatetimeFormat

from adapters.firebase.FirebaseBackupInfra import FirebaseBackupInfra
from adapters.aws.BucketBaseInfra import BucketBaseInfra

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BackupLogic:

    def __init__(self):
        logger.info("Inicializando BackupServices...")
        self.bucketName = os.getenv("BUCKET_NAME_FOR_BACKUP_FIREBASE")
        if not self.bucketName:
            logger.error("La variable de entorno BUCKET_NAME_FOR_BACKUP_FIREBASE no está configurada.")
        else:
            logger.info("Bucket Name: %s", self.bucketName)

    def generateBackupFromFirebase(self):        

        logger.info("backupServices:init - generateBackupFromFirebase %s")        
        bucketBaseInfra=BucketBaseInfra()
        firebaseBackupInfra=FirebaseBackupInfra()

        logger.info("backupServices:method - invoice getDataForBackup%s")
        getDataSerialize=json.dumps(firebaseBackupInfra.getDataForBackup())

        logger.info("backupServices:method - invoice s3%s",self.bucketName)
        bucketBaseInfra.upload_to_s3(self.bucketName,"backup-"+getDatetimeFormat()+".json",getDataSerialize,"application/json")
        logger.info("backupServices:end")
        return None
