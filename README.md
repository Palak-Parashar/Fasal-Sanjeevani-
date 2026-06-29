Fasal Sanjeevani - AI Powered Crop Disease Detection System

Project Overview :-
Fasal Sanjeevani is an AI-powered smart agriculture system that helps farmers detect crop diseases early using image-based deep learning. The system analyzes leaf images and provides instant predictions along with symptoms, treatment, and prevention suggestions.
It is designed to improve crop health monitoring and increase agricultural productivity using MobileNetV3 deep learning model.

Problem Statement:-
Farmers often struggle to identify crop diseases at an early stage, leading to reduced yield, financial loss, and improper treatment decisions.

Our Solution:-
We built an AI-based web platform that:
Detects crop diseases from leaf images
Provides real-time diagnosis
Suggests treatment and prevention methods
Offers additional farmer services like
1.weather updates
2.market prices
3.Government Schemes
4.Bilingual support
5.Voice assistant

System Architecture:-
User uploads or captures crop image (Frontend)
Image is sent to Flask backend API
MobileNetV3 model predicts disease

Backend returns:
Disease name
Symptoms
Treatment
Prevention
Result displayed on UI

Tech Stack:-
Frontend:
HTML
CSS
JavaScript

Backend:
Python (Flask)
AI/ML:
TensorFlow
Keras
MobileNetV3 (Fine-tuned model)

Features:-
Crop disease detection via image upload/camera
AI-based prediction system
Disease information (symptoms, treatment, prevention)
Weather updates
Market price tracking
PM-Kisan scheme information
Voice assistant (Kisan Vani)
History tracking of predictions
Multi-language support (English / Hindi)

AI Model Details:-
Model: MobileNetV3 (Fine-tuned)
Input Size: 128x128 images
Output: Multi-class crop disease classification
Framework: TensorFlow + Keras

Dataset Information:-
Dataset used: PlantVillage Dataset
Source: Kaggle
https://www.kaggle.com/datasets/emmarex/plantdisease
Validation dataset stored externally:\_
Google Drive :- https://drive.google.com/drive/folders/1iGizEhTTJVwDego2nXEMt-JfM2EvBXyU?usp=drive_link

We have not included dataset due to size constraints.

Model File:-
Trained model: finetuned.h5
Google Drive :-https://drive.google.com/file/d/1WpTFNlNZRHTEhZS5x7iQBNJP352WuQ5C/view?usp=drive_link

AI Tools:-
ChatGPT:- Debugging, API integration guidance, documentation used in Backend and README.
TensorFlow:- Model training and inference used in Machine Learning Model.
Keras:- Neural network development used for ML Pipeline.

How to Run the Project

1. Clone Repository
   git clone https://github.com/your-username/Fasal-Sanjeevani.git
   cd Fasal-Sanjeevani
2. Install Dependencies
   pip install -r backend/requirements.txt
3. Run Backend
   cd backend
   python app.py
   Backend runs on: http://127.0.0.1:5000
4. Run Frontend
   Open: frontend/index.html

API Endpoints:-
POST /predict → Predict crop disease
GET /history → Get prediction history
GET /weather → Weather data
GET /mandi-rate → Market prices
GET /scheme-check → Government schemes

Project Structure:-
Fasal-Sanjeevani/
│
├── frontend/
├── backend/
│ ├── app.py
│ ├── models/
│ ├──datasets/(excluded from PUSH)
│ ├── utils/
│ ├── routes/
│ └── fasal.db
│
└── README.md

Team Information:-
Team Name:Green VISIONARIES
Members: 1. Khushi Yadav (Team Leader) 2. Palak Parashar

Future Improvements:-
Improve disease classification accuracy
Add more crops and regional languages
Integrate real-time IoT sensors
Checks soil type and fertility

Conclusion:-
Fasal Sanjeevani is a complete AI-driven agricultural assistant that helps farmers make faster and smarter decisions for crop protection using deep learning and real-time insight.
