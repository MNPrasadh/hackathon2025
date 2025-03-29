# AI Powered to detect and prevent CyberSecurity Threats

## Overview
This project integrates **AI-powered cybersecurity and image security** techniques to detect **network intrusions and malicious hidden data in images**. The system is built using **CNN for steganography detection** and **LSTM-RNN for intrusion detection** using the **CIC-IDS dataset**. If an attack is detected, the system will **plot the attacker's location**.

## Features
- **OCR-Based Link Detection**: Extracts text from images to identify potential malicious links.
- **Steganography Detection**: Uses **CNN architecture** to determine if an image contains hidden data.
- **Intrusion Detection System (IDS)**: Uses **LSTM-RNN** to analyze network traffic and detect attacks from the **CIC-IDS2017 dataset**.
- **Attack Visualization**: Plots attacker locations on a real-time map using IP geolocation.
- **Streamlit Web UI**: A simple and interactive user interface for image and network security analysis.

## Technologies Used
- **Deep Learning:**
  - **Convolutional Neural Networks (CNN)** for steganography detection.
  - **Long Short-Term Memory (LSTM) RNN** for network intrusion detection.
- **Machine Learning:**
  - Data preprocessing and feature extraction for IDS.
- **Python Libraries:**
  - `TensorFlow`for Deep Learning Models
  - `OpenCV` for image processing
  - `Tesseract OCR` for text extraction
  - `Scikit-learn` for ML utilities
  - `Folium` for plotting attack locations
  - `Streamlit` for the UI
- **Datasets:**
  - **CIC-IDS2017** for intrusion detection
  - **Steganographic Image Dataset** for CNN training




### 1. Download Datasets
- **CIC-IDS2017 Dataset**: (https://www.unb.ca/cic/datasets/ids-2017.html)
- **Steganographic Image Dataset**: Kaggle Dataset

### 2. Run the Application
```bash
python app.py
```

## Usage
1. **Upload an image** to check for hidden malicious data.
2. **Upload network logs** to detect intrusion attempts.
3. **View attack details** and their location on the map.

## Project Architecture

📂 static/uploads/                 # Folder for uploaded images
📂 templates/                       # HTML templates for the web interface
📄 Attacker_Location (1).ipynb      # Jupyter Notebook for plotting attacker locations
📄 Intrusion_Detection_System.ipynb # IDS model using LSTM-RNN
📄 README.md                        # Project documentation
📄 app.py                            #OCR
📄 attacker_location.html            # Webpage for displaying attacker locations
📄 steganography_cnn_model.ipynb     # CNN model for steganography detection


## Future Enhancements
- **Real-time network traffic monitoring**
- **Integration with cloud-based security platforms**
- **Blockchain-based image verification**
