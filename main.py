#!/usr/bin/python3
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Load the CSV file into our pandas DataFrame
df = pd.read_csv('smoking.csv')

def line_chart_display():
    """
    This function counts the number of smokers in each group and 
    creates a line chart with for different age group.
    """
    # Group data by age and count the number of smokers
    age_group_counts = df[df['smoke'] == 'Yes'].groupby('age')['smoke'].count()

    # Create the first line chart
    plt.figure(figsize=(10, 6))
    plt.plot(age_group_counts.index, age_group_counts, label="Number of Smokers", color='blue', marker='o')
    plt.title("Number of Smokers by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Number of Smokers")
    plt.legend()
    plt.savefig('figure_1.png')
    return

def pie_chart_diplay():
    """
    This function creates a pie chart with different colors for each smoking group. 
    """
    # Count the number of 'Yes' and 'No' in the 'smoke' column
    smoke_counts = df['smoke'].value_counts()

    # Create a pie chart
    labels = ['Yes', 'No']
    sizes = [smoke_counts.get('Yes', 0), smoke_counts.get('No', 0)]
    colors = ['#ff9999', '#66b3ff']
    explode = (0.1, 0)  # To explode the 'Yes' slice

    plt.figure(figsize=(10, 6))
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85, explode=explode)

    # Add a title
    plt.title("Smoking Status")

    # Add legends
    plt.legend(labels, title="Smoke Status", loc="upper left")

    # Show the chart
    plt.axis('equal')
    plt.show()
    plt.savefig('figure_2.png')
    return 

def bar_plot():
    """
    This function groups the data by age, counts the number of smokers in each group,
    and creates a bar chart with different colors for each age group. 
    """
    # Define colors
    colors = ['red', 'blue', 'green', 'purple', 'orange']
    # Define age groups
    age_groups = ['Under 30', '30-39', '40-49', '50-59', '60 and over']

    # Categorize age values into the specified age groups
    df['age_group'] = pd.cut(df['age'], bins=[0, 30, 40, 50, 60, df['age'].max()], labels=age_groups, right=False)

    # Filter data for smokers
    smokers_by_age = df[df['smoke'] == 'Yes']

    # Create a bar chart
    plt.figure(figsize=(10, 6))
    age_group_counts = smokers_by_age['age_group'].value_counts()[age_groups]
    bars = plt.bar(age_groups, age_group_counts)

    # Add color labels and legends
    for i, bar in enumerate(bars):
        bar.set_color(colors[i])

    legend_labels = age_groups
    legend_handles = [plt.Rectangle((0, 0), 1, 1, color=colors[i]) for i in range(len(age_groups))]

    # Adds a legend to label the age groups with their respective colors. 
    plt.legend(legend_handles, legend_labels, title="Age Groups")

    plt.title("Age of Smokers by Age Group")
    plt.xlabel("Age Group")
    plt.ylabel("Number of Smokers")
    plt.show()
    plt.savefig('figure_3.png')


if __name__ == "__main__":

    line_chart_display()
    pie_chart_diplay()
    bar_plot()