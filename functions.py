from translate import Translator

def translate_text(text, from_lang='en', to_lang='ru'):
    # Создаём объект Translator, указывая исходный язык и язык перевода
    translator = Translator(from_lang=from_lang, to_lang=to_lang)
    try:
        # Пытаемся перевести текст
        translated_text = translator.translate(text)
        return translated_text  # Возвращаем переведённый текст
    except Exception as e:
        # Если возникает ошибка, возвращаем сообщение об ошибке
        return f"Error: {e}"
