#so y python
FROM python:3.12-slim
#directorio de trabajo
WORKDIR /app
#copia de archivos ##como el git clon
COPY . /app
#instalacion de dependencias
RUN pip install --no-cache-dir -r requirements.txt
#puerto de trabajo
EXPOSE 5000
#comando para ejecutar la aplicacion
CMD ["python", "app.py"]