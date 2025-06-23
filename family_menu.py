import streamlit as st

# --- Настройки страницы ---
st.set_page_config(
    page_title="Семейное меню",
    layout="wide"
)

# --- Стили ---
st.markdown("""
    <style>
        html, body, .stApp, p, div, span, a, h1, h2, h3, h4, h5, h6, button {
            background-color: #f5cedb !important;
            font-family: Georgia, serif !important;
            color: #381621 !important;
        }

        .menu-title {
            font-size: 2.8em;
            text-align: center;
            margin-bottom: 1em;
        }

        .category-title {
            font-size: 1.5em;
            margin: 1em 0 0.5em;
            font-weight: bold;
        }

        .menu-link {
            display: inline-block;
            margin: 0.3em 0;
            cursor: pointer;
            text-decoration: underline;
            font-size: 1.05em;
        }

        .popup {
            background-color: rgba(213, 153, 171, 1) !important;
            color: #fff5f8 !important;
            padding: 1em;
            border-radius: 10px;
            margin-top: 1em;
            max-width: 100%;
        }


        .popup h4,
        .popup p,
        .popup a {
            background-color: rgba(213, 153, 171, 1) !important;
            font-family: Georgia, serif !important;
        }

        .popup img {
            width: 100%;
            max-width: 300px;
            border-radius: 10px;
            margin: 10px 0;
        }

        .stButton>button {
            background: none;
            border: none;
            color: #381621;
            text-decoration: underline;
            text-align: left;
            font-size: 1.05em;
            padding: 0;
            margin: 0.3em 0;
            cursor: pointer;
            box-shadow: none !important;
            font-family: Georgia, serif !important;
        }

        @media screen and (max-width: 768px) {
            .block-container .element-container {
                width: 100% !important;
                flex: 1 1 100% !important;
            }
        }
    </style>
""", unsafe_allow_html=True)


# --- Заголовок ---
st.markdown('<div class="menu-title">СЕМЕЙНОЕ МЕНЮ</div>', unsafe_allow_html=True)

# --- Пример данных ---
menu = {
    "САЛАТЫ": [
        "крабовый с огурцом",
        "с тунцом, кукурузой и яйцом (курицей)"
    ],
    "ГАРНИРЫ": [
        "макароны твёрдых сортов",
        "паста с песто / томатной пастой / сливками"
    ],
    "ЗАВТРАКИ": [
        "сырники со сметаной и сгущенкой",
        "тосты с творожным сыром, зеленью и ветчиной"
    ]
}

# --- Popup управление ---
if "active_popup" not in st.session_state:
    st.session_state.active_popup = ""

def toggle_popup(dish):
    if st.session_state.active_popup == dish:
        st.session_state.active_popup = ""
    else:
        st.session_state.active_popup = dish

def show_popup(dish_name):
    st.markdown(f"""
        <div class="popup">
            <h4>{dish_name}</h4>
            <p><b>Ингредиенты:</b> (заполнить позже)</p>
            <img src="https://via.placeholder.com/300x200.png?text=Фото+блюда" alt="Фото блюда">
            <p><a href="#" target="_blank">Ссылка на рецепт</a></p>
        </div>
    """, unsafe_allow_html=True)

# --- Рендер ---
from math import ceil
if "popups_state" not in st.session_state:
    st.session_state.popups_state = {}  # dict с состояниями каждого popup

def toggle_popup(dish):
    current = st.session_state.popups_state.get(dish, False)
    st.session_state.popups_state[dish] = not current

num_columns = 3
cols = st.columns(num_columns)

# распределение по колонкам
i = 0
for category, dishes in menu.items():
    with cols[i % num_columns]:
        st.markdown(f'<div class="category-title">{category}</div>', unsafe_allow_html=True)
        for dish in dishes:
            if st.button(dish, key=f"{category}-{dish}"):
                toggle_popup(dish)
            if st.session_state.popups_state.get(dish, False):
                show_popup(dish)
    i += 1
