echo "Setting up production environment..."
 
# Connecting to the production server and executing commands remotely
ssh -i ~/.ssh/id_rsa $PRODUCTION_SERVER_USER@$PRODUCTION_SERVER_IP << 'EOF'

echo "Connected to production server. Checking Docker installation..."

# Installing docker if it is not installed
if ! sudo docker --version; then
    echo "Docker not found. Installing Docker..."
    
    # Update package index
    sudo apt update
    
    # getting required packages for docker installation
    # Install prerequisites
    sudo apt install -y ca-certificates curl gnupg lsb-release
    
    # Add Docker's official GPG key
    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    
    # Add Docker repository
    echo \
      "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
      $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
    
    # Update package index with Docker repo
    sudo apt update
    
    # Install Docker packages
    # Docker Engine, CLI, containerd, buildx, and compose plugin
    sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
    
    # Add current user to docker group (optional, requires logout/login to take effect)
    sudo usermod -aG docker $USER
    
    # Start and enable Docker service
    sudo systemctl start docker
    sudo systemctl enable docker
    
    echo "Docker installation completed."
else
    echo "Docker is already installed on this server."
fi

# Install git
if ! sudo git --version; then
    echo "Installing git..."
    sudo apt install -y git
else
    echo "Git is already installed on this server."
fi


# Assert that docker and git are installed
if ! sudo docker --version; then
    echo "Docker is not installed on this server."
    exit 1
fi

if ! sudo git --version; then
    echo "Git is not installed on this server."
    exit 1
fi
 
 

EOF

echo "Production environment setup completed."