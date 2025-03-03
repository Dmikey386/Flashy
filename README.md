# Flashy - Flashcard Learning App

## Overview

The **Flashy Flashcard App** is an interactive learning tool designed to help users study foreign language vocabulary through a flashcard system. Built with Python and Tkinter, this application allows users to flip between languages, remove learned words, and dynamically update the learning set. The app supports saving progress and provides a user-friendly graphical interface.

## Skills Used

### **PYTHON**

- Installing and working with Python **packages** (`tkinter`, `pandas`, `random`, `os`)
- **Interactive GUI Development** – Using `tkinter` to create an intuitive flashcard interface
- **Data Management** – Handling CSV files (`pandas`) for saving study progress
- **File Handling** – Reading, writing, and updating vocabulary lists
- **Error Handling** – Managing missing files with exception handling
- **OOP Principles** – Implementing a `Card` class for modular and reusable code

### **GIT**

- **Repository Creation** – Setting up and managing version control
- **Branching and Merging** – Handling feature branches efficiently
- **Pushing to Repository** – Committing and pushing code to remote repositories
- **Handling Merge Conflicts** – Resolving conflicts in collaborative development

### **SOFTWARE DEVELOPMENT**

- **Event-Driven Programming** – Implementing button-click handlers and user interactions
- **Data Persistence** – Using CSV files to save progress dynamically
- **Modular Programming** – Writing reusable functions and separating concerns across files
- **User Interaction & Experience** – Implementing message popups for feedback

## Features

- **Flashcard System**: Presents foreign language words and allows users to flip cards to see translations
- **Word Removal**: Deletes known words from the learning deck to focus on remaining vocabulary
- **Progress Tracking**: Saves progress automatically to `to_study.csv`
- **Data Reset**: Option to reset the study deck if it becomes empty
- **User-Friendly Interface**: Built with Tkinter for a smooth learning experience

## Requirements

Ensure you have the following dependencies installed before running the application:

- Python 3.x
- Tkinter (comes pre-installed with Python)
- `pandas` (for CSV handling)

To install missing dependencies, run:

```bash
pip install pandas
```

## Installation & Usage

1. Clone the repository or download the script.

```bash
git clone https://github.com/your-repository/flashy.git
cd flashy
```

2. Run the application.

```bash
python main.py
```

3. The GUI will open, allowing you to:
   - Flip flashcards between languages
   - Remove known words from the study deck
   - Save progress dynamically

## File Structure

```
flashy/
│── main.py         # Main script for the flashcard app
│── card.py         # Card class for flashcard UI
│── to_study.csv    # Dynamic study list (auto-updated)
│── translated.csv  # Default word set
│── images/         # Contains card images
```

## How It Works

### 1. Flip a Flashcard

Click the **FLIP** button to switch between Spanish and English.

### 2. Keep a Word

Click the **KEEP CARD** button to move to the next word while keeping the current one in the study deck.

### 3. Remove a Learned Word

Click the **DELETE CARD** button to remove the word from the study deck.

### 4. Reset Study Deck

If the deck is empty, the app will prompt the user to restore the default word list.

## CSV Data Format

Vocabulary words are stored in CSV format:

```csv
Spanish,English
hola,hello
adiós,goodbye
```

## Disclaimer

This application was created as part of my personal learning journey in Python development and software engineering, with a focus on building interactive applications and handling data persistence.

---

**Developed by Michael Dodd**
