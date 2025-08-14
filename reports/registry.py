from reports.average import AverageResponseTimeReport
from reports.user_agent import UserAgentReport


# report registry
def get_report_registry() -> dict[str, type]:
    report_classes = [AverageResponseTimeReport, UserAgentReport]
    return {cls.name(): cls for cls in report_classes}
