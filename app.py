#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt


# Initializing the Flask application
app = Flask(__name__)

# Function to read data from an Excel file
def read_data(file_path):
    data = pd.read_excel(file_path)
    return data


# In[2]:


# This Function is to plot the total annual waste per province
def plot_total_annual_waste(data):
    grouped_data = data.groupby(['Year', 'Province']).sum().reset_index()
    plt.figure(figsize=(10, 6))
    for province in grouped_data['Province'].unique():
        province_data = grouped_data[grouped_data['Province'] == province]
        plt.plot(province_data['Year'], province_data['TotalWaste'], label=province)
    
    plt.xlabel('Year')
    plt.ylabel('Total Waste')
    plt.title('Total Annual Waste per Province')
    plt.legend()
    plt.savefig('static/total_annual_waste.png')
    plt.close()


# In[4]:


# This Function is also to plot average annual waste per province
def plot_average_annual_waste(data):
    grouped_data = data.groupby(['Province']).mean().reset_index()
    plt.figure(figsize=(10, 6))
    plt.bar(grouped_data['Province'], grouped_data['TotalWaste'])
    
    plt.xlabel('Province')
    plt.ylabel('Average Annual Waste')
    plt.title('Average Annual Waste per Province')
    plt.savefig('static/average_annual_waste.png')
    plt.close()


# In[5]:


# We want to define the route for the homepage
# The homepage route reads the data, generates plots, and renders the HTML template.

@app.route('/')
def index():
    file_path ='C:/Users/DELL/Desktop/dataset.xlsx'
    data = read_data(file_path)
    plot_total_annual_waste(data)
    plot_average_annual_waste(data)
    return render_template('index.html')


# In[7]:


# We finally run the Flask application
if __name__ == '__main__':
    app.run(debug=True)


# In[ ]:




