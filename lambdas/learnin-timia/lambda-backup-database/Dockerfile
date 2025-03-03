# 🔹 Imagen base oficial de AWS Lambda para Python 3.9
FROM public.ecr.aws/lambda/python:3.9

# 🔹 Copiar el archivo requirements.txt del directorio lambda_handler
COPY conf/requirements.txt .

# 🔹 Instalar las dependencias desde requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 🔹 Copiar todo
COPY . /var/task/

# 🔹 Especificar el handler de la función Lambda (nombre del archivo y la función)
CMD ["main.lambda_handler"]
