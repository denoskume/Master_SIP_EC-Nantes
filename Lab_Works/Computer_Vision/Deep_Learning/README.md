# Deep Learning for MNIST Classification

Handwritten-digit classification with a one-hidden-layer MLP in PyTorch, comparing hidden sizes of 128, 256, and 512 neurons on MNIST.

The module is organized into four complementary notebooks:

- [Problem Statement](notebooks/deep_learning_problem_statement.ipynb) — problem definition, fixed experiment settings, expected outputs, and the 13 required tasks.
- [Requirements Gathering & Approach](notebooks/deep_learning_requirements_gathering_and_approach.ipynb) — engineering requirements, method choices, acceptance criteria, and task-to-code traceability.
- [Theory](notebooks/deep_learning_theory.ipynb) — complete conceptual and mathematical explanation from data representation to optimization and confidence analysis.
- [Implementation](notebooks/deep_learning.ipynb) — executable source of truth; every required task is immediately followed by its corresponding code.

## Outputs

Generated figures are stored in:

```text
outputs/figures/
```

Main outputs:

- `mnist_sample_batch.png`
- `training_loss_comparison.png`
- `mnist_predictions_128.png`
- `mnist_predictions_256.png`
- `mnist_predictions_512.png`
- `pr_accuracy_curve.png`

## Run

From the module directory:

```bash
cd ~/Master_SIP_EC-Nantes/Lab_Works/Computer_Vision/Deep_Learning

source .venv/bin/activate
python -m pip install -r requirements.txt
code .
```

Open [deep_learning.ipynb](notebooks/deep_learning.ipynb), select the project `.venv` kernel, and run all cells from top to bottom.

A successful execution ends with:

```text
All Deep Learning validation checks passed.
```

## Project Structure

```text
Deep_Learning/
├── data/
├── notebooks/
│   ├── deep_learning_problem_statement.ipynb
│   ├── deep_learning_requirements_gathering_and_approach.ipynb
│   ├── deep_learning_theory.ipynb
│   └── deep_learning.ipynb
├── outputs/
│   └── figures/
├── requirements.txt
└── README.md
```

## Scope

Implemented:

- local MNIST loading and normalization;
- one-hidden-layer MLP;
- Batch Normalization and ReLU;
- Cross-Entropy training with Adam;
- hidden-width comparison;
- prediction/confidence analysis;
- numerical and visual validation.

Not included:

- CNN architectures;
- data augmentation;
- separate validation split;
- hyperparameter search;
- probability calibration;
- uncertainty estimation.

## Participants

- **Denos Kume**
- **Oluwole SHOKUNBI**

**MSc. CORO DASSIP — École Centrale de Nantes**
