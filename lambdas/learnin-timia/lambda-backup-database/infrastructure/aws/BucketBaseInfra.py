import boto3
class BucketBaseInfra:

    def __init__(self, region_name='us-east-1'):
        self.s3 = boto3.client('s3', region_name=region_name)

    def upload_to_s3(self,bucket_name,key_name,body,contentType):
        try:            
            self.s3.put_object(
                Bucket=bucket_name,
                Key=key_name,  # Nombre único para el archivo
                Body=body,  # El contenido del backup en JSON
                ContentType=contentType  # Tipo de contenido (JSON)
            )
            print(f'Backup subido exitosamente a S3 con el nombre {key_name}')
        except Exception as e:
            print(f'Ocurrió un error al subir el archivo a S3: {e}')