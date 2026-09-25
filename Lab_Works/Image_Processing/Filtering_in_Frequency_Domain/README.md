<p>
  <img align="left" src="https://www.ec-nantes.fr/medias/photo/logocn-rvb_1648479844750-png?ID_FICHE=178994&amp;INLINE=FALSE" alt="Centrale Nantes" height="64">
</p>
<p align="right"><strong>MSc. CORO DASSIP</strong></p>
<br clear="both">

<table width="85%" align="center">
  <tr>
    <td align="center">
      <h1>Filtering in Frequency Domain</h1>
    </td>
  </tr>
</table>

Fourier-domain image-processing laboratory covering spatial frequency, 2-D FFT analysis, magnitude and phase, classical frequency filters, periodic-noise suppression, moiré removal, illumination correction, and validation.

The module is organized into four complementary notebooks:

- [Problem Statement](notebooks/filtering_in_frequency_domain_problem_statement.ipynb) — problem definition, inputs, expected outputs, and the 26 required tasks.
- [Requirements Gathering & Approach](notebooks/filtering_in_frequency_domain_requirements_gathering_and_approach.ipynb) — engineering requirements, selected methods, acceptance criteria, and implementation traceability.
- [Theory](notebooks/filtering_in_frequency_domain_theory.ipynb) — Fourier-domain formulation, transfer functions, spectral diagnostics, periodic interference analysis, and limitations.
- [Implementation](notebooks/filtering_in_frequency_domain.ipynb) — executable processing pipeline, quantitative results, figures, and validation checks.

## Outputs

Generated figures are stored in:

```text
outputs/figures/
```

Main outputs:

- `01_spatial_frequency.png`
- `02_fft_1d.png`
- `03_house_spectrum.png`
- `04_orientation_spectra.png`
- `05_dataset_spectra.png`
- `06_reconstruction.png`
- `07_phase_magnitude_swap.png`
- `08_phase_only_magnitude_only.png`
- `09_lpf_comparison.png`
- `10_butterworth_orders.png`
- `11_ringing.png`
- `12_high_pass.png`
- `13_high_boost.png`
- `14_band_filters.png`
- `15_periodic_noise_spectra.png`
- `16_notch_filter.png`
- `17_moire_removal.png`
- `18_shading_correction.png`
- `19_cutoff_sensitivity.png`

## Run

From the module directory:

```bash
cd ~/Master_SIP_EC-Nantes/Lab_Works/Image_Processing/Filtering_in_Frequency_Domain

source .venv/bin/activate
python -m pip install -r requirements.txt
code .
```

Open [filtering_in_frequency_domain.ipynb](notebooks/filtering_in_frequency_domain.ipynb), select the project `.venv` kernel, and run all cells from top to bottom.

A successful execution ends with:

```text
All frequency-domain validation checks passed.
```

## Project Structure

```text
Filtering_in_Frequency_Domain/
├── data/
├── notebooks/
│   ├── filtering_in_frequency_domain_problem_statement.ipynb
│   ├── filtering_in_frequency_domain_requirements_gathering_and_approach.ipynb
│   ├── filtering_in_frequency_domain_theory.ipynb
│   └── filtering_in_frequency_domain.ipynb
├── outputs/
│   └── figures/
├── requirements.txt
└── README.md
```

## Scope

Implemented:

- spatial-frequency interpretation;
- 1-D and 2-D Fourier transforms;
- FFT shifting and inverse reconstruction;
- magnitude and phase analysis;
- Ideal, Gaussian, and Butterworth low-pass filtering;
- ringing and Gibbs-phenomenon analysis;
- high-pass and high-boost filtering;
- convolution-theorem interpretation;
- band-pass and band-reject filtering;
- periodic-noise detection and notch filtering;
- moiré suppression;
- slowly varying illumination correction;
- cutoff-sensitivity analysis;
- quantitative and structural validation.

Not included:

- wavelet transforms;
- learned frequency representations;
- advanced inverse-problem restoration;
- segmentation.

## Participants

- **Denos Kume**

**MSc. CORO DASSIP — École Centrale de Nantes**
