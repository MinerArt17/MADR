import streamlit as st
import streamlit.components.v1 as components
import json
import lite_v1_0
import functions as f

text = "<strong>Мониторинг нежелательных реакций на лекарственный препарат</strong>"
html_code = f"""
<div style="text-align: center; font-size: 40px;">
    {text}
</div>
"""
components.html(html_code, height=150)

# Ввод ключевого слова
input_name = st.text_input(f"Ключевое слово :", "ozempic", help=f"Введите название препарата или действующего вещества")
data_bases = ["Все",
              "PubMed", 
              "Amazon", 
              "Apteka", 
              "EApteka", 
              "Uppsala", 
              "Drugs.com"
              ]
options_db = st.multiselect("Выберите интересующие источники :", data_bases, "Все")
start_find = st.button("Начать поиск")
place = st.empty()
if start_find and input_name and options_db:
    for db in options_db:
        if db == "Все":
            place.write("Введется поиск в базе данных...")
            res = lite_v1_0.watch_gui(input_name)
            res = f.translate_text(res)
            if res:
                place.write("Поиск завершен :)")
                st.text_area("Результат :", res, height=300, max_chars=100000)
        elif db == "PubMed":
            st.write("pubmed")