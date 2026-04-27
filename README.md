# 🧬 DNA - Sequence Matcher

![Python](https://img.shields.io/badge/Language-Python-blue.svg)
![CS50x](https://img.shields.io/badge/CS50x-Week%206-orange.svg)
![Algorithm](https://img.shields.io/badge/Algorithm-String%20Matching-brightgreen.svg)

A powerful Python program that identifies a person by analyzing their **DNA sequence** using Short Tandem Repeats (STRs).

## ✨ Overview

This program reads a CSV database of individuals and their STR counts, then compares them against a given DNA sequence to find the best match. It counts consecutive repeats of specific DNA sequences (STRs) and determines whose DNA matches the given sample.

Inspired by real forensic DNA analysis techniques.

## 🎯 Features

- ✅ Accepts command-line arguments (CSV database + DNA sequence file)
- ✅ Counts longest consecutive repeats of multiple STRs
- ✅ Efficient string pattern matching
- ✅ Loads and parses CSV data using Python’s `csv` module
- ✅ Handles large DNA sequences efficiently
- ✅ Returns the name of the matching person or "No match"
- ✅ Clean and well-structured code

## 🚀 Quick Start

```bash
# Clone the repository
git clone https://github.com/yourusername/dna.git
cd dna

# Run the program
python dna.py databases/small.csv sequences/1.txt
Example:
Bashpython dna.py databases/large.csv sequences/5.txt
📊 Example Output
textAlice
or
textNo match
🧠 What I Learned

Advanced string processing and pattern matching
Working with CSV files in Python (csv.reader)
Command-line argument handling (sys.argv)
Efficient counting of consecutive substrings
Algorithmic problem solving with real-world applications (forensics)
Organizing code into clean, reusable functions

🛠️ Built With

Python 3
Standard libraries: csv, sys
