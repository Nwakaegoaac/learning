#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd #for data exploration
import matplotlib.pyplot as plt #for data visualization
import seaborn as sns #for statistical graphics

# Shows plots in jupyter notebook
get_ipython().run_line_magic('matplotlib', 'inline')

# Set plot style
sns.set(color_codes=True) # used to assign color codes


# In[6]:


#load datasets
client_data = pd.read_csv('C:/Users/EGO/Desktop/Kaego Portfolio/BCG/Second Task/client_data.csv')
price_data = pd.read_csv('C:/Users/EGO/Desktop/Kaego Portfolio/BCG/Second Task/price_data.csv')


# In[7]:


price_data.head()


# In[8]:


client_data.head()


# In[9]:


price_data.info()


# In[10]:


client_data.info()


# In[11]:


price_data.describe()


# In[12]:


client_data.describe()


# In[13]:


# Select numerical columns
numerical_features = ['cons_12m', 'cons_gas_12m', 'cons_last_month', 'forecast_cons_12m', 'forecast_cons_year', 'forecast_discount_energy']

# Plot histograms for numerical features
for feature in numerical_features:
    plt.figure(figsize=(8, 4))
    sns.histplot(client_data[feature], bins=20, kde=True, color='blue')
    plt.title(f'Distribution of {feature}')
    plt.xlabel(feature)
    plt.ylabel('Frequency')
    plt.show()


# In[63]:


# Calculate the difference between churned and not churned customers
churned_customers = client_data['churn'].sum()  # Sum of 1s (churned)
total_customers = len(client_data)
not_churned_customers = total_customers - churned_customers  # Total - churned

print("Total customers:", total_customers)
print("Churned Customers:", churned_customers)
print("Difference:", not_churned_customers)


# In[ ]:





# In[126]:


# Define the values for the two variables
churned = (1419 / 14606)  # Value for the first variable
not_churned = (13187 / 14606)   # Value for the second variable

# Set the x-coordinate for the left edge of the bar
x = 0.5

# Set the width of the bar
width = 0.4

# Create a figure and axis
fig, ax = plt.subplots()

# Create the first part of the bar (churned)
ax.bar(x, churned, width, color='blue', label='churned')

# Create the second part of the bar (Not churned)
ax.bar(x, not_churned, width, bottom=churned, color='red', label='Not churned')

# Set the y-axis limits to span the entire bar
ax.set_ylim(0, 1)

# Set the x-axis limits to show the entire bar
ax.set_xlim(0, 1)

# Add labels, title, and legend
ax.set_ylabel('Percentage')
ax.set_title('Percentage of Churned customer')
ax.legend()

# Show the plot
plt.show()


# In[ ]:




