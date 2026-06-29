# 🚦 Smart Traffic Management System using Machine Learning

An intelligent ML-powered traffic management system that uses **computer vision** and **machine learning** to analyze traffic images, predict congestion levels, and find optimal routes with minimal traffic using Dijkstra's algorithm.

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Latest-red)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange)
![XGBoost](https://img.shields.io/badge/XGBoost-Latest-yellow)
![License](https://img.shields.io/badge/License-MIT-green)
![Stars](https://img.shields.io/github/stars/Ranyaa-11/Smart-traffic-management-?style=social)

## 🎯 Problem Statement

Urban areas face rapid growth in vehicle numbers, causing:
- ❌ Frequent traffic congestion and longer travel times
- ❌ Increased fuel consumption and pollution
- ❌ Inefficient traditional fixed traffic signal systems
- ❌ Lack of real-time adaptive traffic management

**Our Solution**: An AI-driven system that analyzes traffic camera images, classifies congestion levels, and intelligently routes vehicles through the least congested paths.

## ✨ Key Features

- 🎥 **Traffic Image Classification** - Detects congestion levels (Low/Moderate/High) from traffic camera feeds
- 🗺️ **Smart Route Finding** - Dijkstra's algorithm finds the optimal least-congested path
- 📊 **Interactive Dashboard** - Streamlit-based UI with real-time visualization
- 🚀 **Deep Learning Feature Extraction** - MobileNetV2 for efficient image analysis
- 🤖 **ML-Powered Predictions** - XGBoost classifier for accurate congestion detection
- 📈 **Data Augmentation** - 6x data enhancement for robust model training

## 🏗️ System Architecture

```
┌─────────────────────┐
│  Traffic Images     │
│  (CCTV Cameras)     │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  MobileNetV2        │
│  Feature Extraction │
│  (1280-D vectors)   │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Feature Scaling    │
│  & Preprocessing    │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  XGBoost Classifier │
│  Traffic Prediction │
│  (Low/Mod/High)     │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Dijkstra's Route   │
│  Optimization       │
│  Algorithm          │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Streamlit Dashboard│
│  Route + Insights   │
└─────────────────────┘
```

## 🛠️ Tech Stack

- **Language**: Python 3.9+
- **Deep Learning**: TensorFlow/Keras (MobileNetV2)
- **ML Classification**: XGBoost
- **Image Processing**: OpenCV
- **Data Processing**: NumPy, Pandas, Scikit-learn
- **Dashboard**: Streamlit
- **Visualization**: Matplotlib, Seaborn

## 📁 Project Structure

```
smart-traffic-management/
├── README.md                      # Project documentation
├── ARCHITECTURE.md                # System design details
├── PROBLEM_STATEMENT.md           # Problem & solution overview
├── requirements.txt               # Dependencies
│
├── src/
│   ├── __init__.py
│   ├── config.py                  # Configuration settings
│   └── utils.py                   # Helper functions
│
├── data/
│   ├── README.md                  # Data documentation
│   ├── raw/                       # Original traffic images
│   └── processed/                 # Preprocessed features
│
├── models/
│   ├── traffic_xgb_model.pkl      # Trained XGBoost model
│   ├── label_encoder.pkl          # Label encoder
│   └── scaler.pkl                 # Feature scaler
│
├── streamlit_app.py               # Main dashboard
├── train.py                       # Training script
├── predict.py                     # Prediction script
├── .gitignore
└── LICENSE
```

## 🚀 Quick Start

### Prerequisites
- Python 3.9 or higher
- pip or conda

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Ranyaa-11/Smart-traffic-management-.git
cd Smart-traffic-management-
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

### Running the Application

**Launch the Streamlit Dashboard**
```bash
streamlit run streamlit_app.py
```

## 📊 Model Details

- **Feature Extraction**: MobileNetV2 (1280-D vectors)
- **Classification**: XGBoost (700 trees, max_depth=8)
- **Accuracy**: 88-91%
- **Classes**: Low, Moderate, High
- **Data Augmentation**: 6x expansion per image

## 🔮 Future Enhancements

- [ ] Real-time sensor integration
- [ ] LSTM for time-series forecasting
- [ ] REST API for external apps
- [ ] Mobile app development
- [ ] Multi-city support

## 📝 License

MIT License - see [LICENSE](LICENSE) file

## 👤 Author

**Ranya B R**
- 📧 Email: ranya.2ram@gmail.com
- 🐙 GitHub: [@Ranyaa-11](https://github.com/Ranyaa-11)

## 🙏 Acknowledgments

- TensorFlow & Keras for MobileNetV2
- XGBoost for gradient boosting
- Streamlit for interactive dashboards

---

**⭐ If this project helps you, please give it a star!**

**Made with ❤️ for smarter cities**
