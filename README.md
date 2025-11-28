# ML CI/CD Pipeline using GitLab 

This project shows how to build a simple CI/CD pipeline for a Machine Learning model.  
The pipeline trains a model, runs tests, builds a Docker image, and can deploy the image.

---

##  What this project does

- Trains a Logistic Regression model on the Breast Cancer dataset  
- Runs unit tests to check accuracy  
- Builds a Docker image using a Dockerfile  
- Uses a CI/CD pipeline  
- Works on GitLab  
- Shows the basics of ML automation

---

##  Machine Learning details

**Dataset:** Breast Cancer dataset (from scikit-learn)  
**Model:** Logistic Regression  
**Metric:** Accuracy  
**Train script:** `train.py`  

The model prints accuracy when trained.

---


---

##  How to run this project locally

### 1 Install dependencies


* pip install -r requirements.txt


### 2 Run the training script

 * python3 train.py


### 3 Run tests
 
 *   pytest -q



---

##  CI/CD Pipeline (GitLab Version)

This project includes a `.gitlab-ci.yml` file with 3 stages:

### **1. Test stage**
- Installs packages  
- Runs pytest  
- Checks model accuracy  

### **2. Build stage**
- Builds a Docker image using the Dockerfile  

### **3. Deploy stage**  
- Pushes the Docker image to the GitLab Container Registry  

---

## Docker Usage

To build the Docker image manually:


* docker build -t ml-cicd-image .


 To run the image:

 * docker run ml-cicd-image

## Author

Yaswanth Sompalli

GitHub: https://github.com/Yaswanth114
