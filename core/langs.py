# core/langs.py

import json
import os

def get_texts(language="vi"):
    default_lang = "vi"
    lang_path = f"translations/{language}.json"

    try:
        with open(lang_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        with open(f"translations/{default_lang}.json", "r", encoding="utf-8") as f:
            return json.load(f)
