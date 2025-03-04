import os
import logging
import firebase_admin
from firebase_admin import credentials, firestore

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
cred_path = os.path.join(base_dir, "conf", "py-test-firebase.json")

if not firebase_admin._apps:    
    logger.info(cred_path)
    cred = credentials.Certificate(cred_path)
    firebase_admin.initialize_app(cred,{'timeout': 120})
    logger.info("Firebase inicializado correctamente.")
else:
    logger.info("Firebase ya estaba inicializado.")
    
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