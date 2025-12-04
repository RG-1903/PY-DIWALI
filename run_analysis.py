import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create plots directory if it doesn't exist
if not os.path.exists('plots'):
    os.makedirs('plots')

# Set style
sns.set(rc={'figure.figsize':(15,5)})

# Load data
print("Loading data...")
df = pd.read_csv('Diwali Sales Data.csv', encoding= 'unicode_escape')

# Data Cleaning
print("Cleaning data...")
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)
df.dropna(inplace=True)
df['Amount'] = df['Amount'].astype('int')

# 1. Gender Count
print("Generating Gender Count plot...")
plt.figure(figsize=(6,5))
ax = sns.countplot(x = 'Gender',data = df)
for bars in ax.containers:
    ax.bar_label(bars)
plt.title('Gender Count')
plt.savefig('plots/gender_count.png')
plt.close()

# 2. Gender Amount
print("Generating Gender Amount plot...")
plt.figure(figsize=(6,5))
sales_gen = df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x = 'Gender',y= 'Amount' ,data = sales_gen)
plt.title('Total Amount by Gender')
plt.savefig('plots/gender_amount.png')
plt.close()

# 3. Age Group Count
print("Generating Age Group Count plot...")
plt.figure(figsize=(15,5))
ax = sns.countplot(data = df, x = 'Age Group', hue = 'Gender')
for bars in ax.containers:
    ax.bar_label(bars)
plt.title('Age Group Count by Gender')
plt.savefig('plots/age_group_count.png')
plt.close()

# 4. Age Group Amount
print("Generating Age Group Amount plot...")
plt.figure(figsize=(15,5))
sales_age = df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(x = 'Age Group',y= 'Amount' ,data = sales_age)
plt.title('Total Amount by Age Group')
plt.savefig('plots/age_group_amount.png')
plt.close()

# 5. State Orders
print("Generating State Orders plot...")
plt.figure(figsize=(25,10)) # Increased width for state names
sales_state = df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.barplot(data = sales_state, x = 'State',y= 'Orders')
plt.title('Top 10 States by Orders')
plt.savefig('plots/state_orders.png')
plt.close()

# 6. State Amount
print("Generating State Amount plot...")
plt.figure(figsize=(25,10))
sales_state_amt = df.groupby(['State'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.barplot(data = sales_state_amt, x = 'State',y= 'Amount')
plt.title('Top 10 States by Amount')
plt.savefig('plots/state_amount.png')
plt.close()

# 7. Marital Status Count
print("Generating Marital Status Count plot...")
plt.figure(figsize=(7,5))
ax = sns.countplot(data = df, x = 'Marital_Status')
for bars in ax.containers:
    ax.bar_label(bars)
plt.title('Marital Status Count')
plt.savefig('plots/marital_status_count.png')
plt.close()

# 8. Marital Status Amount
print("Generating Marital Status Amount plot...")
plt.figure(figsize=(7,5))
sales_marital = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(data = sales_marital, x = 'Marital_Status',y= 'Amount', hue='Gender')
plt.title('Amount by Marital Status and Gender')
plt.savefig('plots/marital_status_amount.png')
plt.close()

# 9. Occupation Count
print("Generating Occupation Count plot...")
plt.figure(figsize=(20,5))
ax = sns.countplot(data = df, x = 'Occupation')
for bars in ax.containers:
    ax.bar_label(bars)
plt.title('Occupation Count')
plt.savefig('plots/occupation_count.png')
plt.close()

# 10. Occupation Amount
print("Generating Occupation Amount plot...")
plt.figure(figsize=(20,5))
sales_occ = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)
sns.barplot(data = sales_occ, x = 'Occupation',y= 'Amount')
plt.title('Amount by Occupation')
plt.savefig('plots/occupation_amount.png')
plt.close()

# 11. Product Category Count
print("Generating Product Category Count plot...")
plt.figure(figsize=(25,10))
ax = sns.countplot(data = df, x = 'Product_Category')
for bars in ax.containers:
    ax.bar_label(bars)
plt.title('Product Category Count')
plt.xticks(rotation=45)
plt.savefig('plots/product_category_count.png')
plt.close()

# 12. Product Category Amount
print("Generating Product Category Amount plot...")
plt.figure(figsize=(25,10))
sales_prod = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)
sns.barplot(data = sales_prod, x = 'Product_Category',y= 'Amount')
plt.title('Top 10 Product Categories by Amount')
plt.xticks(rotation=45)
plt.savefig('plots/product_category_amount.png')
plt.close()

# 13. Top 10 Products by Orders
print("Generating Top 10 Products plot...")
plt.figure(figsize=(15,7))
sales_top_prod = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)
sns.barplot(data = sales_top_prod, x = 'Product_ID',y= 'Orders')
plt.title('Top 10 Products by Orders')
plt.savefig('plots/top_10_products.png')
plt.close()

print("Analysis complete. Plots saved to 'plots' directory.")
