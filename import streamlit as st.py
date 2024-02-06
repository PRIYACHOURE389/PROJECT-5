import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data
@st.cache
def load_data():
    data = pd.read_csv(r"C:\Users\admin\Desktop\next hike\project-5\final_dat.csv")
    # Convert columns to appropriate datatypes, handle missing values, etc.
    # Example: Fill NaN for 'MSISDN/Number' with 'Unknown' or a similar placeholder if needed
    data.fillna({'MSISDN/Number': 'Unknown'}, inplace=True)
    return data

df = load_data()

st.title('Welcome to Telecom World')

# Navigation or Page Layout
options = ['User Overview Analysis', 'User Engagement Analysis', 'Experience Analytics', 'Satisfaction Analysis']
option = st.sidebar.radio('Which analysis would you like to see?', options)

if option == 'User Overview Analysis':
    st.header('User Overview Analysis')
    # Adjust based on relevant columns you have, for example showing the top rows
    st.dataframe(df.head())  # Display the first few rows to get an overview

elif option == 'User Engagement Analysis':
    st.header('User Engagement Analysis')
    # Make sure to include plots that are relevant to engagement, such as session duration
    fig, ax = plt.subplots()
    sns.scatterplot(x='Engagement_Score', y='Total Session Duration (s)', data=df)
    plt.xlabel('Engagement Score')
    plt.ylabel('Total Session Duration (s)')
    st.pyplot(fig)

elif option == 'Experience Analytics':
    st.header('Experience Analytics')
    # Plotting for Experience Analytics, adjust according to your dataframe columns
    fig, ax = plt.subplots()
    sns.scatterplot(x='Average_RTT', y='Average_Throughput', data=df)
    plt.xlabel('Average RTT')
    plt.ylabel('Average Throughput')
    st.pyplot(fig)

elif option == 'Satisfaction Analysis':
    st.header('Satisfaction Analysis')
    # Assuming 'Satisfaction_Score' is calculated and part of your df
    top_satisfied_customers = df.nlargest(10, 'Satisfaction_Score')
    st.write(top_satisfied_customers[['MSISDN/Number', 'Satisfaction_Score']])
    # Example plot for satisfaction analysis
    fig, ax = plt.subplots()
    sns.histplot(df['Satisfaction_Score'], bins=10, kde=True)
    plt.xlabel('Satisfaction Score')
    st.pyplot(fig)
