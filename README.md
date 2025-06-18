# docker
# Instalação do docker no Rock Linux v8.10
Obs: Deixe a instalação do Rocky Linux 8.10 com GUI e Docker "limpo" (sem Podman).

🔧 1. Remova Podman se veio por engano
Só por precaução:
sudo dnf remove -y podman buildah skopeo
🧰 2. Instale as dependências
sudo dnf install -y yum-utils device-mapper-persistent-data lvm2
📦 3. Adicione o repositório oficial do Docker
sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
🔒 4. Desabilite repositórios de teste/nightly
sudo yum-config-manager --disable docker-ce-nightly
sudo yum-config-manager --disable docker-ce-test
🐳 5. Instale o Docker "limpo"
sudo dnf install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
▶️ 6. Ative e inicie o serviço Docker
sudo systemctl enable docker
sudo systemctl start docker
🔍 7. Verifique se o Docker funciona
docker --version
E teste:
sudo docker run hello-world

# Nota: Podman pode ser instalado automaticamente como dependência do ambiente "Server with GUI" no Rocky 8.10 (ou através de um grupo de pacotes).
❌ Remover o Podman completamente (Primeiro, desinstale o Podman e tudo que possa causar conflito:)
sudo dnf remove -y podman buildah skopeo runc containers-common
🔄 Limpe cache de pacotes
sudo dnf clean all
🔧 Agora tente instalar o Docker com --nobest (Isso força a instalação de versões mais compatíveis, evitando o conflito com o containerd.io.)
sudo dnf install -y docker-ce docker-ce-cli containerd.io --nobest
▶️ Ativar e iniciar o Docker
sudo systemctl enable docker
sudo systemctl start docker
🔍 Verificar se o Docker está OK
docker version
docker run hello-world

# Atenção:
🧼 (Opcional, mas recomendado) Bloquear o Podman para não instalar de novo
sudo dnf mark exclude podman buildah skopeo


