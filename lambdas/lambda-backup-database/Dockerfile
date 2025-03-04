# Imagen base de AWS Lambda con Python 3.9
FROM public.ecr.aws/lambda/python:3.9

# Establecer directorio de trabajo
WORKDIR /var/task

# Copiar el archivo de dependencias
COPY lambdas/lambda-backup-database/requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar:layer lambdas `main.py` correctamente
COPY lambdas/lambda-backup-database/main.py /var/task/
COPY lambdas/lambda-backup-database/cicd/ /var/task/src/

# Copiar:configuraciones
COPY common/ /var/task/common/
COPY env/ /var/task/env/
COPY conf/ /var/task/conf/
# Copiar:layer adapters
COPY adapters/ /var/task/adapters/
# Copiar:layer applogic
COPY applogic/ /var/task/applogic/


# Especificar el handler de Lambda
CMD ["main.lambda_handler"]
