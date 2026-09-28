# Docker CI/CD Pipeline (`docker_3.3`)

This repository contains the containerized application and automated CI/CD pipeline using **GitHub Actions** to build and push multi-platform Docker images to **Docker Hub**.

---

## 🛠️ Tech Stack & Tools

* **CI/CD:** [GitHub Actions](https://github.com/JefferyChenjy/docker_3.3/actions)
* **Containerization:** Docker, Docker Buildx, QEMU
* **Registry:** Docker Hub

---

## 🚀 GitHub Actions CI/CD Pipeline

The workflow defined in `.github/workflows/ci.yml` triggers on every `push` to the `main` branch.

### Pipeline Steps
1. **Checkout Code:** Pulls the latest code from the repository.
2. **Docker Hub Authentication:** Logs into Docker Hub using secrets and variables.
3. **QEMU & Buildx Setup:** Configures QEMU for multi-architecture builds and sets up Docker Buildx.
4. **Build & Push:** Compiles the Docker image and pushes `latest` to Docker Hub.

---

## ⚙️ Configuration & Secrets Setup

To run this pipeline successfully in your own fork/repository, configure the following settings in **Settings > Secrets and variables > Actions**:

| Type | Name | Description |
| :--- | :--- | :--- |
| **Variables** | `DOCKERHUB_USERNAME` | Your Docker Hub username |
| **Secrets** | `DOCKERHUB_TOKEN` | Your Docker Hub Personal Access Token (PAT) with Read/Write access |

---

## 💻 Local Development

### Build the Image
```bash
docker build -t your-username/docker_3.3:latest .