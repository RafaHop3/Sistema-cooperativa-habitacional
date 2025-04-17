# Usa uma imagem leve do Python
FROM python:3.11-slim

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia todos os arquivos da pasta atual para dentro do container
COPY . .

# Instala as dependências do projeto (confira se o requirements.txt existe!)
RUN pip install --no-cache-dir -r requirements.txt

# Expõe a porta 5000 (usada pelo Flask por padrão)
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["python", "app.py"]
