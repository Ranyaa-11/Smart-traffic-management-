# System Architecture

## 🏗️ High-Level Architecture

```
┌──────────────────────────────────────────────────────────────┐
│                   TRAFFIC MANAGEMENT SYSTEM                  │
└──────────────────────────────────────────────────────────────┘
                              │
                              ▼
         ┌────────────────────────────────────┐
         │   DATA COLLECTION LAYER            │
         │ (CCTV Cameras / Traffic Sensors)   │
         └────────────────────────────────────┘
                              │
                              ▼
         ┌────────────────────────────────────┐
         │   PREPROCESSING LAYER              │
         │ • Image Loading (224×224)          │
         │ • Normalization                    │
         │ • Data Augmentation (6x)           │
         └────────────────────────────────────┘
                              │
                              ▼
         ┌────────────────────────────────────┐
         │   FEATURE EXTRACTION LAYER         │
         │ (MobileNetV2)                      │
         │ Input: 224×224 RGB Image           │
         │ Output: 1280-D Feature Vector      │
         └────────────────────────────────────┘
                              │
                              ▼
         ┌────────────────────────────────────┐
         │   FEATURE PROCESSING LAYER         │
         │ • Scaling (StandardScaler)         │
         │ • Normalization                    │
         │ • Dimensionality (1280-D)          │
         └────────────────────────────────────┘
                              │
                              ▼
         ┌────────────────────────────────────┐
         │   ML CLASSIFICATION LAYER          │
         │ (XGBoost Classifier)               │
         │ Input: 1280-D scaled features      │
         │ Output: Class (0,1,2)              │
         └────────────────────────────────────┘
                              │
                              ▼
         ┌────────────────────────────────────┐
         │   LABEL DECODING LAYER             │
         │ LabelEncoder Inverse Transform     │
         │ Output: "low" / "moderate" / "high"│
         └────────────────────────────────────┘
                              │
                              ▼
         ┌────────────────────────────────────┐
         │   ROUTING LAYER                    │
         │ (Dijkstra's Algorithm)             │
         │ • Compute node costs               │
         │ • Find shortest path               │
         │ Output: Optimal route list         │
         └────────────────────────────────────┘
                              │
                              ▼
         ┌────────────────────────────────────┐
         │   PRESENTATION LAYER               │
         │ (Streamlit Dashboard)              │
         │ • Route visualization              │
         │ • Traffic status display           │
         │ • Insights & analytics             │
         └────────────────────────────────────┘
```

## 📂 Component Description

### 1. Data Collection Layer
**Purpose**: Capture real-time traffic images

```python
# Pseudo-code
for each_node in network:
    image = capture_from_cctv(node)
    save_image_buffer(image)
```

**Inputs**: CCTV camera streams / saved image files  
**Outputs**: 224×224 RGB images  
**Technologies**: OpenCV

---

### 2. Preprocessing Layer
**Purpose**: Prepare images for model input

```python
def preprocess_image(img_path):
    img = cv2.imread(img_path)              # Load
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert BGR→RGB
    img = cv2.resize(img, (224, 224))      # Resize
    return img
```

**Augmentation Techniques** (applied during training):
- Random brightness (factor: 0.6-1.4)
- Gaussian noise (σ=10)
- Cutout masking (20-50px patches)
- Gaussian blur (5×5 kernel)
- Sharpening filter
- Horizontal flip

**Result**: 7x dataset (1 original + 6 augmented)

---

### 3. Feature Extraction Layer
**Purpose**: Convert images to numerical features

```
MobileNetV2 Pre-trained Model
├── Input: (224, 224, 3) RGB image
├── Architecture: 53 layers (pre-trained on ImageNet)
├── Pooling: Global average pooling
└── Output: (1, 1280) feature vector
```

**Why MobileNetV2?**
- ✅ Lightweight (efficient for real-time)
- ✅ Pre-trained on ImageNet (transfer learning)
- ✅ 1280 high-quality features
- ✅ Fast inference (~100-200ms)
- ✅ Proven accuracy for image classification

---

### 4. Feature Processing Layer
**Purpose**: Scale and normalize features

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)  # Mean=0, Std=1
```

**Why Scaling?**
- XGBoost performs better with normalized inputs
- Prevents large-scale features from dominating
- Improves model convergence during training

---

### 5. ML Classification Layer
**Purpose**: Predict traffic congestion level

```python
from xgboost import XGBClassifier

xgb = XGBClassifier(
    objective='multi:softmax',           # Multi-class classification
    num_class=3,                         # 3 classes
    n_estimators=700,                    # 700 trees
    max_depth=8,                         # Tree depth
    learning_rate=0.03,                  # Shrinkage
    subsample=0.9,                       # 90% row sampling
    colsample_bytree=0.9,                # 90% column sampling
    gamma=0.15,                          # Min loss reduction
    reg_alpha=0.1,                       # L1 regularization
    reg_lambda=1.0,                      # L2 regularization
    random_state=42
)

# Prediction
pred_class = xgb.predict(features_scaled)  # Returns: 0, 1, or 2
```

**Why XGBoost?**
- ✅ Superior accuracy for tabular data
- ✅ Handles non-linear relationships
- ✅ Robust to outliers
- ✅ Fast training & inference
- ✅ Built-in regularization

---

### 6. Label Decoding Layer
**Purpose**: Convert predicted class to readable label

```python
from sklearn.preprocessing import LabelEncoder

le = LabelEncoder()
le.fit(['low', 'moderate', 'high'])

# During prediction
predicted_class = 2  # (0,1,2)
traffic_label = le.inverse_transform([predicted_class])  # 'high'
```

---

### 7. Routing Layer (Dijkstra's Algorithm)
**Purpose**: Find optimal route considering traffic

```python
import heapq

def dijkstra(source, destination, graph, node_traffic):
    """Finds shortest path where cost = traffic congestion"""
    pq = [(0, source, [source])]
    visited = set()

    while pq:
        cost, node, path = heapq.heappop(pq)
        if node in visited:
            continue
        visited.add(node)

        if node == destination:
            return path

        for neighbor in graph[node]:
            weight = traffic_cost[node_traffic[neighbor]]
            new_cost = cost + weight
            heapq.heappush(pq, (new_cost, neighbor, path + [neighbor]))

    return None
```

**Complexity**: O((V + E) log V) - For 15 nodes: ~100ms

---

### 8. Presentation Layer (Streamlit)
**Purpose**: Interactive UI for users

```python
import streamlit as st

st.title("🚦 Smart Traffic-Based Route Finder")

source = st.selectbox("Select Source", nodes)
destination = st.selectbox("Select Destination", nodes)

if st.button("Find Best Route"):
    # Process and display
```

---

## 🔄 Data Flow Example

### User Request: Bengaluru → Koramangala

```
1. User Input → Source: Bengaluru, Destination: Koramangala
        ↓
2. System assigns random traffic images to each node
        ↓
3. For each node:
   - Load image (224×224)
   - Extract MobileNetV2 features (1280-D)
   - Scale features (StandardScaler)
   - Predict class with XGBoost (0, 1, or 2)
   - Decode label (LabelEncoder) → 'low'/'moderate'/'high'
        ↓
4. Result: {node: traffic_level} for all 15 nodes
        ↓
5. Run Dijkstra's algorithm:
   - Start from Bengaluru
   - Consider traffic costs (low=1, moderate=5, high=10)
   - Find optimal path
        ↓
6. Output: Optimal route + traffic visualization
```

---

## 📊 Performance Characteristics

### Latency Breakdown
```
Per-Node Processing    : 250-350ms
Per-Image              : ~500ms
Total for 15 nodes     : ~4-6 seconds
Dijkstra Computation   : <100ms
End-to-End Total       : ~4-6 seconds
```

### Memory Usage
```
MobileNetV2 Model      : ~100MB
XGBoost Model          : ~5MB
Feature Vectors (15)   : ~20KB
Total                  : ~105MB
```

---

## 🎯 Summary

This architecture combines:
- **Computer Vision** (MobileNetV2)
- **Machine Learning** (XGBoost)
- **Graph Algorithms** (Dijkstra)
- **Web Framework** (Streamlit)

To create an end-to-end intelligent traffic management system.
