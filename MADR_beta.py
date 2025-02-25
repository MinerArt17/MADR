import streamlit as st
import streamlit.components.v1 as components
import json
import lite_v1_1
import functions as f
import datetime as dt

date = dt.date.today().strftime('%d-%m-%Y')

if __name__ == "__main__":
    pass

text = "<strong>Мониторинг нежелательных реакций на лекарственный препарат</strong>"
html_code = f"""
<div style="text-align: center; font-size: 40px;">
    {text}
</div>
"""
components.html(html_code, height=150)

# Ввод ключевого слова
form_1 = st.form(key="Options")
input_name = form_1.text_input(f"Ключевое слово :", "ozempic", help=f"Введите название препарата или действующего вещества")
data_bases = ["Все",
              "PubMed (функция недоступна)", 
              "Amazon (функция недоступна)", 
              "Apteka (функция недоступна)", 
              "EApteka (функция недоступна)", 
              "Uppsala (функция недоступна)", 
              "Drugs.com (функция недоступна)"
              ]
options_db = form_1.multiselect("Выберите интересующие источники :", data_bases, "Все")
start_find = form_1.form_submit_button("Начать поиск")
place = st.empty()
if start_find and input_name and options_db:
    for db in options_db:
        if db == "Все":
            place.write("Введется поиск в базе данных...")
            res = lite_v1_0.watch_gui(input_name)
            res = f.translate_text(res)
            # if "res" not in st.session_state:
            #     st.session_state.res = res
            if res: # st.session_state.
                place.write("Поиск завершен :)")
                if st.text_area("Результат :", res, height=300, max_chars=100000):
                    place_2 = st.empty()
                    if st.download_button("Скачать файл .txt и обновить страницу", data=res, file_name=f"MADR_result_{date}.txt", mime="text/plain"):
                        place_2.write("Началась загрузка файла")