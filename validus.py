import requests
import py_compile
import os
import shutil

# Version: 0.2.7
# Ziel: Striktes Gating, intelligente Validierung, automatische Bereinigung.
# Regel: Keine Müll-Dateien, keine Caches, komplette Datei.

def run_from_config(config_file):
    try:
        with open(config_file, "r") as f:
            lines = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        print("ALARM: Config nicht gefunden.")
        return

    endpoint = next((line.split("|")[1] for line in lines if line.startswith("ENDPOINT|")), None)
    if not endpoint: return

    for line in lines:
        if line.startswith("ENDPOINT|"): continue
        
        # Konfiguration parsen
        try:
            model, n_pred, temp, timeout, prompt = [x.strip() for x in line.split("|")]
        except ValueError: continue
        
        print(f"--- Starte: {model} ---")
        payload = {
            "model": model,
            "messages": [{"role": "user", "content": prompt}],
            "stream": False,
            "options": {"num_predict": int(n_pred), "temperature": float(temp)}
        }
        
        try:
            response = requests.post(endpoint, json=payload, timeout=(10, int(timeout)))
            if response.status_code == 200:
                raw = response.json().get("message", {}).get("content", "")
                
                # Intelligentere Code-Extraktion
                code = ""
                if "```python" in raw:
                    code = raw.split("```python")[-1].split("```")[0].strip()
                elif "```" in raw:
                    code = raw.split("```")[-1].split("```")[0].strip()
                else:
                    code = raw if "def " in raw or "import " in raw else ""

                # Nur speichern, wenn wir echten Code haben
                if len(code) > 20:
                    filename = f"out_{model.replace(':', '_')}.py"
                    with open(filename, "w") as f:
                        f.write(code + "\n#EOF")
                    
                    try:
                        py_compile.compile(filename, doraise=True)
                        print(f"Erfolg: {filename} [Syntax OK]")
                    except:
                        print(f"ALARM: Syntaxfehler in {filename}. Lösche Datei.")
                        if os.path.exists(filename): os.remove(filename)
                else:
                    print(f"ALARM: {model} hat keinen validen Code geliefert.")
        except Exception as e:
            print(f"ALARM: {model} Verbindungsfehler: {e}")

    # Finale Bereinigung: __pycache__ löschen, falls vorhanden
    if os.path.exists("__pycache__"):
        shutil.rmtree("__pycache__")
        print("System: __pycache__ erfolgreich entfernt.")

if __name__ == "__main__":
    run_from_config("model-conf.txt")
#EOF
