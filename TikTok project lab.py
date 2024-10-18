#!/usr/bin/env python
# coding: utf-8

# # **TikTok Claims Analysis Project**


# In[1]:


# Import packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sns


# Then, load the dataset into a dataframe. Creating a dataframe will help you conduct data manipulation, exploratory data analysis (EDA), and statistical activities.
# 
# **Note:** As shown in this cell, the dataset has been automatically loaded in for you. You do not need to download the .csv file, or provide more code, in order to access the dataset and proceed with this lab. Please continue with this activity by completing the following instructions.

# In[2]:


# Load dataset into dataframe
data = pd.read_csv("tiktok_dataset.csv")


# ### **Task 2b. Understand the data - Inspect the data** 


# In[54]:


# Display and examine the first ten rows of the dataframe
data.head(10)


# In[52]:


# Get summary info
data.info()


# In[53]:


# Get summary statistics
data.describe()



# ### **Task 2c. Understand the data - Investigate the variables**

# In[3]:


# What are the different values for claim status and how many of each are in the data?
claim_status_counts = data['claim_status'].value_counts(dropna=False)
claim_status_counts


# In[3]:


# Data from the output
labels = ['Claim', 'Opinion', 'NaN']
sizes = [9608, 9476, 298]
colors = ['#c5b0d5', 'lightgreen', 'azure']
# Plotting the pie chart
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors)
plt.title('Distribution of Claim Status')
plt.show()


# Start by using Boolean masking to filter the data according to claim status, then calculate the mean and median view counts for each claim status.

# In[70]:


# What is the average view count of videos with "claim" status?

# Filter the dataset for videos with "claim" status
claim_videos = data[data['claim_status'] == 'claim']

# Calculate the mean and median view counts for "claim" status videos
mean_view_count_claim = claim_videos['video_view_count'].mean()
median_view_count_claim = claim_videos['video_view_count'].median()

# Display the results
print("Claim Status - Mean View Count:", mean_view_count_claim)
print("Claim Status - Median View Count:", median_view_count_claim)


# In[71]:


# What is the average view count of videos with "opinion" status?

# Filter the dataset for videos with "opinion" status
opinion_videos = data[data['claim_status'] == 'opinion']

# Calculate the mean and median view counts for "opinion" status videos
mean_view_count_opinion = opinion_videos['video_view_count'].mean()
median_view_count_opinion = opinion_videos['video_view_count'].median()

# Display the results
print("Opinion Status - Mean View Count:", mean_view_count_opinion)
print("Opinion Status - Median View Count:", median_view_count_opinion)


# In[4]:


# Data preparation
data2 = {
    'Status': ['Claim', 'Claim', 'Opinion', 'Opinion'],
    'Statistic': ['Mean', 'Median', 'Mean', 'Median'],
    'View Count': [501029.45, 501555.0, 4956.43, 4953.0]
}

df = pd.DataFrame(data2)

# Plotting a bar plot
plt.figure(figsize=(12, 5))
sns.barplot(x='Status', y='View Count', hue='Statistic', data=df, palette='PRGn')
plt.title('Mean vs Median View Counts by Claim Status')
plt.xlabel('Claim Status')
plt.ylabel('View Count')
# Set log scale and customize ticks
plt.yscale('log')
plt.yticks([1e3, 1e4, 1e5, 1e6], ['1K', '10K', '100K', '1M'])
plt.show()


# Use `groupby()` to calculate how many videos there are for each combination of categories of claim status and author ban status.

# In[35]:


# Get counts for each group combination of claim status and author ban status

# Group by 'claim_status' and 'author_ban_status', and then count the number of occurrences in each group
data.groupby(['claim_status', 'author_ban_status']).count()[['#']]


# In[5]:


# Sample data based on the output provided
data3 = {
    'claim_status': ['Claim', 'Claim', 'Opinion', 'Opinion'],
    'Author Ban Status': ['active', 'banned', 'active', 'banned'],
    'count': [6566, 1439, 8817, 196]
}

df = pd.DataFrame(data3)

# Plotting a bar plot
plt.figure(figsize=(12, 5))
sns.barplot(x='claim_status', y='count', hue='Author Ban Status', data=df, palette='coolwarm')
plt.title('Distribution of Author Ban Status by Claim Status')
plt.xlabel('Claim Status')
plt.ylabel('Video Count')
plt.show()


# Calculate the median video share count of each author ban status.

# In[39]:


# Group by 'author_ban_status' and calculate the median of 'video_share_count'
data.groupby(['author_ban_status']).agg(
    {'video_view_count': ['mean', 'median'],
     'video_like_count': ['mean', 'median'],
     'video_share_count': ['mean', 'median']})


# In[40]:


# What's the median video share count of each author ban status?
data.groupby(['author_ban_status']).median(numeric_only=True)[['video_share_count']]


# In[6]:


# Sample data based on the output provided
data4 = {
    'author_ban_status': ['Active', 'Banned'],
    'median_share_count': [437, 14468]
}

df = pd.DataFrame(data4)

# Plotting a bar plot
plt.figure(figsize=(8, 5))
sns.barplot(x='author_ban_status', y='median_share_count', data=df, palette='coolwarm')
plt.title('Median Video Share Counts by Author Ban Status')
plt.xlabel('Author Ban Status')
plt.ylabel('Median Video Share Count')
plt.show()


# Use `groupby()` to group the data by `author_ban_status`, then use `agg()` to get the count, mean, and median of each of the following columns:
# * `video_view_count`
# * `video_like_count`
# * `video_share_count`


# In[37]:


data.groupby(['author_ban_status']).agg(
    {'video_view_count': ['count', 'mean', 'median'],
     'video_like_count': ['count', 'mean', 'median'],
     'video_share_count': ['count', 'mean', 'median']
     })


# In[11]:


# Sample data based on the output provided
data5 = {
    'author_ban_status': ['Active', 'Banned'],
    'View Count: Mean': [215927.04, 445845.44],
    'View Count: Median': [8616.00, 448201.00],
    'Like Count: Mean': [71036.53, 153017.24],
    'Like Count: Median': [2222.00, 105573.00],
    'Share Count: Mean': [14111.47, 29998.94],
    'Share Count: Median': [437.00, 14468.00]
}

df = pd.DataFrame(data5)

# Melt the dataframe to long-form for easier plotting with seaborn
df_melted = df.melt(id_vars='author_ban_status', var_name='Metric', value_name='Value')

# Create a clustered bar plot
plt.figure(figsize=(12, 6))
sns.barplot(x='author_ban_status', y='Value', hue='Metric', data=df_melted, palette='PRGn')
plt.title('Comparison of Views, Likes, and Shares by Author Ban Status')
plt.xlabel('Author Ban Status')
plt.ylabel('Amount')
plt.xticks(rotation=45)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.show()


# In[12]:


# Filter the data for active authors and exclude 'under review' status
filtered_data = data[(data['author_ban_status'] != 'under review') & 
                     (data['author_ban_status'].isin(['active', 'banned']))]

# Set up the figure and axes
fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Set the color palette to coolwarm
sns.set_palette('PRGn')

# Video View Count Boxplot
sns.boxplot(x='author_ban_status', y='video_view_count', data=filtered_data, ax=axs[0])
axs[0].set_title('Video Views by Author Ban Status')
axs[0].set_ylabel('Video View Count')

# Video Like Count Boxplot
sns.boxplot(x='author_ban_status', y='video_like_count', data=filtered_data, ax=axs[1])
axs[1].set_title('Video Likes by Author Ban Status')
axs[1].set_ylabel('Video Like Count')

# Video Share Count Boxplot
sns.boxplot(x='author_ban_status', y='video_share_count', data=filtered_data, ax=axs[2])
axs[2].set_title('Video Shares by Author Ban Status')
axs[2].set_ylabel('Video Share Count')

# Adjust layout
plt.tight_layout()

# Show the plot
plt.show()


# Now, create three new columns to help better understand engagement rates:
# * `likes_per_view`: represents the number of likes divided by the number of views for each video
# * `comments_per_view`: represents the number of comments divided by the number of views for each video
# * `shares_per_view`: represents the number of shares divided by the number of views for each video

# In[9]:


# Create a likes_per_view column
data['likes_per_view'] = data['video_like_count'] / data['video_view_count']

# Create a comments_per_view column
data['comments_per_view'] = data['video_comment_count'] / data['video_view_count']

# Create a shares_per_view column
data['shares_per_view'] = data['video_share_count'] / data['video_view_count']


# Use `groupby()` to compile the information in each of the three newly created columns for each combination of categories of claim status and author ban status, then use `agg()` to calculate the count, the mean, and the median of each group.

# In[10]:


data.groupby(['claim_status', 'author_ban_status']).agg(
    {'likes_per_view': ['count', 'mean', 'median'],
     'comments_per_view': ['count', 'mean', 'median'],
     'shares_per_view': ['count', 'mean', 'median']})


# In[16]:


# Data preparation
data6 = {
    'Metric': ['Likes per View', 'Comments per View', 'Shares per View'],
    'Active Claim': [0.329542, 0.001393, 0.065456],
    'Banned Claim': [0.345071, 0.001377, 0.067893],
    'Active Opinion': [0.219744, 0.000517, 0.043729],
    'Banned Opinion': [0.206868, 0.000434, 0.040531]
}

df = pd.DataFrame(data6)
df.set_index('Metric', inplace=True)
df = df.T

# Plot
df.plot(kind='bar', figsize=(19, 6), colormap='viridis')
plt.title('Comparison of Engagement Metrics between Claim and Opinion Videos')
plt.xlabel('Author Ban Status')
plt.ylabel('Metric Values')
plt.xticks(rotation=45)
plt.legend(title='Metric', bbox_to_anchor=(1.05, 1), loc='upper left')
# Set log scale
plt.yscale('log')
# Customize y-axis ticks to quartiles
quartiles = [0.001, 0.01, 0.1, 1]
plt.yticks(quartiles, labels=[f'{q:.4f}' for q in quartiles])
plt.show()


#    Key Observations from the Data:
#    
#     Likes per View:
#     • Claim Videos: 
#     The mean likes_per_view ratio for claim videos is generally higher than for opinion videos across all author ban statuses. For example, active claim videos have a mean likes per view of 0.329542, while active opinion videos have a mean of 0.219744.
#     • Opinion Videos: 
#     Opinion videos have consistently lower likes_per_view ratios. This suggests that viewers are more likely to like claim videos than opinion videos, potentially because claim videos might provoke stronger reactions or resonate more with the audience.
#     
#     Comments per View:
#     • Claim Videos: 
#     The comments_per_view ratio is also slightly higher for claim videos. For example, active claim videos have a mean comments per view of 0.001393, while active opinion videos have a mean of 0.000517.
#     • Opinion Videos: 
#     Opinion videos tend to have fewer comments relative to views, suggesting that claim videos might drive more discussions or elicit stronger reactions that encourage viewers to leave comments.
#     
#     Shares per View:
#     • Claim Videos: 
#     The shares_per_view ratio for claim videos is generally higher across all author ban statuses. For instance, active claim videos have a mean shares per view of 0.065456, whereas active opinion videos have a mean of 0.043729.
#     • Opinion Videos: 
#     Similar to the other metrics, opinion videos have a lower share rate relative to their views, indicating that viewers are less likely to share opinion videos compared to claim videos. This might suggest that claim videos are perceived as more shareable, possibly because they present information or narratives that viewers find worth spreading.
#     
#     Summary of Differences:
#     • Engagement: 
#     Claim videos tend to have higher engagement rates (likes, comments, shares) relative to views compared to opinion videos across all categories of author ban status. This suggests that claim videos are more likely to provoke reactions from the audience.
#     • Shares: 
#     The higher shares_per_view ratio for claim videos indicates that they are more likely to be shared, which could contribute to their virality.
# 
#     Conclusion:
#     • Claim vs. Opinion: 
#     Claim videos generally see higher levels of engagement per view than opinion videos, indicating that they resonate more strongly with viewers. This could be due to the nature of claim content, which may provoke more reactions, discussions, and sharing than opinion-based content.
#     • Impact of Author Ban Status: 
#     The differences in engagement across banned, active, and under review authors are less pronounced, but claim videos consistently outperform opinion videos regardless of author status.
# 
# *   What percentage of the data is comprised of claims and what percentage is comprised of opinions?
#    
#    Of the 19,382 samples in this dataset, just under 50% are claims—9,608 of them.
# 
# *   What factors correlate with a video's claim status?
#       
#    Engagement level is strongly correlated with claim status. This should be a focus of further inquiry.
# 
# *   What factors correlate with a video's engagement level?
#    
#    Videos with banned authors have significantly higher engagement than videos with active authors. Videos with authors under review fall between these two categories in terms of engagement levels.
# 
