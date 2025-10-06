#!/bin/bash
# Este comando 'set -e' faz o script parar imediatamente se algum comando falhar
set -e

echo "--- Iniciando a instalação do Flutter ---"

# 1. Instala o Flutter com permissões de administrador
sudo git clone https://github.com/flutter/flutter.git /usr/local/flutter
sudo chown -R $(whoami) /usr/local/flutter

# 2. Cria um arquivo de configuração global para o PATH.
# Esta é a maneira mais robusta de garantir que o comando 'flutter' seja encontrado
# por qualquer terminal que você abrir.
echo 'export PATH="$PATH:/usr/local/flutter/bin"' | sudo tee /etc/profile.d/flutter.sh

echo "--- Flutter instalado. Executando precache para a web... ---"
# 3. Executa o precache para web, usando o caminho completo para garantir
/usr/local/flutter/bin/flutter precache --web

echo "--- Configuração do Flutter concluída com sucesso! ---"