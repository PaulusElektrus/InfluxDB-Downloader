# InfluxDB --> Pandas Dataframe --> CSV Downloader

### Arguments:

- Usage: 
        
        python dataDownload.py [-h] [-s SERIES] [-m MEASUREMENT] -d DATABASE [-q QUERY]

- Optional arguments:

        -h, --help            show this help message and exit

        -s SERIES, --series SERIES
                            specify series to download or leaf empty to download all series

        -m MEASUREMENT, --measurement MEASUREMENT
                            from given measurement

        -d DATABASE, --database DATABASE
                            in database

        -q QUERY, --query QUERY
                            OR enter a full Influx query
