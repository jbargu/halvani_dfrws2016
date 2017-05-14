# Authorship Verification

This repository contains implementation of a DFRWS 2016 Europe article "Authorship verification for different languages, genres and topics". The describing paper is available as a [PDF](http://www.sciencedirect.com/science/article/pii/S1742287616000074).

## Usage

Run:

    python panAV.py -i input_folder -o output_folder

for example:

    python panAV.py -i "data/dutch essays/" -o "output/DE/"

Evaluate:

    python -c "from evaluator import evalAV; evalAV(truth_file, answer_file)"

for example:

    python -c "from evaluator import evalAV; evalAV('data/dutch essays/truth.txt', 'output/DE/answers.txt')"

## Requirements

- Python 2.7.12
- The PAN data, available here to [download](http://pan.webis.de/clef15/pan15-web/author-identification.html "corpus")

