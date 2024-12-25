from metric_module_v2.mertic import MetricCalculator
import pandas as pd


if __name__ == '__main__':  # Обязательно оборачиваем использование этого класса в данную конструкцию
    df = pd.read_csv("../../../../data/04_functions_tests_1200.csv")

    # Передаём df при инициализации класса (он ОБЯЗАТЕЛЬНО должен содержать столбцы ('Function' и 'Test'),
    # в идеале - только их)
    metric_calculator = MetricCalculator(df)

    metric_calculator.calculate_metrics()  # Запускаем расчёт метрик

    print(metric_calculator.get_metric_frame())  # Получаем либо весь итоговый датафрейм
    print(metric_calculator.get_mean_failed())  # Получаем среднее значение заваленных тестов
    print(metric_calculator.get_mean_coverage_percent())  # Получаем среднее значение процента покрытия

    # Записываем датафрейм с рассчитанными статистиками по каждой строке в файл
    metric_calculator.save_to_csv('tttttt.csv')

    # Можем получить конкретную строку из рассчитанного датафрейма, она содержит следующие строки:
    # ('Function', 'Test', 'coverage_percent', 'Errors')
    print(metric_calculator[1])
