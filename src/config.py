"""
Configuration settings for the Smart Traffic Management System
"""

import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent.parent

# Data paths
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

# Model paths
MODELS_DIR = PROJECT_ROOT / "models"
XGB_MODEL_PATH = MODELS_DIR / "traffic_xgb_model.pkl"
LABEL_ENCODER_PATH = MODELS_DIR / "label_encoder.pkl"
SCALER_PATH = MODELS_DIR / "scaler.pkl"

# Image settings
IMAGE_SIZE = (224, 224)
IMAGE_EXTENSIONS = ('.jpg', '.jpeg', '.png')

# Model configuration
MODEL_CONFIG = {
    'objective': 'multi:softmax',
    'num_class': 3,
    'n_estimators': 700,
    'max_depth': 8,
    'learning_rate': 0.03,
    'subsample': 0.9,
    'colsample_bytree': 0.9,
    'min_child_weight': 1,
    'gamma': 0.15,
    'reg_alpha': 0.1,
    'reg_lambda': 1.0,
    'random_state': 42,
    'tree_method': 'hist'
}

# Traffic classes
TRAFFIC_CLASSES = ['low', 'moderate', 'high']
TRAFFIC_COST = {
    'low': 1,
    'moderate': 5,
    'high': 10
}

# Bengaluru Traffic Network Graph
TRAFFIC_GRAPH = {
    "Bengaluru": ["MG Road", "Richmond Town", "Domlur"],
    "MG Road": ["Bengaluru", "Brigade Road", "Ulsoor"],
    "Richmond Town": ["Bengaluru", "Langford Road", "Adugodi"],
    "Domlur": ["Bengaluru", "Indiranagar", "Ejipura"],
    "Brigade Road": ["MG Road", "Richmond Town", "Adugodi"],
    "Ulsoor": ["MG Road", "Indiranagar", "CMH Road"],
    "Langford Road": ["Richmond Town", "Adugodi", "Shantinagar"],
    "Adugodi": ["Richmond Town", "Brigade Road", "Koramangala"],
    "Indiranagar": ["Domlur", "Ulsoor", "CMH Road"],
    "Ejipura": ["Domlur", "Koramangala", "Madiwala"],
    "CMH Road": ["Ulsoor", "Indiranagar", "100 Feet Road"],
    "100 Feet Road": ["CMH Road"],
    "Madiwala": ["Ejipura", "Koramangala", "Silk Board"],
    "Shantinagar": ["Langford Road", "Richmond Town", "Adugodi"],
    "Koramangala": ["Adugodi", "Ejipura", "Madiwala"]
}
