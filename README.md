# ValiTux 

ValiTux is a strict gating and validation tool for LLM-generated Python code. It ensures that only syntactically correct code reaches your local file system, automatically purging junk files and keeping your workspace clean.
Features

    Striktes Gating: Filters outputs for valid Python code.

    Intelligente Validierung: Automatic syntax check (py_compile) after extraction.

    Automatische Bereinigung: Removes cache files and faulty code snippets.

    Robustness: Integrated #EOF tagging to ensure integrity.

### Installation & Setup

You can get started quickly by using a virtual environment to manage dependencies:
Bash

###  Schnelle Installation / One-Liner
    python3 -m venv venv && source venv/bin activate && pip install requests

Manual Installation

    Clone the repository:
    

    git clone https://github.com/o-valo/valitux.git
    cd valitux

    Create and activate virtual environment:
    

    python3 -m venv venv
    source venv/bin/activate  

    On Windows use: venv\Scripts\activate

    Install dependencies:
    

    pip install requests

### Configuration

Valitus reads from a model-conf.txt. Ensure your config file follows the structure:
Plaintext

    ENDPOINT|http://10.7.0.79:11434/api/generate
    # model|n_pred|temp|timeout|prompt
    qwen3.5:latest|500|0.7|60| Berechne die mathematische Kreiszahl Pi auf 100 Dezimalstellen mit Python decimal. Keine Hardware-Infos!

#### German Summary (Deutsch)

Valitux ist ein striktes Gating- und Validierungstool für Python-Code, der von LLMs generiert wird. Es stellt sicher, dass nur syntaktisch korrekter Code auf deinem System gespeichert wird, indem es automatische Syntax-Checks durchführt und fehlerhafte Dateien sofort bereinigt.

### Installation (Kurzform)

Für eine schnelle Einrichtung in einem virtuellen Environment:

    python3 -m venv venv && source venv/bin/activate && pip install requests

Konfiguration  

Das Tool nutzt eine model-conf.txt Datei, um die Modelle, Parameter und Prompts zu definieren. Die Ergebnisse werden im lokalen Verzeichnis als .py Dateien abgelegt.

    ENDPOINT|http://10.7.0.79:11434/api/generate
    # model|n_pred|temp|timeout|prompt
    qwen3.5:latest|500|0.7|60| Berechne die mathematische Kreiszahl Pi auf 100 Dezimalstellen mit Python decimal. Keine Hardware-Infos!

    ### Valitux wurde Hilfe von KI erstellt, 
