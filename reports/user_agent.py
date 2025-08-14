from reports.base import Report
import pandas as pd


class UserAgentReport(Report):
    NAME = 'user_agent'
    
    @classmethod
    def name(cls) -> str:
        return cls.NAME
    
    def generate(self, df: pd.DataFrame) -> pd.DataFrame:
        ...

