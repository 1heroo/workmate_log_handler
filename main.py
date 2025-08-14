import argparse
from tabulate import tabulate
import pandas as pd
from reports import get_report_registry, parse_logs 



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

