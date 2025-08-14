# Workmate Log Handler

Система для анализа и генерации отчетов по логам веб-приложений с модульной архитектурой.
## Структура проекта

```
workmate_log_handler/
├── main.py                 # Точка входа CLI
├── requirements.txt        # Зависимости
├── reports/               # Модуль отчетов
│   ├── __init__.py        # Экспорты модуля
│   ├── base.py            # Базовый класс Report
│   ├── registry.py        # Реестр отчетов
│   ├── parse_logs.py      # Парсер логов
│   ├── average.py         # Отчет по среднему времени ответа
│   └── user_agent.py      # Отчет по User-Agent (заготовка)
└── tests/                 # Тесты
    └── test_average.py    # Тесты для average отчета
```

## Установка

```bash
pip install -r requirements.txt
```

## Использование

### Базовое использование

```bash
python main.py --file example1.log example2.log --report average
```

### Фильтрация по дате
```bash
python main.py --file example1.log --report average --date 2025-08-14
```

### Пример вывода

```
handler                     total    avg_response_time
------------------------  -------  -------------------
/api/homeworks/...          55312                0.093
/api/context/...            43928                0.019
/api/specializations/...     8335                0.052
/api/challenges/...          1476                0.078
/api/users/...               1447                0.066
```

## Архитектура
### Принципы проектирования

**1. Разделение ответственности:**
- `main.py` - только CLI интерфейс
- `reports/` - бизнес-логика генерации отчетов
- `tests/` - тестирование функциональности

**2. Модульность:**
- Каждый тип отчета - отдельный класс
- Регистрация через реестр
- Легкое добавление новых отчетов

**3. Расширяемость:**
- Базовый класс `Report` определяет интерфейс

### Добавление нового отчета
1. Создайте класс, наследующий `Report`:
```python
# reports/my_report.py
from reports.base import Report
import pandas as pd

class MyReport(Report):
    NAME = 'my_report'
    
    @classmethod
    def name(cls) -> str:
        return cls.NAME
    
    def generate(self, df: pd.DataFrame) -> pd.DataFrame:
        # Ваша логика обработки
        return processed_df
```

2. Добавьте в реестр (`reports/registry.py`):

```python
from reports.my_report import MyReport

def get_report_registry() -> dict[str, type]:
    report_classes = [AverageResponseTimeReport, UserAgentReport, MyReport]
    return {cls.name(): cls for cls in report_classes}
```

### Доступные отчеты
### `average` - Среднее время ответа

Анализирует время ответа по эндпоинтам:
- **Группировка**: по URL
- **Метрики**: количество запросов, среднее время ответа
- **Сортировка**: по количеству запросов (убывание)

### `user_agent` - Анализ User-Agent *(в разработке)*

