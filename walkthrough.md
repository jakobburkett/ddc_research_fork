# Walkthrough the code as I run it

I'm gonna try my best to understand all of the code in here.
I'll go step by step through each file and write what I think is going on.

## Building Dataset
1. `./smd_1_extract.sh speirmix` 
    1. Runs `smd_0_push.sh` in current shell
       1. Runs `source var.sh` in current shell
          1. Defines the ddc directory and data directory
       2. change current dir to ../dataset (prior dir on stack)i
    2. Runs `extract_json.py` with the data directory + the argument we have on `./smd_1_extract.sh`
       1. `extract_json.py` needs a directory of the packs and a directory for its json output as arguments
       2. `extract_json.py` parses the StepMania files and turns them into a structured JSON format
       3. `extract_json.py` allows for a user to change the ITG
      
2. `./smd_2_filter.sh speirmix`
    1. Runs `smd_0_push.sh` in current shell
    2. Runs `filter_json.py` with json[raw or filt]/speirmix directory + a bunch of arguments 
       1.`filter_json.py` using the arguments provided to exclude the stepmania files that don't meet the criteria

3. `./smd_3_dataset.sh speirmix`
    1. Runs `smd_0_push.sh` in current shell
    2. Runs `dataset_json.py` with json_filt/speirmix directory + 4 options
       1. `dataset_json.py` segments the StepMania chart/json's into distinct sets for training, validation, and testing.
    3. Removes json_filt/speirmix.txt
    4. Then cat's all txt files into a single txt file and another file specific to the category
       1. cats all train txt files into speirmix_train.txt
       2. cats all valid txt files into speirmix_valid.txt
       3. cats all test txt files into speirmix_test.txt
       4  cats all txt files into speirmix.txt
      
4. `smd_4_analyze.sh speirmix`
    1. Runs `smd_0_push.sh` in current shell
    1. Runs `analyze_json.py` with the data/json_filt/speirmix directory as an argument
       1. goes through the dataset and 'analyzes' by calculuating difficulties, averages, etc.

## Training Model
1. `./sml_onset_0_extract.sh`
    1. Runs `sml_0_push.sh` in current shell
    
