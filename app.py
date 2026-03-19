import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("📊Bhai-GPT – Tera Bhai Analyze Karega Re Baba!")

uploaded_file = st.file_uploader("📂 Apna CSV upload karo bhai", type=['csv'])

if uploaded_file is not None:
    x = pd.read_csv(uploaded_file)
    st.success("Data mil gaya bhai! 🙌")
    st.write("👀 Sample data dekh le:")
    st.dataframe(x.head())
    st.write(f"📐 Shape of your data: {x.shape[0]} rows × {x.shape[1]} columns")

    st.write("Null values:")
    st.write(x.isnull().sum())
    st.write("datatypes:")
    st.write(x.dtypes)
    st.write("Unique values of columns:")
    for i in x.columns:
        st.write(f"🫴{i}:")
        st.write(x[i].unique())
    
    cols = st.multiselect("Select columns of which you want Null values to be replaced:", x.select_dtypes(include=['number']).columns)
    result = st.selectbox("Koi numerical null value replace karwana hai?", ['y', 'n'])

    
    if result == 'y' and len(cols) > 0:
        for col in cols:
            x[col] = x[col].fillna(x[col].mean())  

        st.success("Bhai ne selected columns ke nulls ko mean se bhar diya! ")
        st.write("Updated null values:")
        st.write(x[cols].isnull().sum())
    elif result == 'y' and len(cols) == 0:
        st.warning("Bhai, koi column to select kar le null fill ke liye 😅")
    elif result=='n':
        st.write("thik bhai tu replace nhi karana chahta ")
    

    # 🟢 Ab yahan likho multiselect + graph code
    st.markdown("### 🧠 Bhai se bolo kaunse do columns ka analysis chahiye:")
    selected_cols = st.multiselect("Select 2 columns bhai 👇", x.columns)

    if len(selected_cols) == 2:
        col1, col2 = selected_cols[0], selected_cols[1]

        st.success(f"🎯 Bhai visualize karega: {col1} vs {col2}")

        plot_type = st.selectbox("📊 Kaunsa graph chahiye?", ["Scatterplot", "Boxplot", "Barplot", "Lineplot"])

        fig, ax = plt.subplots()
        if plot_type == "Scatterplot":
            sns.scatterplot(data=x, x=col1, y=col2, ax=ax)
        elif plot_type == "Boxplot":
            sns.boxplot(data=x, x=col1, y=col2, ax=ax)
        elif plot_type == "Barplot":
            sns.barplot(data=x, x=col1, y=col2, ax=ax,palette='cool')
        elif plot_type == "Lineplot":
            sns.lineplot(data=x, x=col1, y=col2, ax=ax)

        st.pyplot(fig)
    elif len(selected_cols) > 2:
        st.warning("Bhai, filhaal sirf 2 column ke liye bana hai plot. Zyada mat dedo 😅")
        
    st.markdown("### pairplot chahiye? niche dekho") 
    selected_cols_2 = st.multiselect("Select the columns bhai 👇", x.select_dtypes(include=['number']).columns)
    cat_cols = x.select_dtypes(include=['object', 'category']).columns

    target_column = st.selectbox("🎯 Bhai, kaunsa column ko hue rakhe?",)
    palette_options = ['Set1', 'coolwarm', 'husl', 'Blues', 'viridis', 'mako', 'rocket','colorblind']
    palette_choice = st.selectbox("🎨 Bhai, kaunsa color palette chahiye?", palette_options)


    
    if len(selected_cols_2)==0:
        pass
    elif len(selected_cols_2)>=2:
        
        fig= sns.pairplot(x[selected_cols_2],hue=target_column,palette=palette_choice)

        st.pyplot(fig.figure)
        
    else:
        st.warning("Bhai , minimum 2 columns to chaiye na pair plot ke liye.... aise nahi ban payega")
        
    
