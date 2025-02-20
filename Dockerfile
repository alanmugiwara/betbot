FROM python:3.9-alpine3.20

# Define diretório de trabalho
WORKDIR /home/betbot

# Atualiza pacotes e instala dependências
RUN apk update && apk add --no-cache openrc bash dos2unix

# Copia o requirements
COPY requeriments.txt ./

# Instala as dependências do Python
RUN pip install --no-cache-dir -r requeriments.txt

# Corrige problemas de formatação nos scripts
COPY betibot-alpine-exec.sh /app/
RUN dos2unix /app/betibot-exec.sh && chmod +x /app/betibot-alpine-exec.sh

# Copia o script principal do bot
COPY beti.py ./

# Copia o serviço OpenRC
COPY betibot /etc/init.d/betibot

# Adiciona o serviço ao OpenRC e habilita na inicialização
RUN rc-update add betibot default

# Define variáveis de ambiente | garante que output do script apareça em tempo real nos logs do Docker
ENV PYTHONUNBUFFERED=1

# Define o comando de inicialização do contêiner
CMD ["/app/betibot-alpine-exec.sh"]