````markdown
# Deep Learning for MNIST Classification

Handwritten-digit classification using a one-hidden-layer multilayer perceptron (MLP) implemented in PyTorch.

This laboratory trains and evaluates fully connected neural networks on the Modified National Institute of Standards and Technology (MNIST) dataset, compares several hidden-layer sizes, and analyzes model predictions through loss, accuracy, confidence, precision, and recall.

## Problem

The objective is to classify grayscale handwritten-digit images into one of ten classes, from 0 to 9.

Each MNIST image has a resolution of 28 × 28 pixels. The image is normalized, flattened into a 784-dimensional vector, and processed by a fully connected neural network.

Three hidden-layer configurations are evaluated:

```text
784 → 128 → 10
784 → 256 → 10
784 → 512 → 10
````

## Objectives

The laboratory implements the complete classification pipeline:

1. Load the MNIST training and testing datasets.
2. Normalize image pixel values.
3. Construct mini-batches using PyTorch.
4. Implement a one-hidden-layer MLP classifier.
5. Apply Batch Normalization and ReLU activation.
6. Train the network using Cross-Entropy Loss.
7. Optimize model parameters using Adam.
8. Compare hidden-layer sizes of 128, 256, and 512 neurons.
9. Evaluate classification performance on the test set.
10. Visualize predictions and confidence scores.
11. Analyze precision, recall, and accuracy using confidence thresholds.

## Method

The classification pipeline is:

```text
MNIST image
    ↓
Normalize pixel values
    ↓
Flatten 28 × 28 image
    ↓
784-dimensional input
    ↓
Fully connected layer
    ↓
Batch Normalization
    ↓
ReLU
    ↓
Fully connected output layer
    ↓
10 logits
    ↓
Softmax
    ↓
Predicted digit
```

During training, the output logits are compared with the ground-truth labels using Cross-Entropy Loss.

The Adam optimizer updates the model parameters through backpropagation.

After training, Softmax converts the logits into class probabilities. The class with the highest probability is selected as the predicted digit.

## Experimental Configuration

| Parameter          |         Value |
| ------------------ | ------------: |
| Dataset            |         MNIST |
| Training images    |        60,000 |
| Testing images     |        10,000 |
| Image size         |       28 × 28 |
| Input dimension    |           784 |
| Output classes     |            10 |
| Hidden-layer sizes | 128, 256, 512 |
| Epochs             |            10 |
| Batch size         |           512 |
| Optimizer          |          Adam |
| Learning rate      |          1e-3 |
| Weight decay       |          1e-3 |
| Loss function      | Cross Entropy |
| Activation         |          ReLU |
| Normalization      |   BatchNorm1d |

## Project Structure

```text
Deep_Learning/
├── .venv/
├── data/
│   ├── train-images-idx3-ubyte
│   ├── train-labels-idx1-ubyte
│   ├── t10k-images-idx3-ubyte
│   └── t10k-labels-idx1-ubyte
├── notebooks/
│   └── Deep_Learning.ipynb
├── outputs/
│   └── figures/
│       ├── mnist_sample_batch.png
│       ├── training_loss_comparison.png
│       ├── mnist_predictions_128.png
│       ├── mnist_predictions_256.png
│       ├── mnist_predictions_512.png
│       └── pr_accuracy_curve.png
├── requirements.txt
└── README.md
```

The `.venv/` directory is local and is not tracked by Git.

## Notebook Structure

```text
0. Setup
1. Data and Output Paths
2. MNIST Dataset and Mini-Batch Construction
3. Load Training and Testing Data
4. Visualize MNIST Samples
5. Define the MLP Classifier
6. Verify the Model Architecture
7. Training and Evaluation Utilities
8. Train the Three MLP Configurations
9. Compare Training Loss
10. Summarize Model Performance
11. Prediction Visualization
12. Confidence-Threshold Precision, Recall and Accuracy
13. Precision-Recall Analysis of the Best Model

Discussion
Conclusion
```

## Environment

The laboratory was developed using:

```text
Python 3.12.3
```

Direct Python dependencies are defined in `requirements.txt`:

```text
numpy
matplotlib
torch
python-mnist
tqdm
ipykernel
```

## Installation

From the `Deep_Learning/` directory:

```bash
python3 -m venv .venv
```

Activate the environment:

```bash
source .venv/bin/activate
```

Install the required dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Register the environment as a Jupyter kernel:

```bash
python -m ipykernel install \
  --user \
  --name deep-learning \
  --display-name "Deep Learning (.venv)"
```

## Running the Notebook

Open:

```text
notebooks/Deep_Learning.ipynb
```

Select the kernel:

```text
Deep Learning (.venv)
```

Then run all cells from top to bottom.

The notebook expects the MNIST dataset files in:

```text
data/
```

Generated figures are saved automatically in:

```text
outputs/figures/
```

## Outputs

### MNIST Samples

A subset of handwritten digits is displayed together with the corresponding labels.

Output:

```text
outputs/figures/mnist_sample_batch.png
```

### Training Loss Comparison

Training loss is compared across the three hidden-layer configurations.

Output:

```text
outputs/figures/training_loss_comparison.png
```

### Prediction Results

Predicted classes and confidence distributions are visualized for each evaluated MLP architecture.

Outputs:

```text
outputs/figures/mnist_predictions_128.png
outputs/figures/mnist_predictions_256.png
outputs/figures/mnist_predictions_512.png
```

### Precision-Recall and Accuracy Analysis

Confidence-threshold evaluation is used to examine precision, recall, and accepted correct predictions.

Output:

```text
outputs/figures/pr_accuracy_curve.png
```

## Evaluation

The trained models are evaluated using:

* final training loss;
* test classification accuracy;
* predicted class confidence;
* qualitative prediction examples;
* confidence-threshold precision;
* confidence-threshold recall;
* accuracy-recall behavior.

The submitted laboratory experiment reported the following final training losses:

| Hidden neurons | Final training loss |
| -------------: | ------------------: |
|            128 |              0.0753 |
|            256 |              0.0344 |
|            512 |              0.0394 |

These values correspond to the submitted experiment. Results from a new execution may vary slightly because of model initialization, batch ordering, and numerical differences.

## Limitations

The implemented model contains only one hidden fully connected layer.

Unlike a convolutional neural network, the MLP does not explicitly exploit the spatial organization of image pixels.

The laboratory therefore focuses on the fundamental components of neural-network training:

* forward propagation;
* loss computation;
* backpropagation;
* parameter optimization;
* model evaluation.

## Technologies

* Python
* PyTorch
* NumPy
* Matplotlib
* Jupyter
* MNIST
* Multilayer Perceptron
* Batch Normalization
* ReLU
* Softmax
* Cross-Entropy Loss
* Adam

## Participants

* **Denos Kume**
* **Oluwole SHOKUNBI**

Master SIP
École Centrale de Nantes

```
```