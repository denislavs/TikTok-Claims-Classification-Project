# TikTok Claims Classification Analysis
______________________

## 1. Introduction 

This project is part of the Google Advanced Data Analytics Course on Coursera, focusing on analyzing TikTok video data to understand the relationship between video content (whether labeled as a "claim" or "opinion") and the corresponding engagement levels (such as views, likes, and shares). The primary objective of this analysis is to uncover patterns in user behavior, engagement, and author status that may influence video performance, particularly regarding banned authors. The project showcases a comprehensive exploratory data analysis (EDA), insights from visualizations, and key findings that can drive platform decision-making.  

The analysis explores key questions such as:  
• What are the key differences between claim videos and opinion videos in terms of engagement?  
• How does an author's ban status affect the engagement of their videos?  
• What patterns emerge between engagement metrics like views, likes, shares, and comments across various categories?  

## 2. Methodology

**Data Source**  
The dataset used in this analysis was provided through the Google Advanced Data Analytics Course on Coursera. It consists of TikTok videos, including associated metadata such as video view counts, like counts, share counts, claim status (claim vs. opinion), author ban status, and video transcriptions. There are 19,382 rows and 12 columns in the dataset, containing both numerical and categorical data.  

**Tools and Libraries**  
• Python: For data manipulation and analysis.  
• Pandas: For handling and exploring data.  
• Matplotlib and Seaborn: For visualizing trends and distributions.  
• Jupyter Notebook: For conducting interactive analysis.  

**Analytical Approach**  
• Data Inspection and Cleaning:  
Initial inspection of missing data, data types, and distributions was performed. Key focus areas include: Missing values in claim status, numerical engagement metrics, and categorical variables like author ban status.  
• Exploratory Data Analysis (EDA):  
Descriptive statistics and visualizations were used to investigate the distribution of views, likes, shares, and comments by claim status and author ban status. Outliers and skewness in variables such as views, likes, and shares were identified and handled appropriately.  
• Visualization:  
Various visualizations were created to represent the relationships between claim status, engagement metrics, and author ban status. These visualizations reveal patterns in how different content types (claim vs. opinion) perform and the impact of an author’s ban status on engagement.  
  
## 3. Findings 

The TikTok Claims Classification Analysis uncovered several important insights:  
• The dataset contains a relatively balanced split between videos labeled as claims and opinions.  
• Engagement (views, likes, shares) is significantly higher for claim videos compared to opinion videos.  
• Videos from banned authors tend to have disproportionately higher engagement compared to those from active authors.  

**3.1. Distribution of Claim Status**  

![output_20_0](https://github.com/user-attachments/assets/6a118ca6-884a-4805-a3db-f43a3e62b84d)  
The dataset shows a near-even distribution of videos, with 49.6% labeled as claims, 48.9% as opinions, and 1.5% missing claim status.    

**3.2. Mean vs. Median View Counts by Claim Status**  

![output_25_0](https://github.com/user-attachments/assets/8a65f337-5f34-4b25-9d70-9e91ee315f1e)  
**Claims**: Mean and median view counts are very close (~500k), indicating a relatively symmetric distribution for claim videos.  
**Opinions**: Mean and median view counts are just under 5k, suggesting significantly lower engagement for opinion videos compared to claims.  

**3.3. Distribution of Author Ban Status by Claim Status**  

![output_29_0](https://github.com/user-attachments/assets/b250644b-3273-4077-ab15-17615385abc4)  
The chart shows that among claim videos, 1,439 were created by banned authors and 8,169 by active authors, while for opinion videos, 196 were from banned authors and 9,280 from active authors, indicating a much higher proportion of banned authors associated with claim videos compared to opinion videos.   

**3.4. Median Video Share Counts by Author Ban Status**  

![output_34_0](https://github.com/user-attachments/assets/73126993-2de9-4d7a-a9db-4a07025bac98)  
Videos from banned authors have a much higher median share count (~14,468) compared to videos from active authors (~437). This suggests banned authors' content is more likely to be shared, potentially because of its controversial or viral nature.  

**3.5. Comparison of Views, Likes, and Shares by Author Ban Status**  

![output_38_0](https://github.com/user-attachments/assets/49c861f7-52e0-49ce-8326-3407e46f56c6)  
Banned authors' videos receive higher engagement across all metrics (views, likes, and shares) compared to active authors. This is evident in the bar chart showing significantly higher mean and median counts for banned authors.  

**3.6. Video Views, Likes, Shares by Author Ban Status**  

![output_39_0](https://github.com/user-attachments/assets/462abe63-ada4-4b2b-8a06-a1de84e74f42)  
Boxplots for views, likes, and shares clearly show that videos from banned authors outperform those from active authors, with banned authors' videos having a higher median view count (approximately 450,000 vs. 220,000), a higher median like count (around 100,000 vs. 70,000), and a higher median share count (about 15,000 vs. 500). The larger spread in all three metrics for banned authors further highlights the wider variability in their engagement.

**3.7. Comparison of Engagement Metrics between Claim and Opinion Videos**  

![output_45_0](https://github.com/user-attachments/assets/b0df729e-d8e6-4d61-9afd-cc9c6f2522f1)  
Claim videos consistently outperform opinion videos in key engagement metrics, with active claim videos having a higher likes-per-view ratio (0.33 vs. 0.22), comments-per-view ratio (0.00139 vs. 0.00052), and shares-per-view ratio (0.065 vs. 0.044). This pattern is similar for banned authors, indicating that claim videos generate stronger reactions across all metrics.  

### **Key Insights**

• **Higher Engagement for Claims**:   
Videos labeled as "claim" receive significantly higher engagement compared to "opinion" videos. On average, claim videos have a mean view count of 501,029 compared to 4,956 for opinion videos, and a mean likes-per-view ratio of 0.33 for claims versus 0.22 for opinions.  
• **Banned Authors' Impact**:   
Videos from banned authors show much higher engagement than those from active authors. Banned authors’ videos have a mean view count of 445,845, while active authors' videos have a mean of 215,927. Banned authors also have a median share count of 14,468, compared to just 437 for active authors, indicating that their content is more widely shared.  
• **Engagement Consistency**:   
The distribution of engagement metrics (views, likes, shares) for claim videos is relatively symmetric, with the mean and median being very close. For instance, the median view count for claim videos is 501,555, closely matching the mean. In contrast, opinion videos show consistently lower engagement, with the median view count at 4,953.  
• **Content Moderation and Viral Nature**:   
Claim videos are more likely to be associated with banned authors, with 1,439 claim videos created by banned authors compared to only 196 opinion videos. This suggests that claim content is more prone to violations or controversy, potentially explaining the higher engagement from these videos.  

## 4. Business Impact

The findings from this analysis provide several actionable insights for platforms like TikTok, particularly regarding content moderation, user engagement strategies, and policy enforcement:  

• **Content Moderation Strategy**:   
The higher engagement levels for claim videos, especially from banned authors, suggest that claims are often more provocative or controversial. This highlights the importance of accurate content moderation to mitigate misinformation.    
• **User Engagement**:   
Claim videos tend to drive significantly higher user engagement compared to opinion videos. Platforms could capitalize on this by promoting fact-based content, but with robust verification processes to avoid spreading misinformation.    
• **Author Bans and Viral Content**:   
Banned authors consistently have higher engagement metrics, suggesting that controversial content, whether true or false, tends to go viral. Platforms should balance allowing viral content while enforcing community guidelines.    

## 5. Conclusion  

The TikTok Claims Classification Analysis project, conducted as part of the Google Advanced Data Analytics Course on Coursera, effectively uncovered key trends in video content and engagement on TikTok, particularly regarding the impact of claim-based videos and the ban status of authors. Through comprehensive data inspection, exploratory data analysis, and the creation of insightful visualizations, this analysis provides valuable insights into how content type and user moderation policies can affect audience engagement.

### Key Findings
This analysis revealed several critical patterns that differentiate between claim videos and opinion videos, as well as between banned and active authors:  
• **Videos categorized as "claim"** consistently garnered more views, likes, shares, and comments compared to "opinion" videos. This suggests that claim-based content resonates more strongly with users, potentially due to its informative or provocative nature.  
• **Videos from banned authors** exhibited significantly higher engagement across all metrics—views, likes, and shares—than those from active authors. This may indicate that content created by banned authors tends to be more controversial or sensational, which can drive virality but also lead to increased scrutiny and moderation.  
• The **distribution of engagement metrics for claim videos** (mean vs. median) was relatively symmetric, indicating that these videos tend to perform consistently well without being dominated by a few outliers. In contrast, opinion videos had significantly lower engagement overall.   

### Future Recommendations  
• Further analysis could explore predictive models to identify patterns that lead to videos being flagged or authors being banned.  
• A deeper dive into content types and the nature of claims (e.g., health-related, political) could help refine content moderation policies.  

These insights can inform data-driven content moderation and engagement strategies, enabling TikTok to enhance user interactions, improve platform safety, and optimize overall user experience.
