# PLEASE DO NOT PUSH ANYTHING FROM /data

# Requirements

Can be found in `requirements.txt`

# working on changing to python3

# Running demo locally

1. Run server: `./new_ddc_server.sh` (it's inside `infer/`)

# Building dataset

1. ```cd ddc/data/raw/speirmix```
2. download and extract/unzip speirmix from https://zenius-i-vanisher.com/v5.2/viewsimfilecategory.php?categoryid=897
1. ```cd ../../../scripts```
1. Parse `.sm` files to JSON: `./smd_1_extract.sh speirmix`
1. Filter JSON files (removing mines, etc.): `./smd_2_filter.sh speirmix`
1. Split dataset 80/10/10: `./smd_3_dataset.sh speirmix`
1. Analyze dataset (e.g.): `./smd_4_analyze.sh speirmix`

# Running training

1. Navigate to `scripts/`
1. Extract features: `./sml_onset_0_extract.sh %dataset_name%`
1. Generate chart `.pkl` files (this may take a while): `./sml_onset_1_chart.sh %dataset_name%`
1. Train a step placement (onset detection) model on a dataset: `./sml_onset_2_train.sh %dataset_name%`
1. Train a step selection (symbolic) model on a dataset: `./sml_sym_2_train.sh %dataset_name%`
1. Train and evaluate a Laplace-smoothed 5gram model on a dataset: `./sml_sym_2_mark.sh %dataset_name% 5`
