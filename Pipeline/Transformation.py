import pandas as pd
import numpy as np

def CleanPostalCodesDataframe(
        PostalCodesDataframe: pd.DataFrame
    ) -> np.ndarray:
    """
    Function for drop an empty column 
    and return a numpy array of values
    """

    PostalCodesDataframeClean = PostalCodesDataframe.drop(columns=['c_CP']).values
    PostalCodesDataframeClean[PostalCodesDataframeClean != PostalCodesDataframeClean] = None
    return map(tuple,PostalCodesDataframeClean)