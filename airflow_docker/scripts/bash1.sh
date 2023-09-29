echo "The script is starting"

cd /opt/airflow/vitamincscrapy/ && pwd

scrapy crawl vitamincspider -O Output_Data/airflowscrapy-$(date '+%FT%T.%3N').csv
echo "Script executed"