import json

# -------------------------
# PASTE YOUR FNF CHART JSON HERE
# -------------------------
chart_json = '''
[
    {"time": 0.5, "note": "left"},
    {"time": 1.0, "note": "down"},
    {"time": 1.5, "note": "up"},
    {"time": 2.0, "note": "right"}
]
'''

# Load JSON
try:
    chart = json.loads(chart_json)
except Exception as e:
    print("Error parsing JSON:", e)
    exit()

# Generate Julian block instructions
previous_time = 0
print("\n--- Julian Block Instructions ---\n")
for note in chart:
    wait_time = round(note["time"] - previous_time, 2)
    print(f"[Wait {wait_time}s] → [Spawn Arrow: {note['note']}]")
    previous_time = note["time"]

print("\n--- End of Instructions ---\n")