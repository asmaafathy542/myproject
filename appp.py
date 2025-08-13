import streamlit as st
from PIL import Image
import os
import gdown

# تحميل ml_model.pkl من Google Drive لو مش موجود
if not os.path.exists("ml_model.pkl"):
    url = "https://drive.google.com/uc?id=1-Wgh3uUPrv2AO-_I3-6iGjLOYskWEDx6"
    gdown.download(url, "ml_model.pkl", quiet=False)

# عنوان رئيسي للتطبيق
st.title("Restaurant Analysis & Prediction App")

# اختيار الصفحة
page = st.sidebar.selectbox("Select a page:", ["EDA", "Prediction"])

if page == "EDA":
    st.header("Exploratory Data Analysis")

    st.subheader("1. Does the demography of an area matter?")
    img1 = Image.open("location_rating_boxplot.png")
    st.image(img1, caption="location_rating_boxplot.png", use_column_width=True)

    st.subheader("2. Does the location of a particular type of restaurant depend on the people living in that area? ")
    img2 = Image.open("rest_type_distribution.png")
    st.image(img2, caption="rest_type_distribution", use_column_width=True)

    st.subheader("3. Does the theme of the restaurant matter?")
    img3 = Image.open("theme_heatmap.png")
    st.image(img3, caption="Theme Heatmap", use_column_width=True)

    st.subheader("4. Is a food chain category restaurant likely to have more customers than its counterpart?")
    img3 = Image.open("chain_vs_nonchain_votes.png")
    st.image(img3, caption="chain_vs_nonchain_votes", use_column_width=True)

    st.subheader("5. Are any neighborhoods similar? ")
    img5 = Image.open("neighborhood_similarity_pca.png")
    st.image(img5, caption="neighborhood_similarity", use_column_width=True)

    st.subheader("6. Do expensive restaurants get better ratings?")
    img6 = Image.open("expensive_vs_rating.png")
    st.image(img6, caption="expensive_vs_rating", use_column_width=True)

    st.subheader("7. Does online delivery availability affect the restaurant’s rating?")
    img6 = Image.open("online_delivery_vs_rating.png")
    st.image(img6, caption="online_delivery_vs_rating", use_column_width=True)