"""
Smart Traffic Management System
ML-based traffic congestion prediction and route optimization
"""

__version__ = "1.0.0"
__author__ = "Ranyaa-11"

from .config import TRAFFIC_GRAPH, TRAFFIC_CLASSES, TRAFFIC_COST
from .utils import normalize_traffic_label, load_image, get_random_image

__all__ = [
    'TRAFFIC_GRAPH',
    'TRAFFIC_CLASSES', 
    'TRAFFIC_COST',
    'normalize_traffic_label',
    'load_image',
    'get_random_image'
]
