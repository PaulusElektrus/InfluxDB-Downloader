from influxdb import InfluxDBClient
import pandas as pd
import configparser
import argparse


def download(series, measurement, database, query):

    client = InfluxDBClient(host, 8086, user, password, database)

    if query == None:
        query = "SELECT " + series + " FROM " + measurement

    points = client.query(query).get_points()

    df = pd.DataFrame(points)

    path = "../data/" + series + ".csv"

    df.to_csv(path)

    print("Download abgeschlossen")
    print(df)


def parse_args():
    parser = argparse.ArgumentParser(description="Download InfluxDB Data")
    parser.add_argument(
        "-s", "--series", type=str, required=False, help="specify series to download"
    )
    parser.add_argument(
        "-m", "--measurement", type=str, required=False, help="from given measurement"
    )
    parser.add_argument("-d", "--database", type=str, required=True, help="in database")
    parser.add_argument(
        "-q", "--query", type=str, required=False, help="OR enter a full Influx query"
    )
    return parser.parse_args()


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read_file(open("./token.config", mode="r"))
    host = config.get("config", "host")
    user = config.get("config", "user")
    password = config.get("config", "password")

    args = parse_args()

    download(
        series=args.series,
        measurement=args.measurement,
        database=args.database,
        query=args.query,
    )
