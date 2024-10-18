# TikTok Claims Classification Analysis
______________________

## 1. Introduction 

This project is focused on analyzing TikTok video data to understand the relationship between video content (whether labeled as a "claim" or "opinion") and the corresponding engagement levels (such as views, likes, and shares). The primary objective of this analysis is to uncover patterns in user behavior, engagement, and author status that may influence video performance, particularly regarding banned authors.  

The analysis explores key questions such as:  
• What are the key differences between claim videos and opinion videos in terms of engagement?  
• How does an author's ban status affect the engagement of their videos?  
• What patterns emerge between engagement metrics like views, likes, shares, and comments across various categories?  
  
The project showcases a comprehensive exploratory data analysis (EDA), insights from visualizations, and key findings that can drive platform decision-making.  

## 2. Methodology

**Data Source**  
The dataset used for this analysis consists of TikTok videos, including associated metadata such as video view counts, like counts, share counts, claim status (claim vs. opinion), author ban status, and video transcriptions. It has 19,382 rows and 12 columns, containing both numerical and categorical data.  

**Tools and Libraries**  
• Python: For data manipulation and analysis.  
• Pandas: For handling and exploring data.  
• Matplotlib: For visualizing trends and distributions.  
• Jupyter Notebook: For conducting interactive analysis.  

**Analytical Approach**  
• Data Inspection and Cleaning:  
Initial inspection of missing data, data types, and distributions was performed. Key focus areas include: Missing values in claim status, numerical engagement metrics, and categorical variables like author ban status.  
• Exploratory Data Analysis (EDA):  
Descriptive statistics and visualizations were used to investigate the distribution of views, likes, shares, and comments by claim status and author ban status. Outliers and skewness in variables such as views, likes, and shares were identified and handled appropriately.  
• Visualization:  
Various visualizations were created to represent the relationships between claim status, engagement metrics, and author ban status. These visualizations reveal patterns in how different content types (claim vs. opinion) perform and the impact of an author’s ban status on engagement.  
  
## 3. Findings 



## 4. Business Impact

The findings from this analysis provide several actionable insights for platforms like TikTok, particularly regarding content moderation, user engagement strategies, and policy enforcement:  
• **Content Moderation Strategy**:   
The higher engagement levels for claim videos, especially from banned authors, suggest that claims are often more provocative or controversial. This highlights the importance of accurate content moderation to mitigate misinformation.    
• **User Engagement**:   
Claim videos tend to drive significantly higher user engagement compared to opinion videos. Platforms could capitalize on this by promoting fact-based content, but with robust verification processes to avoid spreading misinformation.    
• **Author Bans and Viral Content**:   
Banned authors consistently have higher engagement metrics, suggesting that controversial content, whether true or false, tends to go viral. Platforms should balance allowing viral content while enforcing community guidelines.    

## 5. Conclusion  

This analysis of TikTok's claim and opinion video data provided several valuable insights into how content type and author ban status influence user engagement. The project revealed that:    
• **Claim videos** receive significantly higher engagement than opinion videos, making them a key driver of user interaction on the platform.  
• **Banned authors** tend to produce more engaging content in terms of views, likes, and shares, but this also implies a potential risk of spreading controversial or harmful information.  

### Future Recommendations  
• Further analysis could explore predictive models to identify patterns that lead to videos being flagged or authors being banned.  
• A deeper dive into content types and the nature of claims (e.g., health-related, political) could help refine content moderation policies.  

By thoroughly inspecting and cleaning the dataset, conducting EDA, and visualizing key trends, this project demonstrates solid data analytics skills, suitable for addressing complex business problems, driving decision-making, and improving platform strategy.  
