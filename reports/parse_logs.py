import json


def parse_logs(files: list[str], date_filter=None) -> list[dict]:
    """парсинг логов"""
    
    entries = []
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            for line in f.readlines():
                try:
                    log = json.loads(line)
                except json.JSONDecodeError:
                    continue
                if date_filter:
                    log_date = log.get("@timestamp", "").split("T")[0]
                    if log_date != date_filter:
                        continue
                entries.append(log)
    return entries
