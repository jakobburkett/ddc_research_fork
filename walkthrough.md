# Walkthrough the code as I run it

I'm gonna try my best to understand all of the code in here.
I'll go step by step through each file and write what I think is going on.

## Building Dataset
1. `./smd_1_extract.sh speirmix` 
    1. Runs `smd_0_push.sh` in current shell
       1. Runs `source var.sh` in current shell
          1. Defines the ddc directory and data directory
       2. change current dir to ../dataset (prior dir on stack)
    2. Runs `extract_json.py` with the data directory + the argument we have on `./smd_1_extract.sh`
       1. `extract_json.py` needs a directory of the packs and a directory for its json output as arguments
       2.  
