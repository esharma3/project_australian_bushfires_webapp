# AUSTRALIA BUSHFIRE CENTRAL (WebApp) - Group Project

University of Texas at Austin, Data Bootcamp 2019-2020

Group Members - Ekta Sharma | David Altuve | James Durnan | Catherine Gomes | Claudia Ibarra | Austin SpaceK

[Project Requirements](project_documents/Project_II_Requirements.docx)

![AUS Bushfire Central](static/images/readme_image.gif)

### Objective: 

To analyze and present the history and impact of Australian Bushfires through a web app.
Bushfires in Australia are a widespread and regular occurrence that have contributed significantly to moulding the nature of the continent over millions of years. Bushfires have killed approximately 800 people in Australia since 1851, and billions of animals. The purpose of this project is to dig deeper into the roots of current and historical bushfires in Australia and present the findings and analysis results in the form of a web based Flask app with routes for -  Australian bushfire locations, global bushfire locations, current and historical fire counts, impact caused by bushfires and climate’s role in causing the bushfires, home and about page.

### Additional Highlights:

*   Access to the project data using API requests 
*   Fun 404 page 
*   Feedback section on the Home Page that lets user post comments

### Technologies Used:

*   APP – Flask, Flask-SQLAlchemy, Python
*	Database – MySQL on GCP. Script created using SQL
*   Templates – HTML, CSS, Bootstrap
*   Interactive Features – JavaScript, Plotly
*   Visualizations – Plotly map, bar graph, pie chart, line graph, scatter plot
*	Web Scraping – Requests, Beautiful Soup
*   Deployment - GCP (Google Cloud Platform)

### Data Sources:

*   Australia and Global Fire Locations – NASA, Fire Information for Resource Management System (FIRMS)
*   Protected Species Impact - Australian Government, Department of Agriculture, Water and the Environment
*   Socio - Economic Impact – Wikipedia Economy of Australia
    *   Bushfire Season – Wikipedia 2019–20 Australian bushfire season
    *   Major Bushfires – Wikipedia, List of major bushfires in Australia
    *   The World Bank Data, Country Australia
*   Climate Data – Australian Government Bureau of Meteorology
*   Greenhouse Gases – CSIRO 
*   Fire Counts – GFED (Global Fire Emissions Database)

### Project Data Routes:

*   https://australia-bushfire-central-ak7h3hm6ya-uc.a.run.app/annual_total_fire_counts?state=&year=
*   https://australia-bushfire-central-ak7h3hm6ya-uc.a.run.app/climate_data?category=
*   https://australia-bushfire-central-ak7h3hm6ya-uc.a.run.app/impact-data
*   https://australia-bushfire-central-ak7h3hm6ya-uc.a.run.app/econ-impact
*   https://australia-bushfire-central-ak7h3hm6ya-uc.a.run.app/aus_fire_map/<year>

### Project API Documentation:

https://documenter.getpostman.com/view/10893300/SzYXVdtw


© 2020 Copyright: University of Texas, Data Bootcamp
