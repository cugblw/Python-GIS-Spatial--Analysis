# -*- encoding: utf-8 -*-

'''
@File    :   upload_shapefile.py
@Time    :   2022/06/02 12:05:55
@Author  :   Weil Lee
@Version :   1.0
@Email   :   cugblw2014@outlook.com
@Desc    :   upload shapefile to database.
'''


#import required libraries
import os

import pandas as pd
import geopandas as gpd
from sqlalchemy import create_engine

class Database( object ):
    def __init__(self, database_name, database_host, database_port, database_username, database_password):
        self.database_name = database_name
        self.database_host = database_host
        self.database_port = database_port
        self.database_username = database_username
        self.database_password = database_password
        self.database_url = 'postgresql://{}:{}@{}:{}/{}'.format(self.database_username, self.database_password, self.database_host, self.database_port, self.database_name)
        self.engine = create_engine(self.database_url)
        self.conn = self.engine.connect()
        # self.metadata = self.engine.metadata
        # self.table_name = None

    def __del__(self):
        self.conn.close()

# upload single shapefile
def upload_single_shapefile(shapefile_path, conn,schema):
    # read shapefile
    shapefile_gdf = gpd.read_file(shapefile_path)
    basename = os.path.basename(shapefile_path)
    table_name = basename.split('.')[0]
    shapefile_gdf.to_postgis(table_name, conn, schema = schema, if_exists='replace', index=False, index_label='index')
    print('Upload {} successfully!'.format(basename))

# upload multiple shapefiles
def upload_multi_shapefiles(shapefile_dir, conn, schema):
    # read shapefile
    for root, dirs, files in os.walk(shapefile_dir):
        for file in files:
            if file.endswith('.shp'):
                shapefile_path = os.path.join(root, file)
                upload_single_shapefile(shapefile_path, conn, schema)
    conn.close()
    del root, dirs, files

#upload excel file
def upload_single_xlsx(xlsx_path, conn, schema):
    basename = os.path.basename(xlsx_path)
    table_name = basename.split('.')[0]
    excel_df = pd.read_excel(xlsx_path,sheet_name='Sheet1')
    print(excel_df.keys())
    excel_df.to_sql(table_name, conn, schema = schema, if_exists='replace', index=False, index_label='index')
    print('Upload {} successfully!'.format(basename))

# upload multiple excel files
def upload_multi_xlsx(xlsx_dir, conn, schema):
    for root, dirs, files in os.walk(xlsx_dir):
        for file in files:
            if file.endswith('.xlsx'):
                xlsx_path = os.path.join(root, file)
                upload_single_xlsx(xlsx_path, conn, schema)
    conn.close()
    del root, dirs, files


## To Do

def upload_single_csv():
    pass

def upload_multi_csv():
    pass

def upload_single_geojson():
    pass

def upload_multi_geojson():
    pass


if __name__ == '__main__':
    database_name = 'Vector'
    database_host = 'localhost'
    database_port = '5432'
    database_username = 'postgres'
    database_password = '123456'
    database_schema = 'Cities'
    database = Database(database_name, database_host, database_port, database_username, database_password)
    shapefile_path =  r"E:\Data\Vector\World_Cities\World_Cities.shp"
    # shapefile_dir = r"E:\Data\Vector\中国省级行政区划（审图号）"
    # xlsx_dir = r"E:\Data\Vector\China"
    # satellite_wrs_dir = r"E:\Data\Vector\Satellite_WRS"

    
    if  database.conn:
        # print('Connected to database successfully!')
        upload_single_shapefile(shapefile_path, database.conn, database_schema)
        # upload_multi_shapefiles(shapefile_dir, database.conn, "China")
        # upload_multi_xlsx(xlsx_dir, database.conn, "China")
        # upload_multi_shapefiles(satellite_wrs_dir, database.conn, "Satellite_WRS")
        database.conn.close()