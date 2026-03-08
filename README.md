**Project Structure**

This project follows a modular structure to keep data handling, model development, and training logic separated. This improves maintainability, reproducibility, and experiment tracking.

```
Top Secret Research (Sshh)/
│
├── data/ # Datasets
│ ├── raw/ # Downloaded datasets, original, immutable data
│ └── processed/ # Cleaned or transformed data
│
│
├── notebooks/ # Jupyter notebooks for exploration and experimentation
│
├── src/ # Core project source code
│ ├── data/ # Dataset loading and preprocessing
│ ├── models/ # Model architectures
│ ├── training/ # Training loops and optimization logic
│ ├── evaluation/ # Metrics and evaluation scripts
│ └── utils/ # Shared utilities (logging, config, etc.)
│
├── configs/ # Configuration files for experiments
│
├── experiments/ # Experiment outputs (metrics, logs, plots)
│
├── checkpoints/ # Saved model weights
│
├── scripts/ # Helper scripts for running training/evaluation
│
├── tests/ # Unit tests
│
├── requirements.txt # Python (IF we are using Python) dependencies
└── README.md # Project documentation
```

(tests may or may not be implemented depending on how responsible we feel :))

** Virtual Environment Setup **
Create venv:

Run `python -m venv venv` in root directory.

To activate run: `venv\Scripts\activate` in terminal.
