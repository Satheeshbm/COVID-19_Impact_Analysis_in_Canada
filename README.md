# Impact Analysis of COVID-19 in Canada

<a href="url"><img src="https://odh.ohio.gov/wps/wcm/connect/gov/9f25da6e-7aae-4c8b-94ff-9b41e1f56302/COVID-19-1280x480.jpg?MOD=AJPERES&CACHEID=ROOTWORKSPACE.Z18_M1HGGIK0N0JO00QO9DDDDM3000-9f25da6e-7aae-4c8b-94ff-9b41e1f56302-n3a09Co" align="centre" height="200" width="600" ></a>

###### Contributors: Tyeson Demets (tyedem), Nimai Desai (Nimai95), Trevor Yeomans (YuPsx2), Satheesh Mohan (Satheeshbm)

 Project Outline: Measuring COVID-19's impact on Canadian job markets, consumer price index, businesses, and community mobility

## Research Questions: 
1) What are COVID-19 hospitalizations summary statistics in Canada? (Replace - What is COVID-19's impact on Canadian economy)
2) What sectors in the job market are affected?
3) What were the top 5 industries impacted? 
4) How many businesses shut down across various industries?
5) What is COVID-19's impact on community mobility in Canada?
6) What is the COVID-19's impact on the Canadian CPI?

Datasets:
[Statcan](https://www.statcan.gc.ca/en/start), [Kaggle](https://www.kaggle.com/), [Bank of Canada](https://www.bankofcanada.ca/), [FRED](https://fred.stlouisfed.org/), [data.gov](https://www.data.gov/), [Our Wolrd in Data](https://ourworldindata.org/), [Google Community Mobility Reports](https://www.google.com/covid19/mobility/), [mapbox](https://www.mapbox.com/) and individual Canadian province open data websites. See data sources below.

Breakdown of responsibilities:

1) COVID-19 hospitalizations and CPI: Tyeson
2) Job market: Nimai
3) Top 5 industries and businesses: Trevor 
4) Community mobility: Satheesh

# Hypothesis

# Summary Findings

## COVID-19 Hospitalizations
## 
### Data Exploration & Cleanup
Data exploration involved navigating through Canadian provincial government open data web portals and perusing their data catalogue to find relevant data surrounding COVID-19. It was decided that total # of COVID-19 hospitalzations is the better data to analyze over total cases given the variability baked into how cases were tracked. For example, the quality of tracking cases is heavily subject to provincial COVID-19 testing capacity and the fact that severity of symptoms varied widely between individuals and certain demographics. Whereas total # of COVID-19 hospitalizations limits the variability of the severity of symptoms to those who require inpatient medical treatment and are thus incapable of working, which has a direct and obvious impact on the Canadian economy.

It was expected that COVID-19 open data would be available for all Canadian provinces and territories. However, data was only publicly available for the provinces of Quebec, Ontario, Manitoba, Saskatchewan and Alberta. Canada-wide hospitalizations data was not available through [Statcan](https://www.statcan.gc.ca/en/start) and had to be sourced via [Our World in Data](www.ourworldindata.org). After drilling down into their dataset, we were unable to locate a daily tracking of provincial hospitalizations and thus our hospitalizations dataset is restricted to the Canada-wide and the aforementioned provinces we were able to pull from the open data portals.

### Data Assumptions
Since each province has their own regulatory health authority, the methods of tracking COVID-19 are not consistent across provinces. For example, Ontario makes very specific distinctions between Intensive Care Units (ICUs) tracked, i.e. ICU due to COVID-19 related illness, ICU testing positive for COVID-19, ICU no longer testing positive for COVID-19, ICU on ventilators due to COVID-19, ICU on ventilators due to COVID-related critical illness, etc. No other province makes such specific distinctions in ICU tracking. Methods of tracking are also publicized with varying levels of detail, except Saskatchewan which doesn't publicize any details except that their dataset captures hospitalizations and ICUs. All hospitalization data is reported by hospitals to regional health authorities who then report to the provincial health authority. Canada's provincially regulated health system makes for data collection subject to greater variability than would be in a centralized regulatory health system. It has been decided to consolidate all hospitalizations and ICU data into a single dataset to limit this variability.

### Analysis - What are COVID-19 hospitalizations summary statistics in Canada? (Replace - What is COVID-19's impact on Canadian economy)

Of the hospitalizations datasets available, hospitalization movements generally follow a similar pattern at similar times, though Saskatchewan and Manitoba have experienced a very mild impact relative to the rest of the provinces measured. It is evident from the data Canada as a nation experienced 4 waves during the pandemic and at time of writing (January 2022), Canada is in the beginning of its 5th and largest wave yet. It remains unclear how acute this spike in hospitalizations will be over time. 

Ontario, Quebec and Alberta have each experienced major impacts due to COVID-19. Ontario and Quebec's impact are similar in the 1st wave April 2020 (when health authorities began tracking COVID-19 hospitalizations) and have generally followed the same pattern. One notable exception is Ontario's 3rd wave between March and June 2021 with its greatest peak. No other province measured experience such a dramatic spike in hospitalizations. Alberta experienced a later wave between September 2021 - December 2021. January 2021 is proving to be Quebec's largest spike in hospitalizations since the pandemic began in 2020. 

Summary statistics are available via mapbox plot in project's panel.


### Post-Mortem


## Job Market

### Data Exploration & Cleanup

### Analysis - What sectors in the job market are affected?

### Post-Mortem

## Industries

### Data Exploration & Cleanup

### Data Assumptions

### Analysis - What were the top 5 industries impacted?

### Post-Mortem

## Businesses - How many businesses shut down across various industries?

### Data Exploration & Cleanup

### Data Assumptions

### Analysis - How many businesses shut down across various industries?

### Post-Mortem

## Community Mobility

### Data Exploration & Cleanup

### Data Assumptions

### Analysis - What is COVID-19's impact on community mobility in Canada?

### Post-Mortem

## Consumer Price Index

### Data Exploration & Cleanup
We were able to pull CPI data directly from [Statcan](https://www.statcan.gc.ca/en/start). There were a few options available, so it was decided that the monthly CPI report was selected without seasonal adjustment to best reflect the true costs of goods and services without any statistical smoothening.

### Data Assumptions
There are a number of assumptions embedded into the development of the CPI of which only a few significant assumptions are highlighted here. The dataset used is not seasonally adjusted to even out seasonal swings in price movements. The quality of the data is constrained by budgets and the information available during the sampling process. The official time base in this CPI is 2002=100. The change is strictly an arithmetic conversion, but leaves the percentage changes between any two periods intact, except for any differences from rounding. For more details on CPI sampling, imputation, quality control, etc., visit https://www23.statcan.gc.ca/imdb/p2SV.pl?Function=getSurvey&SDDS=2301.

### Analysis - What is COVID-19's impact on the Canadian CPI?
Overall, price movements in Canada has seen steady growth trend and a particular steep climb upwards since December 2020. January 2019 saw an overall value of 133.6 and November 2021 saw an overall value of 144.2. A 7.9% increase over this time period. All provinces follow the same trend in price movements.

Some product groups of interest in Canada include Clothing and Footwear and Fresh Fruit and Vegetables which has seen major volatility. Energy experienced a particularly steep drop between February 2020 and April 2020. While Services was the only group that did not experience any drop when the pandemic hit in March 2020.

Focusing on the rate of change, Canada has seen overall volatility. Each province experienced some volatility to varying degrees. The territories experienced the greatest amount of volatility compared to the provinces.

### Post-Mortem
No particular difficulties arose for the CPI data. 

# Data Sources
## COVID-19 Data

1.	Canada - https://ourworldindata.org/grapher/current-covid-patients-hospital?country=~CAN
2.	Alberta - https://www.alberta.ca/stats/covid-19-alberta-statistics.htm#data-export
3.	Ontario - https://data.ontario.ca/en/dataset/covid-19-cases-in-hospital-and-icu-by-ontario-health-region

4. Quebec - https://www.donneesquebec.ca/recherche/dataset/covid-19-portrait-quotidien-des-hospitalisations

5.	Manitoba - https://geoportal.gov.mb.ca/datasets/manitoba::manitoba-covid-19-daily-cases-and-hospitalizations-historical/about
6.	Saskatchewan - https://dashboard.saskatchewan.ca/health-wellness/covid-19-cases/hospitalized

7. Geospatial Data - https://docs.mapbox.com/help/demos/geocoding/final.html

## Job Market

## Businesses

# Community Mobility

## Consumer Price Index
x. CPI - https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000401