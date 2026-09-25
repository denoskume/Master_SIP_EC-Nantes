<p>
  <img align="left" src="https://www.ec-nantes.fr/medias/photo/logocn-rvb_1648479844750-png?ID_FICHE=178994&amp;INLINE=FALSE" alt="Centrale Nantes" height="64">
</p>
<p align="right"><strong>MSc. CORO DASSIP</strong></p>
<br clear="both">

<table width="85%" align="center">
  <tr>
    <td align="center">
      <h1>Deep Learning for MNIST Classification</h1>
    </td>
  </tr>
</table>

Handwritten-digit classification with a one-hidden-layer MLP in PyTorch, comparing hidden sizes of 128, 256, and 512 neurons on MNIST.

The module is organized into four complementary notebooks:

- [Problem Statement](notebooks/problem_statement.ipynb) — problem definition, fixed experiment settings, expected outputs, and the 13 required tasks.
- [Requirements Gathering & Approach](notebooks/requirements.ipynb) — engineering requirements, method choices, acceptance criteria, and task-to-code traceability.
- [Theory](notebooks/theory.ipynb) — mathematical formulation of the MLP, optimization objective, controlled model-capacity comparison, and confidence analysis.
- [Implementation](notebooks/main.ipynb) — concise executable workflow with code, generated outputs, metrics, diagnostics, and validation only.

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
cd ~/msc-coro-dassip-portfolio/labs/computer-vision/deep-learning

source .venv/bin/activate
python -m pip install -r requirements.txt
code .
```

Open [main.ipynb](notebooks/main.ipynb), select the project `.venv` kernel, and run all cells from top to bottom.

A successful execution ends with:

```text
All Deep Learning validation checks passed.
```

## Project Structure

```text
deep-learning/
├── data/
├── notebooks/
│   ├── problem_statement.ipynb
│   ├── requirements.ipynb
│   ├── theory.ipynb
│   └── main.ipynb
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
