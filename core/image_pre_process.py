import os
import sys
from osgeo import gdal
from sqlalchemy import null


# 数据存放，保存目录

source_data_path = {
    "image":{
        "r_band":"/",
        "g_band":"/",
        "b_band":"/",
        "pan_band":"/",
        "nir_band":"/",
    },
    "vector":"/",
    "result":"/"
}

result_data_path = {
    "image":{
        "rgb_tif":"/",
        "fusion_tif":"/",
        "clip_tif":"/",
        "convert_crs_tif":"/"
    },
    "vector":"/",
}

class ImagePreProcess:
    def __init__(self) -> None:
        pass

## 读取影像:哨兵/Landsat/GF-1/GF-2
## 读取矢量：shp/geojson
    def read_image():
        r_band = null
        g_band = null
        b_band = null
        nir_band= null
        pan_band = null

        return [b_band,g_band,r_band,pan_band,nir_band]


    def read_vector():
        pass


    ## 单波段：几何/正射校正
    def geometric_correction():
        pass


    ## 波段合成(RGB/Faslse Color)
    def rbg_color_composite():
        pass


    def false_color_composite():
        pass


    ## 影像融合(全色与多光谱)
    def image_fusion():
        pass


    ## 影像镶嵌(多幅影像之间)
    def image_mosaic():
        pass


    ## 匀色处理（多幅影像镶嵌之后）
    def image_seamless_mosaic():
        return null


    ## 影像裁剪(矢量边接)
    def clip_image():
        pass


    ## 大气校正
    def radiometric_correction():
        pass

    
    ## 坐标转换
    def convert_crs():
        pass


    ## 影像重采样
    def image_resample():
        pass


    ## 格式转换
    def convert_format():
        pass



if __name__ == '__main__':
    pass



