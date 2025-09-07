import zipfile
import pandas as pd

from typing import Iterable

def UnzipFile() -> None:
    """
    Function for unzipping the Excel 
    file with the postal codes by state
    """

    with zipfile.ZipFile('./CPdescargaxls.zip') as ZipFile:
        FileNameUnzip = ZipFile.filelist[0]
        ZipFile.extract(FileNameUnzip)

def ReadExcelSheets() -> Iterable[pd.DataFrame]:
    """
    Function for reading many Excel sheets 
    as pandas DataFrames from a workbook
    """

    with pd.ExcelFile('./CPdescarga.xls') as Workbook:
        DataFrames = pd.read_excel(Workbook,Workbook.sheet_names[1:])
        return DataFrames.values()