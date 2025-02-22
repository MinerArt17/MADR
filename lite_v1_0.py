import json

def main():
    drug_name = input("Введите название препарата: ").strip()
    # watch(drug_name)
    res = watch_gui(drug_name)
    print(res)

def watch(drug_name):
    try:
        with open("side_effects_database.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Файл side_effects_database.json не найден.")
        return

    # Ищем препарат без учёта регистра
    matching_drug = None
    for key in data:
        if key.lower() == drug_name.lower():
            matching_drug = key
            break

    if not matching_drug:
        print(f"Препарат '{drug_name}' не найден в базе данных.")
        return

    result_lines = [f"Побочные эффекты для препарата '{matching_drug}':"]
    entries = data[matching_drug]
    for entry in entries:
        side_effects = entry.get("side effects", [])
        first_met_dates = entry.get("first met", [])
        # Для каждого побочного эффекта выводим соответствующую дату
        for effect, date_str in zip(side_effects, first_met_dates):
            result_lines.append(f"{effect}: {date_str}")

    print("\n".join(result_lines))

def watch_gui(drug_name):
    # Функция для интеграции с GUI. Принимает название препарата и возвращает результаты в виде строки.
    try:
        with open("side_effects_database.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return "Файл side_effects_database.json не найден."

    matching_drug = None
    for key in data:
        if key.lower() == drug_name.lower():
            matching_drug = key
            break

    if not matching_drug:
        return f"Препарат '{drug_name}' не найден в базе данных."

    result_lines = [f"Побочные эффекты для препарата '{matching_drug}':"]
    entries = data[matching_drug]
    for entry in entries:
        side_effects = entry.get("side effects", [])
        first_met_dates = entry.get("first met", [])
        for effect, date_str in zip(side_effects, first_met_dates):
            result_lines.append(f"{effect}: {date_str}")

    return "\n".join(result_lines)

if __name__ == "__main__":
    main()
