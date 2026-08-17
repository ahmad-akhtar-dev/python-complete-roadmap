"""Beginner-friendly Python practice.
Created by Ahmad Akhtar
"""

import json
from pathlib import Path
path = Path(__file__).parent / "data" / "student.json"
student = {"name": "Ahmad", "skill": "Python"}
path.write_text(json.dumps(student, indent=2), encoding="utf-8")
loaded = json.loads(path.read_text(encoding="utf-8"))
print(loaded)
