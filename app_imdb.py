import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import streamlit as st
from collections import Counter

st.set_page_config(
    page_title="Top 50 Movies Dashboard",
    layout="wide")

url = "https://raw.githubusercontent.com/wdyprtiwi/davis-2024/main/imdb_combined.csv"
df_imbd = pd.read_csv(url)

st.write("### Preview Data Top 50 Movies on IMDB")
st.dataframe(df_imbd.head(10))

# Memisahkan layar dengan st.columns untuk 2 kolom
col1, col2 = st.columns(2)

# Kolom kiri: Composition and Comparasion
with col1:
    st.write("### Comparasion Rating by Gross World")
    
    # Perbandingan rating berdasarkan gross world
    plt.figure(figsize=(8, 6))
    plt.bar(df_imbd['Rating'], df_imbd['Gross_World'])
    plt.xlabel('Rating')
    plt.ylabel('Gross World')
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, pos: '{:,.0f}'.format(y)))
    st.pyplot(plt)
    
    st.write("""
    ### Deskripsi:
    
    <div style="text-align: justify;">
        <p>Grafik di atas menjelaskan perbandingan Gross World berdasarkan Rating film. Dapat diambil kesimpulan bahwa film dengan
        rating PG-13 mendapatkan gross world yang paling tinggi. Rating film Approved dan dan Not Rated tidak menampilkan bar chart
        karena perbandingan yang begitu besar dengan rating film yang lainnya.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Donut chart untuk Composition of Films by Rating
    st.write("### Composition of Films by Rating")

    rating_counts = Counter(df_imbd['Rating'])
    labels = list(rating_counts.keys())
    sizes = list(rating_counts.values())
    colors = ['#FF0000', '#0000FF', '#FFFF00', '#ADFF2F', '#FFA500', '#8A2BE2']
    explode = (0.05,) * len(labels)  # Meledakkan semua bagian
    
    fig, ax = plt.subplots()
    ax.pie(sizes, colors=colors, labels=labels,
           autopct='%1.1f%%', pctdistance=0.85, explode=explode)
    centre_circle = plt.Circle((0, 0), 0.70, fc='white')
    fig.gca().add_artist(centre_circle)
    plt.legend(labels, loc="upper right", title="Rating")
    st.pyplot(fig)
    
    st.write("""
    ### Deskripsi:
    
    <div style="text-align: justify;">
        <p>Grafik di atas menjelaskan komposisi rating film yang ada di top 50 IMDB. 
        Diketahui bahwa komposisi top 50 movies yang paling banyak pada IMBD adalah film 
        dengan rating R kemudian disusul dengan PG-13, dan PG.</p>
    </div>
    """, unsafe_allow_html=True)


# Kolom kanan: Relationship dan Distribution
with col2:
    st.write("### Relationship of Duration and Budget")
    
    # Scatter plot untuk Relationship between Gross US and Gross World
    plt.figure(figsize=(8, 6))
    sns.scatterplot(data=df_imbd, x='Gross_US', y='Gross_World')
    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
    plt.gca().yaxis.set_major_formatter(ticker.FuncFormatter(lambda y, pos: '{:,.0f}'.format(y)))
    plt.xlabel('Gross US')
    plt.ylabel('Gross World')
    st.pyplot(plt)
    
    st.write("""
    ### Deskripsi:
    
    <div style="text-align: justify;">
        <p>Grafik di atas memperlihatkan apakah terdapat hubungan antara Gross US dan Gross World. 
        Hubungan tersebut memiliki korelasi yang positif dimana film yang mendapatkan gross US tinggi 
        maka film tersebut mendapatkan gross world yang tinggi juga.</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Histogram untuk Distribution of Gross World
    st.write("### Distribution of Gross World")

    plt.figure(figsize=(8, 6))
    sns.histplot(df_imbd['Gross_World'], bins=10, kde=True)
    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x)))
    plt.xlabel('Gross World')
    plt.ylabel('Frequency')
    st.pyplot(plt)
    
    st.write("""
    ### Deskripsi:
    
    <div style="text-align: justify;">
        <p>Grafik di atas menjelaskan distribusi gross world yang didapatkan dari setiap top 50 film.
        Gross world dengan rentan 0-100,000,000 memiliki frekuensi yang paling tinggi dibandingankan 
        dengan yang lainnya.</p>
        </div>
    """, unsafe_allow_html=True)
