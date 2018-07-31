# Grafana Dashboard Backup Tool

Some python programs to call Grafana API to:

* Save every datasource to each datasource file.
	* **saveDatasources.py**
* Save every dashboard to each dashboard file.
	* **saveDashboards.py**
* Create datasource from a backup file.
	* **createDatasource.py**
* Create dashboard from a backup file.
	* **createDashboard.py**

There a three convenient script files: 

1. **backup_grafana.sh**
2. **restore_dashboards.sh**
3. **restore_datasources.sh** 

you can use them to 

1. **backup all datasources and dashboards.**
	2. ex: sh backup_grafana.sh
2. **restore dashboards from your dashboard backup folder.**
	3. ex: sh restore_dashboards.sh /tmp/dashboards/2016-10-10_12:00:00
3. **restore datasources from your datasource backup folder.**
	4. ex: sh restore_dashboards.sh /tmp/datasources/2016-10-10_12:00:00

[Grafana API document](http://docs.grafana.org/http_api/overview/)

## ENV:
* python 2.7
	* Need to **pip install requests** library
* Garafana 3.0 API

## Setting

1. Export the environment variables bellow
2. GRAFANA_URL (the default url is http://localhost:3000)
3. GRAFANA_TOKEN 
        
You can see how to get token from here: [Grafana Web page](http://docs.grafana.org/http_api/auth/)

## How to Use
* First edit **grafana_settings.py** as above.
* Use **saveDashboards.py** to save each dashboard to each file.
	* ex: python saveDashboards.py **folder_path**

* Use **saveDatasources.py** to save each datasources to each file under specific folder.
	*  ex: python saveDatasources.py **folder_path**

* Use **createDashboard.py** to read the dashboard  file and create or update them on Grafana.
 	*  ex: python createDashboard.py **file_path**

* Use **createDatasource.py** to read the datasource  file and create or update them on Grafana.
 	*  ex: python createDatasource.py **file_path**

 
* Use **backup_grafana.sh** to backup all your dashboards and datasources to **/tmp** folder.
	* It will create 
		* two files: **/tmp/dashboards.tar.gz**, **/tmp/datasources.tar.gz** 
		* two folders contain dashboard files and datasource files: **/tmp/dashboards/$current_time**, **/tmp/datasources/$current_time**
	* ex：**sh backup_grafana.sh**
	* result：**/tmp/dashboads.tar.gz**, **/tmp/datasourcess.tar.gz**, **/tmp/dashboards/2016-10-10_12:00:00**, **/tmp/datasources/2016-10-10_12:00:00**

## Changes from original 
* Primary change here is that the output was modified to be more concise and readable. The original script attempted to delete every dashboard before creating it, regardless of it existed or not, resulting in a lot of unnecessary clutter from 404: Graph not found messages. The modified script still attempts to delete, but will now only output a message if the graph did in fact exist before the delete attempt.

* Output is now clearer in general and with less clutter.

## Notes

* The role of the API key you specify in the grafanaSettings file NEEDS to be "Admin" or the scripts will not have the correct permissions to work properly. Backing up dashboards may not work correctly and backing up datasources will not work at all.

* If you have graphs whose datasource is Cloudwatch, the scripts will still back up and restore these correctly, but you MUST run the server in question on a machine that has been given appropriate Cloudwatch permissions or they will not display properly. All other data sources appear to work correctly regardless of machine.
