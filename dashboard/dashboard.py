import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from datetime import datetime

@st.cache_data
def load_data():
    customers = pd.read_csv("dataset/customers_dataset.csv")
    orders = pd.read_csv("dataset/orders_dataset.csv")
    order_items = pd.read_csv("dataset/order_items_dataset.csv")
    order_payments = pd.read_csv("dataset/order_payments_dataset.csv")
    order_reviews = pd.read_csv("dataset/order_reviews_dataset.csv")
    products = pd.read_csv("dataset/products_dataset.csv")
    sellers = pd.read_csv("dataset/sellers_dataset.csv")
    product_category = pd.read_csv("dataset/product_category_name_translation.csv")
    return customers, orders, order_items, order_payments, order_reviews, products, sellers, product_category

customers, orders, order_items, order_payments, order_reviews, products, sellers, product_category = load_data()

st.title("Dashboard Analisis E-commerce")
st.markdown("""
Dashboard ini memberikan wawasan tentang karakteristik pelanggan dan tren pembelian produk berdasarkan musim.
""")

orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'])
orders['season'] = orders['order_purchase_timestamp'].dt.month % 12 // 3 + 1
season_labels = {1: "Musim Dingin", 2: "Musim Semi", 3: "Musim Panas", 4: "Musim Gugur"}
orders['season'] = orders['season'].map(season_labels)

season_options = ["Semua Musim"] + list(season_labels.values())
selected_season = st.selectbox("Pilih Musim", options=season_options)

if selected_season != "Semua Musim":
    filtered_orders = orders[orders['season'] == selected_season]
else:
    filtered_orders = orders

customer_orders = filtered_orders.groupby("customer_id").size().reset_index(name="order_count")
avg_order_per_customer = customer_orders["order_count"].mean()
st.metric("Rata-rata pesanan per pelanggan", f"{avg_order_per_customer:.2f}")

merged_data = order_items.merge(filtered_orders[['order_id', 'season', 'order_purchase_timestamp']], on='order_id')
merged_data = merged_data.merge(products[['product_id', 'product_category_name']], on='product_id')
seasonal_top_products = merged_data.groupby(['season', 'product_category_name']).size().reset_index(name='count')
top_products = seasonal_top_products.sort_values(['season', 'count'], ascending=[True, False]).groupby('season').head(5)

fig_seasonal = px.bar(top_products, x='product_category_name', y='count', color='season', barmode='group', 
                        title='Produk Terlaris di Setiap Musim')
st.plotly_chart(fig_seasonal)

category_sales = merged_data.groupby(['product_category_name', 'order_purchase_timestamp']).size().reset_index(name='count')
fig_category_sales = px.line(category_sales, x='order_purchase_timestamp', y='count', color='product_category_name', 
                            title='Tren Penjualan Berdasarkan Kategori Produk')
st.plotly_chart(fig_category_sales)
