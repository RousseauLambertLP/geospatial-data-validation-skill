#!/usr/bin/env python3
"""Read-only metadata inspection for GDAL-supported raster datasets."""
import argparse
import json
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('path', help='Local raster path')
    args = parser.parse_args()
    try:
        from osgeo import gdal
    except ImportError:
        print('GDAL Python bindings are required: osgeo.gdal', file=sys.stderr)
        return 2
    ds = gdal.Open(args.path, gdal.GA_ReadOnly)
    if ds is None:
        print('Unable to read raster', file=sys.stderr)
        return 1
    result = {
        'path': args.path,
        'driver': ds.GetDriver().ShortName,
        'width': ds.RasterXSize,
        'height': ds.RasterYSize,
        'bands': ds.RasterCount,
        'projection_wkt': ds.GetProjection(),
        'geotransform': ds.GetGeoTransform(can_return_null=True),
        'band_metadata': [
            {'index': i, 'type': gdal.GetDataTypeName(ds.GetRasterBand(i).DataType),
             'nodata': ds.GetRasterBand(i).GetNoDataValue(),
             'unit': ds.GetRasterBand(i).GetUnitType()}
            for i in range(1, ds.RasterCount + 1)
        ]
    }
    print(json.dumps(result, indent=2, default=str))
    return 0


if __name__ == '__main__':
    sys.exit(main())
