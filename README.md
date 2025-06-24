# Data Insights Azure Co-pilot Connector

## Setup Instructions

Follow these steps to set up and run the Azure Co-pilot Connector:

### 1. Clone the Repository

```bash
git clone <this-repo-name>
cd insights-copilot-connector
```

### 1. Connect to VPN
Ensure you are connected to the AWS VPN Client.

### 2. Obtain the Environment File
Contact the project maintainer (me) to obtain the required `.env` file. This file contains sensitive configuration and should not be shared publicly.

### 3. Build and Run the Docker Image

Make sure the `.env` file is located in the root directory of the project.

```bash
# Build the Docker image
docker build -t insights-copilot-connector .

# Run the Docker container with the environment variables
docker run --env-file .env -p 8090:8090 insights-copilot-connector
```