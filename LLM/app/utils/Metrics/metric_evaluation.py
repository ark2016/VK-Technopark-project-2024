import pandas as pd
from ..Metrics.metric_module_v2.mertic import MetricCalculator

def evaluate_metrics(csv_path: str) -> dict:
    """
    Выполняет расчёт метрик на основе переданного пути к CSV файлу.

    :param csv_path: Путь к CSV файлу с результатами.
    :return: Словарь с рассчитанными метриками и деталями.
    """
    try:
        # Загрузка данных из CSV
        df = pd.read_csv(csv_path)

        # Инициализация и расчёт метрик
        metric_calculator = MetricCalculator(df)
        metric_calculator.calculate_metrics()

        # Получение всех необходимых данных
        metrics_frame = metric_calculator.get_metric_frame()
        mean_failed = metric_calculator.get_mean_failed()
        mean_coverage_percent = metric_calculator.get_mean_coverage_percent()

        # Формируем результат
        result = {
            "metric_frame": metrics_frame.to_dict(orient="records"),
            "mean_failed": mean_failed,
            "mean_coverage_percent": mean_coverage_percent,
        }

        # Записываем рассчитанный датафрейм в файл
        output_csv = "calculated_metrics.csv"
        metric_calculator.save_to_csv(output_csv)
        result["output_file"] = output_csv

        return result

    except FileNotFoundError:
        raise ValueError("CSV file not found.")
    except ValueError as ve:
        raise ValueError(f"Invalid data: {ve}")
    except Exception as e:
        raise RuntimeError(f"Internal Error: {str(e)}")
