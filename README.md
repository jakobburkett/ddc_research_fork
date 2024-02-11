# Requirements

Can be found in `requirements.txt`

* click==7.1.2
* essentia==2.1b6.dev234
* Flask==1.1.4
* funcsigs==1.0.2
* itsdangerous==1.1.0
* Jinja2==2.11.3
* MarkupSafe==1.1.1
* mock==3.0.5
* numpy==1.16.6
* protobuf==3.17.3
* PyYAML==5.4.1
* scipy==1.2.3
* six==1.16.0
* tensorflow==0.12.1
* Werkzeug==1.0.1

I could only find these packages through WSL so you'll probably need to use that or Linux

# Running demo locally

1. Run server: `./new_ddc_server.sh` (it's inside `infer/`)

# Building dataset

1. Make a directory named `data` under `~/ddc` (or change `scripts/var.sh` to point to a different directory)
1. Under `data`, make directories `raw`, `json_raw` and `json_filt`
1. Under `data/raw`, make directories for datasets `%dataset_name%`
1. Navigate to `scripts/`
1. Parse `.sm` files to JSON: `./smd_1_extract.sh %dataset_name%`
1. Filter JSON files (removing mines, etc.): `./smd_2_filter.sh %dataset_name%`
1. Split dataset 80/10/10: `./smd_3_dataset.sh %dataset_name%`
1. Analyze dataset (e.g.): `./smd_4_analyze.sh %dataset_name%`

# Running training

1. Navigate to `scripts/`
1. Extract features: `./sml_onset_0_extract.sh %dataset_name%`
1. Generate chart `.pkl` files (this may take a while): `./sml_onset_1_chart.sh %dataset_name%`
1. Train a step placement (onset detection) model on a dataset: `./sml_onset_2_train.sh %dataset_name%`
1. Train a step selection (symbolic) model on a dataset: `./sml_sym_2_train.sh %dataset_name%`
1. Train and evaluate a Laplace-smoothed 5gram model on a dataset: `./sml_sym_2_mark.sh %dataset_name% 5`