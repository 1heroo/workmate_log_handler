import pytest
import pandas as pd
import json
from reports import get_report_registry, parse_logs, AverageResponseTimeReport



@pytest.fixture
def sample_logs():
    return [
        {"@timestamp": "2025-08-14T10:00:00", "url": "/home", "response_time": 120},
        {"@timestamp": "2025-08-14T10:05:00", "url": "/home", "response_time": 100},
        {"@timestamp": "2025-08-14T10:10:00", "url": "/about", "response_time": 200},
        {"@timestamp": "2025-08-13T10:00:00", "url": "/home", "response_time": 150},
    ]


@pytest.fixture
def sample_log_file(tmp_path, sample_logs):
    file_path = tmp_path / "log.json"
    with open(file_path, "w", encoding="utf-8") as f:
        for log in sample_logs:
            f.write(json.dumps(log) + "\n")
    return str(file_path)


def test_parse_logs_no_filter(sample_log_file):
    logs = parse_logs([sample_log_file])
    assert len(logs) == 4
    assert all(isinstance(log, dict) for log in logs)


def test_parse_logs_with_date_filter(sample_log_file):
    logs = parse_logs([sample_log_file], date_filter="2025-08-14")
    assert len(logs) == 3
    for log in logs:
        assert log["@timestamp"].startswith("2025-08-14")


def test_average_response_time_report(sample_logs):
    df = pd.DataFrame(sample_logs)
    report = AverageResponseTimeReport()
    result = report.generate(df)
    
    assert list(result.columns) == ["handler", "total", "avg_response_time"]
    
    home_row = result[result["handler"] == "/home"].iloc[0]
    assert home_row["total"] == 3 
    assert home_row["avg_response_time"] == pytest.approx((120+100+150)/3, 0.001)


def test_get_report_registry():
    registry = get_report_registry()
    assert "average" in registry
    assert "user_agent" in registry
    assert issubclass(registry["average"], AverageResponseTimeReport)
