from .average import AverageResponseTimeReport
from .useragent import UserAgentReport


# report registry
def get_report_registry() -> dict[str, type]:
    report_classes = [AverageResponseTimeReport, UserAgentReport]
    return {cls.name(): cls for cls in report_classes}
