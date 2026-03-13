# Project Dataset

This repository contains a simple image preprocessing pipeline that reads raw images from `dataset/`, applies resizing + normalization, performs basic augmentations (flip, rotate), and writes results into `processed_dataset/`.

---
---

## 🚀 Detailed Version Explanation

### 📌 Project Version
- **Version:** `1.0.0` (initial preprocessing pipeline)

### 🧰 Dependencies
This project is designed to run with:

- **Python:** 3.8+ (recommended)
- **Packages:**
  - `opencv-python` (for image I/O and transformations)
  - `numpy` (for numerical operations)

### 🛠️ How it works (step-by-step)
1. Reads every file under `dataset/`.
2. Skips corrupted/unreadable images.
3. Resizes each image to **224×224** pixels.
4. Normalizes pixel values to `[0, 1]`, then converts back for saving.
5. Saves the processed image to `processed_dataset/`.
6. Generates two augmentations per image:
   - Horizontal flip
   - Rotate 90° clockwise

---

## ▶️ Running the Preprocessing

```bash
python preprocess_dataset.py
```

### ✅ Expected output
- Processed images saved under `processed_dataset/` with suffixes `_flip` and `_rot` for augmentations.
