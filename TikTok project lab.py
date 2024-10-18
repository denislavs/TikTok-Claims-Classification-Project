#!/usr/bin/env python
# coding: utf-8

# # **TikTok Claims Analysis Project**
# **Course 2 - Get Started with Python**

# Welcome to the TikTok Project!
# 
# You have just started as a data professional at TikTok.
# 
# The team is still in the early stages of the project. You have received notice that TikTok's leadership team has approved the project proposal. To gain clear insights to prepare for a claims classification model, TikTok's provided data must be examined to begin the process of exploratory data analysis (EDA).
# 
# A notebook was structured and prepared to help you in this project. Please complete the following questions.

# # **Course 2 End-of-course project: Inspect and analyze data**
# 
# In this activity, you will examine data provided and prepare it for analysis.
# <br/>
# 
# **The purpose** of this project is to investigate and understand the data provided. This activity will:
# 
# 1.   Acquaint you with the data
# 
# 2.   Compile summary information about the data
# 
# 3.   Begin the process of EDA and reveal insights contained in the data
# 
# 4.   Prepare you for more in-depth EDA, hypothesis testing, and statistical analysis
# 
# **The goal** is to construct a dataframe in Python, perform a cursory inspection of the provided dataset, and inform TikTok data team members of your findings.
# <br/>
# *This activity has three parts:*
# 
# **Part 1:** Understand the situation
# * How can you best prepare to understand and organize the provided TikTok information?
# 
# **Part 2:** Understand the data
# 
# * Create a pandas dataframe for data learning and future exploratory data analysis (EDA) and statistical activities
# 
# * Compile summary information about the data to inform next steps
# 
# **Part 3:** Understand the variables
# 
# * Use insights from your examination of the summary data to guide deeper investigation into variables
# 
# <br/>
# 
# To complete the activity, follow the instructions and answer the questions below. Then, you will use your responses to these questions and the questions included in the Course 2 PACE Strategy Document to create an executive summary.
# 
# Be sure to complete this activity before moving on to Course 3. You can assess your work by comparing the results to a completed exemplar after completing the end-of-course project.

# # **Identify data types and compile summary information**
# 

# Throughout these project notebooks, you'll see references to the problem-solving framework PACE. The following notebook components are labeled with the respective PACE stage: Plan, Analyze, Construct, and Execute.
# 
# # **PACE stages**
# 
# <img src="images/Pace.png" width="100" height="100" align=left>
# 
#    *        [Plan](#scrollTo=psz51YkZVwtN&line=3&uniqifier=1)
#    *        [Analyze](#scrollTo=mA7Mz_SnI8km&line=4&uniqifier=1)
#    *        [Construct](#scrollTo=Lca9c8XON8lc&line=2&uniqifier=1)
#    *        [Execute](#scrollTo=401PgchTPr4E&line=2&uniqifier=1)

# <img src="images/Plan.png" width="100" height="100" align=left>
# 
# 
# ## **PACE: Plan**
# 
# Consider the questions in your PACE Strategy Document and those below to craft your response:
# 
# 

# ### **Task 1. Understand the situation**
# 
# *   How can you best prepare to understand and organize the provided information?
# 
# 
# *Begin by exploring your dataset and consider reviewing the Data Dictionary.*

# Step 1: Familiarize Yourself with the Data Dictionary
#     
#     Review the data dictionary to understand the purpose and description of each column. This provides context and helps in interpreting the data correctly.
# 
# Step 2: Load the Data into a Pandas DataFrame
#     
#     Read the dataset into a pandas DataFrame for ease of manipulation and analysis.
# 
# Step 3: Perform Initial Data Inspection
# 
#     Display the First Few Rows: Get a quick overview of the data.
#     Check Data Types: Ensure each column has the appropriate data type.
#     Check for Missing Values: Identify any columns with missing data.
#     Generate Descriptive Statistics: Summarize the central tendency, dispersion, and shape of the dataset’s distribution.
# 
# Step 4: Visualize Key Metrics
# 
#     Histograms: To understand the distribution of numerical variables.
#     Box Plots: To identify outliers and understand the spread of the data.
#     Scatter Plots: To explore relationships between numerical variables.
#     Correlation Heatmap: To visualize correlations between different metrics.
#     Bar Charts: To understand the distribution of categorical variables like verified_status.
# 
# Step 5: Clean and Prepare Data
# 
#     Handle Missing Values: Decide on strategies for dealing with missing data (e.g., imputation, removal).
#     Handle Outliers: Identify and decide how to handle outliers.
#     Feature Engineering: Create new features if necessary for better analysis and modeling.
# 
# Step 6: Document Findings
# 
#     Summarize Initial Observations: Document insights and observations from the initial data inspection.
#     Prepare for Further Analysis: Outline the next steps for more in-depth EDA, hypothesis testing, and statistical analysis.
#     

# <img src="images/Analyze.png" width="100" height="100" align=left>
# 
# ## **PACE: Analyze**
# 
# Consider the questions in your PACE Strategy Document to reflect on the Analyze stage.

# ### **Task 2a. Imports and data loading**
# 
# Start by importing the packages that you will need to load and explore the dataset. Make sure to use the following import statements:
# *   `import pandas as pd`
# 
# *   `import numpy as np`
# 

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
# 
# View and inspect summary information about the dataframe by **coding the following:**
# 
# 1. `data.head(10)`
# 2. `data.info()`
# 3. `data.describe()`
# 
# *Consider the following questions:*
# 
# **Question 1:** When reviewing the first few rows of the dataframe, what do you observe about the data? What does each row represent?
# 
# **Question 2:** When reviewing the `data.info()` output, what do you notice about the different variables? Are there any null values? Are all of the variables numeric? Does anything else stand out?
# 
# **Question 3:** When reviewing the `data.describe()` output, what do you notice about the distributions of each variable? Are there any questionable values? Does it seem that there are outlier values?
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 

# In[54]:


# Display and examine the first ten rows of the dataframe
data.head(10)


# In[52]:


# Get summary info
data.info()


# In[53]:


# Get summary statistics
data.describe()


# **Question 1**: When reviewing the first few rows of the dataframe, what do you observe about the data? What does each row represent?
# 
#     Structure: The dataframe contains several columns, each with different types of data.
#     Rows: Each row represents a unique video with associated metadata and engagement statistics.
# 
# **Question 2**: When reviewing the data.info() output, what do you notice about the different variables? Are there any null values? Are all of the variables numeric? Does anything else stand out?
# 
#         2.1 Variable Information:
#     • Number of entries: 19,382 rows.
#     • Number of columns: 12 columns.
#     
#         2.2 Data Types:
#         Numeric Variables:
#     • int64: 3 columns (#, video_id, video_duration_sec)
#     • float64: 5 columns (video_view_count, video_like_count, video_share_count, video_download_count, video_comment_count)
#     
#         Categorical/Non-numeric Variables:
#     • object: 4 columns (claim_status, video_transcription_text, verified_status, author_ban_status)
#     
#         2.3 Null Values:
#     • claim_status, video_transcription_text, and all the engagement metrics columns (video_view_count, video_like_count, etc.) contain some null values.
#     • Specifically, the claim_status, video_transcription_text, and engagement metrics have 19,084 non-null entries, meaning 
#     that about 298 entries have missing data in these columns.
#     
#         2.4 Key Observations:
#     • Missing Data: There are missing values in some columns, which may need to be addressed depending on the analysis.
#     • Mixed Data Types: The dataset includes both numeric (integers and floats) and non-numeric (text) variables, indicating    that the data includes both quantitative and qualitative information.
#     • Non-standard Columns: There is a column labeled # that seems to represent an index or identifier, but this could    potentially be redundant if the row index of the dataframe is sufficient.
# 
# **Question 3**: When reviewing the data.describe() output, what do you notice about the distributions of each variable? Are there any questionable values? Does it seem that there are outlier values?
# 
#         3.1 Distributions:
#         • Video Duration: 
#     The average video duration is 32.42 seconds, with a standard deviation of 16.22 seconds. The minimum duration is 5 seconds, and the maximum is 60 seconds. The distribution seems reasonable for video lengths.
#         • Video View Count: 
#     The average view count is 254,708.56, with a high standard deviation of 322,893.28, indicating a wide spread in the data. The minimum view count is 20, while the maximum is 9,999,817. This large range suggests a highly skewed distribution, with potential outliers at the upper end.
#         • Video Like Count: 
#     The average like count is 84,304.63, with a standard deviation of 133,420.55. The minimum value is 20, and the maximum is 657,830. Like the view count, this variable has a wide range and high standard deviation, indicating possible outliers.
#         • Video Share Count: 
#     The average share count is 16,735.25, with a standard deviation of 32,036.17. The minimum value is 0, and the maximum is 256,130. Again, the distribution shows a significant range with possible outliers.
#         • Video Download Count: 
#     The average download count is 1,049.43, with a standard deviation of 2,004.30. The minimum value is 0, and the maximum is 14,994. This wide spread also suggests potential outliers.
#         • Video Comment Count: 
#     The average comment count is 349.31, with a standard deviation of 799.64. The minimum value is 1, and the maximum is 9,599, indicating that there may be outliers in the comment count as well.
#     
#         3.2 Questionable Values:
#         • Zero Values: 
#     Some metrics like video_share_count, video_download_count, and video_comment_count have minimum values of 0, which could represent cases where videos had no engagement in those areas. These zeros might need to be verified, especially for very popular videos with high view and like counts, as having zero shares or comments might be unusual.
#         • Extremely High Values: 
#     The maximum values for video_view_count, video_like_count, and video_share_count seem disproportionately high compared to their means, indicating potential outliers or extreme cases in the dataset.
#     
#         3.3 Potential Outliers:
#     • The large standard deviations and the significant differences between the mean and maximum values across several columns suggest that outliers are present in the data. These outliers may represent highly popular or viral videos, which could skew  the overall statistics.
#     
#         3.4 Conclusion:
#     • The data distribution appears to be skewed with potential outliers, particularly in the video_view_count, video_like_count, and video_share_count variables. Additionally, some questionable zero values in the engagement metrics may need further investigation to confirm their validity.

# ### **Task 2c. Understand the data - Investigate the variables**
# 
# In this phase, you will begin to investigate the variables more closely to better understand them.
# 
# You know from the project proposal that the ultimate objective is to use machine learning to classify videos as either claims or opinions. A good first step towards understanding the data might therefore be examining the `claim_status` variable. Begin by determining how many videos there are for each different claim status.

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


# ##### **Question:** What do you notice about the values shown?
# 
#    Balanced Classes:
# 
#     • There are two primary categories: claim and opinion.
#     • The distribution between the two classes is relatively balanced, with 9,608 videos labeled as claim and 9,476 labeled as opinion. This is a positive sign for machine learning, as balanced classes generally lead to better performance when building classification models.
#     
#    Missing Values:
# 
#     • There are 298 NaN values in the claim_status column. These rows do not have a labeled status, which might need to be handled before training a model.
#     • Depending on the context and the nature of the missing data, you might consider:
#         • Removing these rows from the dataset.
#         • Imputing the missing values if there's enough information to do so.
#         • Investigating if the missing data is random or if there's a pattern that needs to be addressed.
#     
#    Next Steps:
# 
#     • Handling Missing Values: Decide on a strategy for dealing with the 298 missing values in the claim_status column.
#     • Further Exploration: Investigate other variables to see if there are patterns or correlations that might help in predicting the claim status.
#     • Model Training: Since the classes are balanced, you can proceed with developing a machine learning model to classify videos as either claim or opinion.

# Next, examine the engagement trends associated with each different claim status.
# 
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


# **Question:** What do you notice about the mean and media within each claim category?
# 
#    Observations from the Mean and Median View Counts:
#     
#     Claim Status:
#     • Mean View Count: 501,029.45
#     • Median View Count: 501,555.0
#     • The mean and median view counts for videos labeled as "claim" are very close to each other, indicating that the 
#     distribution of view counts for "claim" videos is likely symmetric or only slightly skewed. The similarity suggests that 
#     there are not many extreme outliers pulling the mean significantly away from the median.
#     
#     Opinion Status:
#     • Mean View Count: 4,956.43
#     • Median View Count: 4,953.0
#     • Similarly, the mean and median view counts for videos labeled as "opinion" are also very close, indicating that the 
#     distribution of view counts for "opinion" videos is relatively symmetric. This suggests a fairly consistent level of 
#     engagement across "opinion" videos, with no extreme outliers.
#     
#    Key Insights:
#     
#     • Symmetry in Distribution: In both the "claim" and "opinion" categories, the mean and median are quite close, implying that the view counts for both types of videos do not have extreme outliers significantly affecting the central tendency measures.
#     • Significant Difference Between Categories: There is a huge difference between the view counts of "claim" and "opinion" 
#     videos:
#         • "Claim" videos have an average view count in the hundreds of thousands, while "opinion" videos have an average 
#         view count of just under 5,000.
#         • This suggests that videos labeled as "claim" tend to receive significantly more attention and engagement than 
#         videos labeled as "opinion."
#     
#    Next Steps:
#     
#     • Further Analysis: It might be worth exploring other engagement metrics (like likes, shares, comments) to see if 
#     similar patterns emerge across different types of engagement.
#     • Outlier Analysis: Although the mean and median are close, it could still be valuable to plot the distributions of 
#     view counts for each category to visually confirm the absence of significant outliers.

# Now, examine trends associated with the ban status of the author.
# 
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


# **Question:** What do you notice about the number of claims videos with banned authors? Why might this relationship occur?
# 
#    Observations:
#    
#     • Claim Videos with Banned Authors: There are 1,439 claim videos where the author is banned, compared to only 196 opinion videos with banned authors.
#     • Higher Proportion in Claim Videos: The number of banned authors is significantly higher for claim videos than for opinion videos. In fact, the proportion of banned authors in claim videos is much larger compared to opinion videos.
#     
#    Possible Reasons for this Relationship:
#    
#     • Content Violation: Videos labeled as "claim" may often contain controversial or misleading information, leading to more frequent violations of platform policies. This could result in a higher number of bans for authors who create claim-based content.
#     • Misinformation Concerns: Platforms like TikTok may have stricter moderation policies for content that makes factual claims, especially if those claims are related to sensitive topics (e.g., health, politics, etc.). This could lead to more frequent bans for authors of claim videos, as they might be perceived as spreading misinformation or violating community guidelines.
#     • Engagement and Scrutiny: As noted earlier, claim videos tend to have higher view counts compared to opinion videos. Higher engagement might lead to increased scrutiny from both the platform and users, resulting in more reports and potential bans for content that is flagged as problematic.
#     • Platform Policy Focus: Platforms may focus more on regulating content that makes factual claims, which can have a more significant impact on the community compared to opinion content. This could explain the higher number of bans associated with claim videos.
# 
#    Conclusion:
#    
#     • The higher number of banned authors for claim videos might be due to the nature of the content, which could be more likely to violate platform rules, especially if the claims made are false or misleading.
#     • Further analysis could involve examining the content of these claim videos to understand more about the types of claims being made and how they correlate with the bans.

# Continue investigating engagement levels, now focusing on `author_ban_status`.
# 
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


# **Question:** What do you notice about the share count of banned authors, compared to that of active authors? Explore this in more depth.
# 
#    Observations:
#     
#     • Banned Authors: The median video share count for banned authors is 14,468.
#     • Active Authors: The median video share count for active authors is significantly lower, at 437.
#     
#    Insights:
#     
#     • Higher Engagement for Banned Authors: Videos from banned authors have a much higher median share count compared to videos from active authors. This suggests that content from banned authors tends to generate significantly more engagement in terms of shares.
#     • Potential Controversial Content: The higher share count for banned authors may indicate that their content is more controversial or sensational, leading to increased sharing. This type of content might be more likely to violate platform rules, resulting in the authors being banned.
#     • Viral Nature: Content that is heavily shared might have a higher likelihood of being flagged and reviewed by the platform, which could explain why authors of such content face bans.
#     
#    Conclusion:
#     
#     • The large difference in share counts suggests that content from banned authors may have viral characteristics, making it more likely to spread quickly and attract platform attention, potentially leading to their ban. Further investigation into the nature of this content could provide deeper insights into the relationship between share counts and author bans.

# Use `groupby()` to group the data by `author_ban_status`, then use `agg()` to get the count, mean, and median of each of the following columns:
# * `video_view_count`
# * `video_like_count`
# * `video_share_count`
# 
# Remember, the argument for the `agg()` function is a dictionary whose keys are columns. The values for each column are a list of the calculations you want to perform.

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


# **Question:** What do you notice about the number of views, likes, and shares for banned authors compared to active authors?
# 
#    Observations:
#     
#     Video View Count:
#     • Banned Authors: The mean view count for videos from banned authors is 445,845.44, and the median is 448,201.00.
#     • Active Authors: The mean view count for videos from active authors is 215,927.04, and the median is 8,616.00.
#     • Key Insight: Banned authors have significantly higher mean and median view counts compared to active authors. The large gap between the mean and median for active authors suggests that a small number of videos may be driving up the mean, while most videos have much lower view counts.
#     
#     Video Like Count:
#     • Banned Authors: The mean like count is 153,017.24, and the median is 105,573.00.
#     • Active Authors: The mean like count is 71,036.53, and the median is 2,222.00.
#     • Key Insight: Banned authors' videos receive significantly more likes on average than those of active authors. The disparity between the mean and median for active authors again suggests that a few videos receive many likes, while the majority receive fewer likes.
#     
#     Video Share Count:
#     • Banned Authors: The mean share count is 29,998.94, and the median is 14,468.00.
#     • Active Authors: The mean share count is 14,111.47, and the median is 437.00.
#     • Key Insight: Similar to the views and likes, banned authors' videos have significantly higher share counts compared to active authors. The median share count for active authors is notably low, indicating that most of their videos are shared much less frequently.
#     
#    Summary:
#     
#     • Higher Engagement for Banned Authors: Across all three metrics—views, likes, and shares—banned authors' videos exhibit significantly higher levels of engagement compared to active authors. This pattern suggests that content produced by banned authors is more engaging, possibly because it is more sensational or controversial, which may contribute to its virality and, ultimately, the banning of the author.
#     • Potential Outliers: The large difference between the mean and median for active authors, particularly in views and shares, suggests that a small number of videos are outliers, receiving far more engagement than the typical video from an active author.
#     
#     This pattern of higher engagement for banned authors could be an important factor to consider in future analyses, particularly in understanding the relationship between content virality and platform moderation actions.

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


# **Question:**
# How does the data for claim videos and opinion videos compare or differ? Consider views, comments, likes, and shares.
# 
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

# <img src="images/Construct.png" width="100" height="100" align=left>
# 
# ## **PACE: Construct**
# 
# **Note**: The Construct stage does not apply to this workflow. The PACE framework can be adapted to fit the specific requirements of any project.
# 
# 
# 

# <img src="images/Execute.png" width="100" height="100" align=left>
# 
# ## **PACE: Execute**
# 
# Consider the questions in your PACE Strategy Document and those below to craft your response.

# ### **Given your efforts, what can you summarize for Rosie Mae Bradshaw and the TikTok data team?**
# 
# *Note for Learners: Your answer should address TikTok's request for a summary that covers the following points:*
# 
# *   What percentage of the data is comprised of claims and what percentage is comprised of opinions?
#    
#    
#    Of the 19,382 samples in this dataset, just under 50% are claims—9,608 of them.
# 
# 
# *   What factors correlate with a video's claim status?
#    
#    
#    Engagement level is strongly correlated with claim status. This should be a focus of further inquiry.
# 
# *   What factors correlate with a video's engagement level?
#    
#    
#    Videos with banned authors have significantly higher engagement than videos with active authors. Videos with authors under review fall between these two categories in terms of engagement levels.
# 

# **Congratulations!** You've completed this lab. However, you may not notice a green check mark next to this item on Coursera's platform. Please continue your progress regardless of the check mark. Just click on the "save" icon at the top of this notebook to ensure your work has been logged.
