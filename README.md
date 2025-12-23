🌍 CO₂ Emission Predictor
📖 Project Overview

The CO₂ Emission Predictor is an end-to-end machine learning web application designed to estimate vehicle carbon dioxide emissions (g/km) based on vehicle specifications and fuel consumption data.

This project demonstrates how machine learning can be applied to environmental impact analysis by building a complete pipeline — from data preprocessing and model training to deployment through an interactive web interface.

Users can enter vehicle details such as engine size, transmission type, fuel type, and fuel consumption values to obtain an instant CO₂ emission prediction.
The application emphasizes accuracy, transparency, and clean ML engineering practices, deliberately avoiding misleading or artificial metrics.

📊 Dataset Information

The dataset used in this project consists of real-world vehicle specifications and emission measurements. It contains a combination of categorical and numerical features, making it suitable for a supervised regression problem.

🔹 Key Features

Vehicle manufacturer (Make)

Vehicle class (e.g., compact, SUV, pickup)

Engine size (liters)

Number of cylinders

Transmission type

Fuel type

Fuel consumption (city, highway, combined)

CO₂ emissions

🎯 Target Variable

CO₂ Emissions (grams per kilometer)

The dataset reflects realistic automotive emission data and is commonly used for fuel efficiency and environmental analysis.

🧠 Methodology

The project follows a supervised machine learning regression approach:

🔸 Data Preprocessing

Categorical features are encoded within a preprocessing pipeline

Numerical features are scaled to maintain consistency

Feature engineering includes converting combined fuel consumption from L/100 km to MPG

🔸 Model Training

A regression model is trained using scikit-learn

Preprocessing and model steps are encapsulated in a single Pipeline

Ensures identical transformations during training and prediction

🔸 Model Persistence

The trained pipeline is saved using joblib

The serialized model is reused during deployment without retraining

This pipeline-based approach improves reproducibility, reliability, and maintainability.

🖥️ Implementation

The application is implemented using Streamlit, providing a clean and interactive web interface.

🔹 Implementation Highlights

Structured input forms for vehicle and fuel data

Persistent user inputs using Streamlit session state (prevents reset on reruns)

Real-time CO₂ emission prediction on button click

Minimal dark-themed UI using embedded HTML & CSS

Direct integration with the trained ML pipeline for inference

The backend strictly returns predictions in g/km, maintaining scientific accuracy without adding fabricated environmental indicators.

📂 Repository Structure
co2-emission-predictor/
│
├── app.py
│   └── Streamlit web application
│       • Handles user input
│       • Loads trained ML pipeline
│       • Performs real-time predictions
│
├── co2_pipeline.pkl
│   └── Serialized scikit-learn pipeline
│       • Includes preprocessing and regression model
│
├── requirements.txt
│   └── List of required Python dependencies
│
├── README.md
│   └── Project documentation
│
└── .gitignore
    └── Excludes virtual environments and cache files


This structure is minimal, organized, and deployment-ready.

🛠️ Tech Stack
🔹 Programming Language

Python 3.9+

🔹 Machine Learning

scikit-learn – regression modeling, pipelines, preprocessing

joblib – model serialization

🔹 Data Processing

pandas – data handling and feature alignment

🔹 Web Application

Streamlit – interactive UI, session state, deployment

🔹 Frontend Styling

HTML & CSS – embedded styling for a custom dark UI

🔹 Deployment (Optional)

Streamlit Community Cloud – GitHub-based hosting

✅ Conclusion

The CO₂ Emission Predictor demonstrates a complete machine learning application lifecycle, emphasizing correct preprocessing, pipeline-based modeling, and clean deployment.

This project highlights how machine learning can be applied responsibly and transparently to real-world environmental problems while maintaining technical correctness and usability.
