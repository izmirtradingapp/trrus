import streamlit as st
import pandas as pd
st.set_page_config(
    page_title="Çeviriler",
    page_icon="📙",
)

with st.expander("Notu gör."):
    st.markdown('''**Tablodaki bazı metinler uzun olduğu için görünmemektedir. Çift tıklayarak görüntüleyebilirsin.**
                Некоторые тексты в таблице не видны, поскольку они длинные. Посмотреть его можно двойным щелчком мыши.''')

@st.cache_data
def from_data_file():
    return pd.read_csv("tr-rus.csv")    
df = from_data_file()
#######################

def paginate_dataframe(dataframe, page_size):
    total_rows = dataframe.shape[0]
    total_pages = (total_rows // page_size) + (1 if total_rows % page_size > 0 else 0)

    # Sayfa seçimi için kullanıcı girdisi
    page = st.number_input('Page', min_value=1, max_value=total_pages, value=1)

    # Gösterilecek dilimi hesapla
    start_idx = (page - 1) * page_size
    end_idx = start_idx + page_size
    return dataframe[start_idx:end_idx]

# Sayfa başına gösterilecek satır sayısı
page_size = 10
paginated_df = paginate_dataframe(df, page_size)

# DataFrame'i görüntüleme
st.dataframe(paginated_df)