import os
import logging
import firebase_admin
from firebase_admin import credentials, firestore

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

cred = credentials.Certificate("conf/py-test-firebase.json")
firebase_admin.initialize_app(cred)

class FirebaseBackupInfra:
    
    def __init__(self, db_url=None):
        logger.info("constructor:init")
        self.db_url = db_url or os.getenv("FIREBASE_DB_URL")
        self.db = firestore.client()
        logger.info("constructor:end")
        
        
    def getDataForBackup(self):
        try:
            backup_data = {}            
            logger.info("firebaseBackupInfra:init - getDataForBackup")

            collections = self.db.collections()
            logger.info("firebaseBackupInfra:get collection")

            for collection in collections:
                collectionName = collection.id   
                backup_data[collectionName] = {}                
                logger.info("firebaseBackupInfra:get collection %s",collectionName)

            docs = collection.stream()
            for doc in docs:
                backup_data[collectionName][doc.id] = doc.to_dict()  

            logger.info("firebaseBackupInfra:end")
            return backup_data
        except Exception as e:
            logger.error("firebaseBackupInfra:error %s",{e})
       

# ins=FirebaseBackupInfra()  logger.info("response:%s", ins.getDataForBackup())
