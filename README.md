# `dilipred`

DILI Predictor is an open-source app framework built specifically for human drug-induced liver injury (DILI)

DILI Predictor employs eleven proxy-DILI labels from in vitro (e.g., mitochondrial toxicity, bile salt export pump inhibition) and in vivo (e.g., preclinical rat hepatotoxicity studies) datasets along with pharmacokinetic parameters, structural fingerprints and physicochemical parameters as features.

Select from the sidebar to predict DILI for a single molecule! For bulk jobs, or local use: use code from Github page: https://github.com/srijitseal/DILI_Predictor

## Installation

### Clone this repo

```sh
git clone https://github.com/Manas02/dili-pip.git
cd dili-pip/
```

### Conda Environment [Optional | Recommeneded]

Install `dilipred` conda environment using the following command.

```sh
conda create --name dilipred
conda activate dilipred
```

### PIP Install package

```sh
pip install .
```

> Note: Use `pip install -e .` to make an editable installation.

## Usage

### Running `DILIPredictor` as CLI

#### Help

Simply run `dili` or `dili -h` or `dili --help` to get the helper.
![]()

#### Inference given SMILES strings
Output is stored in a directory with the name in the format `DILIPRedictor_dd-mm-yyyy-hh-mm-ss.csv`

### Running `DILIPredictor` as Library

```py
from dilipred import DILIPRedictor


if __name__ == '__main__':
    smiles = "CCCCCCCO"
    dp = DILIPRedictor(smiles)
    result = dp.predict()
```
