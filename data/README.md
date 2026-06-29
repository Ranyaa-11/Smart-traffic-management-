# Data Directory

This directory contains datasets for the Smart Traffic Management System.

## Directory Structure

```
data/
├── raw/                   # Original traffic images
│   ├── low/              # Low traffic images
│   ├── moderate/         # Moderate traffic images
│   └── high/             # High traffic images
└── processed/            # Preprocessed features
```

## Dataset Format

- **Format**: JPEG, PNG
- **Size**: 224×224 pixels
- **Classes**: low, moderate, high
- **Recommended**: 300+ images per class

## Folder Structure

```
data/raw/
├── low/
│   ├── image_001.jpg
│   └── ...
├── moderate/
│   ├── image_001.jpg
│   └── ...
└── high/
    ├── image_001.jpg
    └── ...
```

## Data Augmentation

- Random brightness (0.6-1.4)
- Gaussian noise (σ=10)
- Cutout masking (20-50px)
- Gaussian blur (5×5)
- Sharpening filter
- Horizontal flip

**Result**: 7x dataset expansion (1 original + 6 augmented)
