import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
st.set_page_config(page_title="Diwali Sales Analysis", layout="wide")

# Title
st.title("Diwali Sales Analysis Dashboard")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')
    df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
    df.dropna(inplace=True)
    df['Amount'] = df['Amount'].astype('int')
    return df

try:
    df = load_data()
except FileNotFoundError:
    st.error("Data file 'Diwali Sales Data.csv' not found. Please make sure it is in the same directory.")
    st.stop()

# Sidebar
st.sidebar.header("Filters")
selected_state = st.sidebar.multiselect("Select State", df['State'].unique(), default=df['State'].unique())
selected_gender = st.sidebar.multiselect("Select Gender", df['Gender'].unique(), default=df['Gender'].unique())

# Filter data
filtered_df = df[(df['State'].isin(selected_state)) & (df['Gender'].isin(selected_gender))]

# Key Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Sales", f"₹{filtered_df['Amount'].sum():,.0f}")
col2.metric("Total Orders", f"{filtered_df['Orders'].sum():,.0f}")
col3.metric("Total Customers", f"{filtered_df['User_ID'].nunique():,.0f}")

# Visualizations
st.markdown("---")

# Row 1: Gender Analysis
col1, col2 = st.columns(2)

with col1:
    st.subheader("Gender Distribution")
    fig, ax = plt.subplots()
    sns.countplot(x='Gender', data=filtered_df, ax=ax)
    for container in ax.containers:
        ax.bar_label(container)
    st.pyplot(fig)

with col2:
    st.subheader("Sales by Gender")
    fig, ax = plt.subplots()
    sales_gen = filtered_df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    sns.barplot(x='Gender', y='Amount', data=sales_gen, ax=ax)
    st.pyplot(fig)

# Row 2: Age Group Analysis
st.subheader("Age Group Analysis")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Count by Age Group**")
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.countplot(data=filtered_df, x='Age Group', hue='Gender', ax=ax)
    for container in ax.containers:
        ax.bar_label(container)
    st.pyplot(fig)

with col2:
    st.markdown("**Sales by Age Group**")
    fig, ax = plt.subplots(figsize=(10, 5))
    sales_age = filtered_df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    sns.barplot(x='Age Group', y='Amount', data=sales_age, ax=ax)
    st.pyplot(fig)

# Row 3: State Analysis
st.subheader("State Analysis")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Top 10 States by Orders**")
    fig, ax = plt.subplots(figsize=(12, 6))
    sales_state = filtered_df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
    sns.barplot(data=sales_state, x='State', y='Orders', ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    st.markdown("**Top 10 States by Sales Amount**")
    fig, ax = plt.subplots(figsize=(12, 6))
    sales_state_amt = filtered_df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
    sns.barplot(data=sales_state_amt, x='State', y='Amount', ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Row 4: Marital Status & Occupation
st.subheader("Demographics & Occupation")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Marital Status**")
    fig, ax = plt.subplots()
    sns.countplot(data=filtered_df, x='Marital_Status', ax=ax)
    for container in ax.containers:
        ax.bar_label(container)
    st.pyplot(fig)

with col2:
    st.markdown("**Occupation Sales**")
    fig, ax = plt.subplots(figsize=(12, 6))
    sales_occ = filtered_df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
    sns.barplot(data=sales_occ, x='Occupation', y='Amount', ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

# Row 5: Product Analysis
st.subheader("Product Analysis")
col1, col2 = st.columns(2)

with col1:
    st.markdown("**Top Product Categories**")
    fig, ax = plt.subplots(figsize=(12, 6))
    sales_prod = filtered_df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
    sns.barplot(data=sales_prod, x='Product_Category', y='Amount', ax=ax)
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    st.markdown("**Top 10 Products by Orders**")
    fig, ax = plt.subplots(figsize=(12, 6))
    sales_top_prod = filtered_df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
    sns.barplot(data=sales_top_prod, x='Product_ID', y='Orders', ax=ax)
    st.pyplot(fig)
