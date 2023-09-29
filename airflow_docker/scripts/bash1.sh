echo "The script is starting"

cd /opt/airflow/vitamincscrapy/ && pwd

scrapy crawl vitamincspider -O airflowscrapy.csv
echo "Script executed"