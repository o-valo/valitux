[ENG]
#Validus 

Validus is a strict gating and validation tool for LLM-generated Python code. It ensures that only syntactically correct code reaches your local file system, automatically purging junk files and keeping your workspace clean.
Features

    Striktes Gating: Filters outputs for valid Python code.

    Intelligente Validierung: Automatic syntax check (py_compile) after extraction.

    Automatische Bereinigung: Removes cache files and faulty code snippets.

    Robustness: Integrated #EOF tagging to ensure integrity.

Installation & Setup

You can get started quickly by using a virtual environment to manage dependencies:
Bash

# Schnelle Installation / One-Liner
python3 -m venv venv && source venv/bin/activate && pip install requests

Manual Installation

    Clone the repository:
    Bash

    git clone https://github.com/yourusername/validus.git
    cd validus

    Create and activate virtual environment:
    Bash

    python3 -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate

    Install dependencies:
    Bash

    pip install requests

Configuration

Validus reads from a model-conf.txt. Ensure your config file follows the structure:
Plaintext

ENDPOINT|http://10.7.0.79:11434/api/generate
# model|n_pred|temp|timeout|prompt
qwen3.5:latest|500|0.7|60|Write a function to calculate Fibonacci.

German Summary (Deutsch)

Validus ist ein striktes Gating- und Validierungstool für Python-Code, der von LLMs generiert wird. Es stellt sicher, dass nur syntaktisch korrekter Code auf deinem System gespeichert wird, indem es automatische Syntax-Checks durchführt und fehlerhafte Dateien sofort bereinigt.
Installation (Kurzform)

Für eine schnelle Einrichtung in einem virtuellen Environment:
python3 -m venv venv && source venv/bin/activate && pip install requests
Konfiguration  

Das Tool nutzt eine model-conf.txt Datei, um die Modelle, Parameter und Prompts zu definieren. Die Ergebnisse werden im lokalen Verzeichnis als .py Dateien 
