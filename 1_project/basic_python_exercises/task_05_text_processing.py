# Обработка строки лога: замена и разделение
def process_log(log: str) -> list[str]:
    cleaned = log.strip().replace("Ошибка", "Ошибка критическая", 1)
    return cleaned.split()

# Анализ строки лога: длина, критичность, количество слов
def analyze_log_message(log: str) -> dict:
    return {
        "length": len(log),
        "is_critical": "critical" in log.lower(),
        "words": log.count(" ") + 1
    }
