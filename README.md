# COVID-19-Data-Analysis
GUI Application to view the analysis of Corona data
In this project, i have analysed COVID-19 using python and created an GUI Application to view the results of the analysis.
# Dataset
The Dataset was acquired from Kaggle.
https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset
This dataset has daily level information on the number of affected cases, deaths and recovery from 2019 novel coronavirus.This is a time series data and so the number of cases on any given day is the cumulative number.The data is available from 22 Jan, 2020.The following are the columns of the dataset.
- Sno - Serial number
- ObservationDate - Date of the observation in MM/DD/YYYY
- Province/State - Province or state of the observation
- Country/Region - Country of observation
- Last Update - Time in UTC at which the row is updated for the given province or country.
- Confirmed - Cumulative number of confirmed cases till that date
- Deaths - Cumulative number of of deaths till that date
- Recovered - Cumulative number of recovered cases till that date
# Application
   It is python Tkinter GUI Application.
<p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/44143282/81507424-5af14880-92cb-11ea-9a35-b816d4776657.png">
</p>
 
The following queries were implemented using python.
- World wide analysis of COVID-19, which shows the total number of deaths, Confirmed and Recovered cases
 <p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/44143282/81507574-55e0c900-92cc-11ea-8f0b-c06d4194be40.png")
</p>
   
- Country wise analysis , whatever the country name we give in the text box,it shows its analysis.In this case, it shows US data.
 <p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/44143282/81507653-d69fc500-92cc-11ea-9e24-62fe6491fe91.png">
    </p>
- Top 10 countries affected by COVID-19
   <p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/44143282/81507729-431ac400-92cd-11ea-98e5-3e64905e0591.png">
    </p>
- Least affected Countries
  <p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/44143282/81507842-0ac7b580-92ce-11ea-9188-f14f5bc6073d.png">
    </p>
- State wise analysis - It shows the state wise analysis for whatever country you want.
  <p align="center">
  <img width="460" height="300" src="https://user-images.githubusercontent.com/44143282/81507936-a78a5300-92ce-11ea-888e-e578869ba708.png">
    </p>
