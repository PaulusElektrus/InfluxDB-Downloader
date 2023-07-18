# InfluxDB Data Downloader

This Python script allows you to download data from InfluxDB and save it as a CSV file. It uses the `influxdb` library to connect to the InfluxDB server and the `pandas` library to handle the data.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed on your system.
- The required Python libraries installed: `influxdb`, `pandas`, `configparser`, and `argparse`.
- Access to an InfluxDB server with the necessary credentials.

## Installation

1. Clone the repository or download the script file `influxdb_data_downloader.py` to your local machine.

   ```shell
   git clone https://github.com/PaulusElektrus/InfluxDB-Downloader
   ```

2. Install the required Python libraries using pip:

   ```shell
   pip install influxdb pandas
   ```

## Configuration

1. Create a file named `token.config` in the same directory as the script.
2. Open the `token.config` file and enter your InfluxDB server configuration details in the following format:

   ```ini
   [config]
   host = your_influxdb_host
   user = your_influxdb_username
   password = your_influxdb_password
   ```

   Replace `your_influxdb_host`, `your_influxdb_username`, and `your_influxdb_password` with the appropriate values for your InfluxDB server.

## Usage

Run the script using the following command:

```shell
python influxdb_data_downloader.py [-h] [-s SERIES] [-m MEASUREMENT] -d DATABASE [-q QUERY]
```

The script accepts the following command-line arguments:

- `-s SERIES`, `--series SERIES`: Specify the series to download. You can use the `*` wildcard to download all series (default: `*`).
- `-m MEASUREMENT`, `--measurement MEASUREMENT`: Specify the measurement from which to download data.
- `-d DATABASE`, `--database DATABASE`: Specify the InfluxDB database name.
- `-q QUERY`, `--query QUERY`: Enter a custom InfluxDB query to download specific data (optional).

The downloaded data will be saved as a CSV file in the `./data/` directory with the filename corresponding to the series name.

Example usages:

```shell
# Download all series from the 'measurement1' in 'mydatabase'
python influxdb_data_downloader.py -m measurement1 -d mydatabase

# Download 'series1' from the 'measurement2' in 'mydatabase'
python influxdb_data_downloader.py -s series1 -m measurement2 -d mydatabase

# Download data using a custom InfluxDB query
python influxdb_data_downloader.py -q "SELECT field1, field2 FROM measurement3 WHERE time > now() - 1h" -d mydatabase
```

After running the script, the downloaded data will be saved as a CSV file, and the script will print the downloaded data on the console.

**Note:** Make sure the `token.config` file and the script file (`influxdb_data_downloader.py`) are in the same directory when running the script.
