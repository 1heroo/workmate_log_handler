from reports.base import Report
from reports.average import AverageResponseTimeReport
from reports.user_agent import UserAgentReport
from reports.registry import get_report_registry
from reports.parse_logs import parse_logs


__all__ = [
    "Report",
    "AverageResponseTimeReport",
    "UserAgentReport",
    "get_report_registry",
    "parse_logs"
]
