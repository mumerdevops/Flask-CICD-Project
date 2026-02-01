# Flask CI/CD Pipeline on AWS
This project demonstrates a fully automated DevOps workflow using GitHub Actions, Docker, and AWS.

## 🚀 How it Works
1. Code is pushed to the `main` branch.
2. **GitHub Actions** triggers a build.
3. A **Docker Image** is created and pushed to **Docker Hub**.
4. GitHub Actions SSH-es into **AWS EC2** and pulls the latest image.
5. The container is restarted, making the changes live.

## 🛠 Tech Stack
* **App:** Python (Flask)
* **CI/CD:** GitHub Actions
* **Container:** Docker
* **Cloud:** AWS (EC2)
