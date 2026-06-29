"""
Utility functions for the Smart Traffic Management System
"""

import os
import random
import logging
from typing import List, Tuple, Optional
import cv2
import numpy as np

logger = logging.getLogger(__name__)


def normalize_traffic_label(label: str) -> str:
    """
    Convert any traffic label to standard format (low/moderate/high)
    """
    label = str(label).lower()
    
    if "low" in label or "few" in label:
        return "low"
    elif "moderate" in label or "medium" in label:
        return "moderate"
    elif "high" in label or "heavy" in label:
        return "high"
    else:
        return "moderate"


def load_image(image_path: str, target_size: Tuple[int, int] = (224, 224)) -> Optional[np.ndarray]:
    """
    Load and preprocess an image
    """
    try:
        img = cv2.imread(image_path)
        if img is None:
            logger.error(f"Unable to read image: {image_path}")
            return None
        
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, target_size)
        return img
    except Exception as e:
        logger.error(f"Error loading image: {str(e)}")
        return None


def get_random_image(root_dir: str, extensions: Tuple = ('.jpg', '.jpeg', '.png')) -> Optional[str]:
    """
    Select a random image from a directory tree
    """
    try:
        folders = [os.path.join(root_dir, d) for d in os.listdir(root_dir)
                  if os.path.isdir(os.path.join(root_dir, d))]
        
        if not folders:
            return None
        
        folder = random.choice(folders)
        images = [f for f in os.listdir(folder) if f.lower().endswith(extensions)]
        
        if not images:
            return None
        
        return os.path.join(folder, random.choice(images))
    except Exception as e:
        logger.error(f"Error selecting image: {str(e)}")
        return None
