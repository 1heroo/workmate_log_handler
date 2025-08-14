from .base import Report
import pandas as pd


class AverageResponseTimeReport(Report):
    NAME = 'average'

    @classmethod
    def name(cls) -> str:
        return cls.NAME
    
    def generate(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df[df['url'].notna() & df['response_time'].notna()]  # фильтрация записей с пустыми url и response_time

        stats = df.groupby('url', as_index=False)['response_time'].agg(['count', 'mean'])  # группировка по url и подсчет колва и среднего времени
        stats.columns = ['handler', 'total', 'avg_response_time'] 

        stats['avg_response_time'] = stats['avg_response_time'].round(3)  # округление
        return stats.sort_values(by='total', ascending=False)
    