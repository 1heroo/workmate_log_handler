import argparse
import json
from tabulate import tabulate
import pandas as pd
from reports import get_report_registry



def parse_logs(files: list[str], date_filter=None) -> list[dict]:
    """log parsing and filtering by date func"""
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


def main():
    parser = argparse.ArgumentParser(description="Log report")
    parser.add_argument("--file", nargs="+", required=True, help="Paths to log files")
    parser.add_argument("--report", required=True, choices=["average"], help="Report type")
    parser.add_argument("--date", help="Filter logs by date (YYYY-MM-DD)")
    args = parser.parse_args()

    logs = parse_logs(args.file, args.date)
    df = pd.DataFrame(logs)

    if df.empty:
        print("No logs found for the given parameters.")
        return

    reports = get_report_registry()
    report = reports.get(args.report)
    if not report:
        print(f"Report {args.report} not found.")
        return
    
    report = report()
    report_df = report.generate(df)
    print(tabulate(tabular_data=report_df.values.tolist(), headers=report_df.columns.tolist()))



if __name__ == "__main__":
    main()

