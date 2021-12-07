# -Business-Intelligence-1641
Introduction: 
In the previous article, we presented our Bi-influenced project, step by step, in order to add BI to the project. In this review, we will show the board of directors the opportunity to apply business intelligence to the existing business processes of the organization. I hope we can come up with some helpful information. This report complies with the criteria of the assignment. 
	I. 	Overview about BI 
1. What is BI? 
According to (Albert Nogués, Juan Valladares, 2017) : “Business intelligence is a collection of theories, methodologies, architectures, and technologies that translate raw data for business purposes into relevant and useful information.” 
![image](https://user-images.githubusercontent.com/94780400/145019918-d036943d-b88c-4222-9d9c-4d1d66140e05.png)
Figure 1:BI(https://o7planning.org/10355/what-is-business-intelligence) 
2. Example for applying BI 
A unified perspective on restaurant operations was created by Chipotle 
Company: Chipotle 
Problem: Disparate sources of data stopped teams from seeing a single vision of restaurants. 
Solution: With more than 2,400 outlets around the world, Chipotle Mexican Grill is an American restaurant chain. For a new, self-service BI network, Chipotle has retired its conventional BI solution. This allowed them to establish a centralized view of activities so that they could control the operational effectiveness of restaurants on a national scale. The pace of report delivery for strategic initiatives has tripled from quarterly to monthly and saved thousands of hours, now that workers have more access to data. "This was the ticket for taking all metrics and understanding to the next level," explained Business Intelligence Director Zach Sippy. 
3. BI techniques: 
Collection techniques 
Data cleaning: The method of identifying and resolving data quality problems is data cleansing. Usually, it requires steps like. Fix Structural Defects, Filter, Delete unnecessary findings. Unwanted Outliers, Incomplete Details Handle. Labeling the Class ( categorical and numerical). A set of information that is split into groups is categorical data. 
For example: Education level, household income numerical data, for example, is a type of data represented in numbers rather than expressing the natural language. 
Analysis techniques: The assessment is a method of data analysis that has existed in the past. This approach is used to understand how and how everything arises from experience. Data analysis may be used in different ways, such as conducting analysis, such as descriptive analysis, analysis of discovery, deductive analysis, analysis of prediction, and valuable data insights. 
For example: I need to compare the number of cars sold by the Mercedes and BMW brands in the Vietnamese market over the last two years. I have to evaluate the data on car sales in the past and specifically the last 2 years of Mercedes and BMW brands from which I can achieve the results in order to get this result. 
![image](https://user-images.githubusercontent.com/94780400/145019959-e638bd78-09df-4c23-9711-89fb52b2949c.png)
Figure 2:Analysis techniques (https://www.educba.com/data-analysis-techniques/) 
Reporting is a static document containing information in the form of tables or text. These data can be viewed on charts used for the visualization of individual data and related data. A more holistic view of an organization or a company may be provided by studies. Database review is a method used in databases that use SQL in order to evaluate how output queries can be further optimized. The dashboard is the method used for visualizing information that can be personalized and structured to view unique information and information. These tools turn information into versatile and vivid data. More precisely, the Dashboard transforms digital data into chart data, making it simple for users to interpret it specifically. 
Analytic techniques 
Analysis of regression is a mathematical method used to find variables' relationships. We call it quick regression when there is just one independent and dependent variable, and we call multiple regression when there are several independent variables. 
For example: Via ads, businesses want to boost online sales. The relationship between money spent on ads and sales is of interest to companies. Specifically, as the advertisement money rises by 10 percent, they want to know the projected income will rise by what percentage relative to the present. 
Machine learning is a small field of computer science that, on the basis of feedback, has the ability to learn by itself. Machine learning, in other words, provides perfect input-based data output. 
Data Warehouse: A data warehouse is a system of data storage that stores vast quantities of data for subsequent processing and research use. You may think of it as a big warehouse where their data is unloaded by trucks (i.e. source data). The information is then sorted into rows of well-organized shelves and rows that make it easy to find exactly what you are searching for later on. When all the analytical sources revolve around the data warehouse, it is regarded as the center of business intelligence (BI). 
Pros: A quick, well-managed data warehouse that uses the existing standard SQL and BI instruments to analyze data. A simple and cost-effective tool that allows complex analytical queries to be run using intelligent query optimization functionality. By using column storage on high-performance disks and massively parallel processing concepts, it manages big data. Allows the user to run queries directly on Amazon S3 against unstructured data. No need for transformation and loading. Depending on data, it scales query computing power automatically. 
 
 
Conclusion: Advanced analytics and collections of improved results, Increased creativity and perspectives unique to the industry. The maximum big data value, Profitability, Extreme Performance & consolidation. 
Data mining 
In big data sets, data mining is searching for secret, true, and potentially useful patterns. Data Mining deals with the discovery of unsuspected/previously unknown data relationships. It is a multi-disciplinary expertise that utilizes machine learning, statistics, AI and technology for databases. For marketing, fraud detection, and scientific exploration, etc., insights gained through data mining can be used.  
![image](https://user-images.githubusercontent.com/94780400/145019981-6b3e3858-e139-4462-a430-fb21c42b4786.png)
Figure 3:(https://data-flair.training/blogs/data-mining-and-data-science/) 
 
Advantage: 
-	Predicting future patterns is useful 
-	It signifies customer habits 
-	Helps in decision making 
-	Increase company revenue 
-	Quick fraud detection 
• Examples: Tableau
![image](https://user-images.githubusercontent.com/94780400/145020009-01a41b2c-98c1-439f-b209-37badb526929.png)
Figure 4:(https://blog.surveybot.io/connect-tableau-surveybot/) 
4. Business Intelligence tools 
Programming tools 
For data analysis, Python programming is strong. 
Pros:  
-	Not complex in declare 
-	Code quickly - 	Easy to learn 
R programming: 
![image](https://user-images.githubusercontent.com/94780400/145020040-15828126-de50-460f-95bc-52b1bcefcac0.png)
![image](https://user-images.githubusercontent.com/94780400/145020058-7c70d8e0-f930-474b-b56f-d38b3fcd056b.png)
The leading analytics method commonly used in data modeling. On different platforms, running (UNIX, Windows and MacOS). For almost any data science mission, from data manipulation and automation to ad-hoc analysis and dataset exploration, either language is sufficient. For different purposes, users may use both languages, such as performing early-stage data analysis and exploration in R, then switching to Python when it is time to ship a data product. Python is used by programmers who want to explore the interpretation of data or apply statistical methods. It has the potential to be a single tool that integrates with each workflow component. R does not require any programming skills for computers. Users are also very different, and data collection in industries has also been used in recent years. 
	II. 	Demonstration about BI 
1. Dataset  
The dataset can be viewed directly from the hotel on the link: https://www.kaggle.com/jessemostipak/hotel-bookingdemandx 
Clean specifications for the tutor's data: 
-	Remove the columns for 'company' and 'agent.' 
-	In the 'country' column, change the abbreviated name to the lowercase name. 
-	In the 'meal' column, change the abbreviated name to the lowercase name. 
-	Merge 2 "children" and "baby" columns into a single column with the sum of 2 columns as the weight. 
-	Merge the 2 "arrival-date-year" and "arrival-date-month" columns into one column and concatenate the 2 column material. Process Clean data 
![image](https://user-images.githubusercontent.com/94780400/145020086-302e9a74-df38-4725-b293-28a60201ae23.png)
Figure 6:Code cleaning data 
Here are the 2 full name dictionaries for the "country" column and "meal" column. 
![image](https://user-images.githubusercontent.com/94780400/145020113-6f93b361-6c35-4277-badc-5eab04e379bb.png)
Figure 7Code cleaning data(2) 
Header row elimination involves the column name and assigns it to the header. 
![image](https://user-images.githubusercontent.com/94780400/145020135-d8984587-2b78-4609-8223-df2a0dab6dcc.png)
Figure 8Code cleaning data(3) 
"Create a function that can be passed to sub-functions, called "clean data. 
![image](https://user-images.githubusercontent.com/94780400/145020150-e6adb533-b191-4fc9-9026-95ebfc1dc4af.png)
Figure 9Code cleaning data 
-	"Remove agent company function." Remove the columns for "agent" and "company." 
-	Clean Country feature. Adjust the name of the country bypassing the column "country" through the dictionary "country dict" - 	"Meal" feature. By bypassing the "meal" column via the "meal dict" dictionary, change the meal name. 
-	The 'baby' feature. Combining 2 "kids" and "baby" columns. And then the new column gets a two-column sum. 
-	"time" feature. The combination of two "year" and "month" columns. 
![image](https://user-images.githubusercontent.com/94780400/145020194-fc61d1ed-f8de-4abb-b8f7-97626170583a.png)
![image](https://user-images.githubusercontent.com/94780400/145020205-a605d8df-276e-42a8-a882-1dfcd54f295c.png)
. Design dashboard 
![image](https://user-images.githubusercontent.com/94780400/145020230-007be59c-dd85-40fc-a2a8-e1f1d8131304.png)
Figure 12Number of tourists by month 
This is the graph which shows the number of customers ordering during the months of the hotel. In comparison, the real number of bookings is blue and the number of cancelled guests is green. Through the map, we can see that there are 2 peak months in July and 
August. With a sudden spike in tourist numbers. The three months with record low arrivals were November, December, and January. Only half of what is normal. Cancellation rates vary from 30-40% . As compared to other hotels, this is a reasonably high cancellation rate. 
![image](https://user-images.githubusercontent.com/94780400/145020247-bda9744c-e56a-4ffc-a15d-8a9c26c83046.png)
Figure 13Amount of nights in a hotel for customers on weekdays 
Through the charts, we could see. On weekdays, the average guest stays for 1 to 3 days. The rates are: 1 night - 25.62%, 2 nights - 28.63%, 3 nights - 18.56% . Also very high is the number of guests staying for 4 and 5 nights. 7.76 percent and 8.97 percent respectively, respectively. 
![image](https://user-images.githubusercontent.com/94780400/145020278-08081c34-6d1d-4553-9df1-5082cb9a846c.png)
Figure 14number of guests staying for the weekend 
We can see that the average of 44.15 percent for no one in the room at the weekend is really high. For a hotel, this is an alarming amount. The prices for one and two night stays are high. 25.74 percent, respectively, and 27.28 percent. 
![image](https://user-images.githubusercontent.com/94780400/145020307-b7b6a08f-4ff8-4b9e-a1bf-10b40c70eba4.png)
Figure 15Combining figure 13 and 14 
We may conclude via these 2 maps. The rate of hotel guests is from 1 to 3 days. A high proportion of over 44 percent accounts for the number of tourists not staying on weekends . Through this, we make the option to provide several deals for guests who want to stay at the hotel for 3 to 5 days, room rates will also decrease on weekends to decrease availability and raise revenue. 
![image](https://user-images.githubusercontent.com/94780400/145020351-7e1be5e9-7cbf-4361-997a-6bd6e822253a.png)
Figure 16Dashboard 1 
We can see it through the dashboard. The client divisions of the organization are singles, business people, couples, and individuals who enjoy the experience. For families with children, our hotel is not suitable. We are, therefore, making a strategic decision. Customer groups are not going to target families. The philosophy of the hotel would therefore be geared towards serving the following services: visitors' experience or relaxation. In addition, July and August are several clients' months. Tactical options we make use of. Employ and train more workers before the peak opportunity arrives. 
![image](https://user-images.githubusercontent.com/94780400/145020373-4a5998de-da0c-4ce2-99f5-6ec3ef0c692b.png)
Figure 17The top 10 countries with the highest number of clients 
Graph of Aggregate Hotel Nations. Through this, we see that Portugal has the highest rate of hotel guests in the world. There were 12129, 10415, 8568 for Belgium, France, and Spain. We see European countries going to hotels the most through this. 
![image](https://user-images.githubusercontent.com/94780400/145020393-b35b4a33-6fbd-4b58-bfe2-284b694dc132.png)
![image](https://user-images.githubusercontent.com/94780400/145020403-3abde236-f018-456a-98d2-5f33b3701241.png)
![image](https://user-images.githubusercontent.com/94780400/145020414-e3f1d401-a80f-48d9-9250-b4de51768c8f.png)
![image](https://user-images.githubusercontent.com/94780400/145020429-2cea5294-92e1-4d16-947b-9e586c92ddbb.png)
Shows us the Dashboard 
Most guests at the hotel come from Europe. And they prefer to choose rooms in classes A and D. In addition, BB and HB also come with a la carte service: 
Hotels will concentrate on selling in the strong markets of Europe: Spain, Portugal, Belgium and France. In addition, in future markets such as America and Asia, it will be marketed. The hotel will build more rooms of types A and D in the future, if there is a strategy to build more hotels. Since these are the two styles of living rooms that are most preferred. They will tailor the dish to European tastes. Since most of the clients come from Europe. Moreover, to raise sales from the restaurant segment of customers, it will offer many facilities with meal service packages. 
3. Feedback 
4. ![image](https://user-images.githubusercontent.com/94780400/145020464-7d2eedba-31d8-44f8-a34b-72dafc1ac74b.png)
Figure 22Feedback 1 
As requested by the teacher, we have completed the data cleanup. And according to the findings, there are positive ratings for a significant number of viewers. 
![image](https://user-images.githubusercontent.com/94780400/145020522-255d50db-1dc9-4318-8750-c7b947223c86.png)
![image](https://user-images.githubusercontent.com/94780400/145020530-f6643d20-3666-468c-984b-b4f33248f75e.png)
Figure 24Feedback 3 
The evaluated data and the operational and strategic assumptions are highly regarded by the audience. 
![image](https://user-images.githubusercontent.com/94780400/145020555-1bc6c09e-94dc-4897-934b-7dae03936d45.png)
![image](https://user-images.githubusercontent.com/94780400/145020572-9fea95c2-21f0-48c9-a995-e4e8ed072fe8.png)
![image](https://user-images.githubusercontent.com/94780400/145020582-87190c1c-11de-465c-a37b-6d06032d1977.png)
Figure 27Feedback 6 
Our job on the tableau isn't fine. The dataset is not very strong and there are really few items that can be analyzed. 
	III. 	Point of view 
1.	The legal problems involved in the exploitation of business intelligence user data 
The main objective of BI instruments is to exploit and evaluate consumer or organizational data. These providers must, however, demonstrate how they safeguard information. Users should have specific records that provide legacy of data security In the event that BI tools use data inappropriately, all responsibility must be borne by statute. 
2.	How BI instruments can assist in decision making 
What-if Research helps to guess the potential trend, the very high precision of the risks and prizes-> helps to consider the decision. Present the data with the clearest way to understand -> allow us to interpret the data easier. When processing the data, getting the automated system -> decreases the cheat and error made by humans -> more trusted judgment. 
3.	Why do I pick python to clean the dataset? 
Python offers many features, repositories, and plugins that can enable the advancement of data cleaning. Python's syntax is completely plain, easy to learn and to understand the code (similar to reading English). 
References 
Albert Nogués, Juan Valladares. (2017). Business Intelligence Tools for Small Companies.  

