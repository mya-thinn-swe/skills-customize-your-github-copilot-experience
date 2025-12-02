# 📘 Assignment: Python Text Processing

## 🎯 Objective

Write a Python program that practices working with strings, file I/O, and common text-manipulation tasks. The script will load a text file, compute basic statistics, and provide simple text transformations.

## 📝 Tasks

### 🛠️	Text Processing Script

#### Description
Create a command-line Python program that reads a text file and implements utilities for analyzing and transforming the text. Students should implement functions to count lines, words, and characters, compute the most common words, and perform simple find-and-replace operations.

#### Requirements
Completed program should:

- Read a text file specified by the user (or use a default sample file)
- Report counts for lines, words, and characters
- Find and list the top N most frequent words (ignore case and punctuation)
- Support a simple find-and-replace mode that writes the transformed output to a new file
- Be documented with usage instructions and examples

#### Example Usage

```bash
python3 starter-code.py sample_text.txt --top 5
# Output: Lines: 4 | Words: 120 | Characters: 650
# Top 5 words: the, and, to, of, a

python3 starter-code.py sample_text.txt --replace "old" "new" --out replaced.txt
```

## 📎 Starter Files

- `starter-code.py` — starter script with helper functions and a minimal CLI
- `sample_text.txt` — small sample text for testing and development

---

If you'd like, I can extend the starter script with additional exercises (e.g., sentence tokenization, stop-word removal, or simple concordance generation). Which extras do you want included? 
