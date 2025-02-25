import streamlit as st
import streamlit.components.v1 as components
import json
import lite_v1_1
import functions as f
import datetime as dt

# Основные переменные
date = dt.date.today().strftime('%d-%m-%Y')

# Настройки страницы
st.set_page_config(
    page_title="MADR",
    layout="wide"
    )
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Переменные состояния (не будут обновляться при каждом взаимодействии с сайтом)
if 'user_input' not in st.session_state:
    st.session_state['user_input'] = ''
if 'options_db' not in st.session_state:
    st.session_state['options_db'] = []
if 'start_search' not in st.session_state:
    st.session_state['start_search'] = False
if 'res' not in st.session_state:
    st.session_state['res'] = ''
if 'output' not in st.session_state:
    st.session_state['output'] = ''
if 'write1' not in st.session_state:
    st.session_state['write1'] = 'Результат :'
if 'donwload' not in st.session_state:
    st.session_state['donwload'] = False
if 'report_issue' not in st.session_state:
    st.session_state['report_issue'] = False

# Вот такая прикольная механика, что сначала заводим переменные, потом переменные в другие переменные для удобства (можно и просто st.session_state_var использовать)
user_input = st.session_state['user_input']
options_db = st.session_state['options_db']
start_search = st.session_state['start_search']

# Заголовок страницы
st.title("Мониторинг нежелательных реакций на лекарственный препарат")

# Ввод ключевого слова
form_1 = st.form(key="Options")
user_input = form_1.text_input(f"Ключевое слово :", "ozempic", help=f"Введите название препарата или действующего вещества")
data_bases = ["Все",
              "PubMed (функция недоступна)", 
              "Amazon (функция недоступна)", 
              "Apteka (функция недоступна)", 
              "EApteka (функция недоступна)", 
              "Uppsala (функция недоступна)", 
              "Drugs.com (функция недоступна)"
              ]
options_db = form_1.multiselect("Выберите интересующие источники :", data_bases, "Все")
start_search = form_1.form_submit_button("Начать поиск")

# Вывод программы
place_text1 = st.empty()
if start_search and user_input and options_db:
    for db in options_db:
        if db == "Все":
            place_text1.write("Введется поиск в базе данных...")
            st.session_state.res = f.translate_text(lite_v1_1.watch_gui(user_input))
            # st.session_state.res = f.translate_text(st.session_state.res)
if st.session_state.res: 
    place_text1.write("Поиск завершен :)")
    st.session_state.output = st.text_area("Результат :", st.session_state.res, height=300, max_chars=5000)
if st.session_state.output:
    st.session_state.download = st.download_button("Скачать файл .txt", data=st.session_state.res, file_name=f"MADR_result_{date}.txt", mime="text/plain")
    if st.session_state.download:
        st.write("Началась загрузка файла")
    st.session_state.report_issue = st.button("Оформить и скачать отчёт (функция недоступна)")
    if st.session_state.report_issue:
        st.write("Немного нужно потерпеть")
            