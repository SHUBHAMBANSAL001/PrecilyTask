# Tesseract service

Given : You are given an application with APIs which extracts text from images. 

Task : You have to build a lightweight docker container which will map port 4000 of your app to your machine. 
You also have to create a kubernetes manifest file which can deploy replica sets in a cluster. 
Create a requirements.txt file for this repo. 
Create a contract of rest api read_ocr.
The solution will be evaluated by running the manifest file on minikube. 

Note:
Please download this repo and email a zip file over email. 

Extra marks will be given for : 
- setting up CI/CD files for the same app. 
- adding logging functionality in repo.

Dependencies :

opencv-python==4.4.0.46

pytesseract==0.3.7
