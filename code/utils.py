import numpy as np
import pandas as pd

def get_params(df):
    x = np.arange(len(df))
    y = np.array(df['star_age'])
    idxs = ~np.isnan(y) # good indexes (no nan values)

    # the low error bar is sometimes positive and sometimes negative (we should take the abs value)
    yerr_lower = np.abs(np.array(df['star_age_error_min'])) # absolute value to avoid negative errorbars
    # if yerr_lower is nan, set it to zero
    yerr_lower[np.isnan(yerr_lower)] = 0
    yerr_upper = np.abs(np.array(df['star_age_error_max'])) # absolute value to avoid negative errorbars
    # if yerr_upper is nan, set it to zero
    yerr_upper[np.isnan(yerr_upper)] = 0
    
    # grab only non-nan values (i.e. stars with age determined)
    x, y, yerr_lower, yerr_upper = x[idxs], y[idxs], yerr_lower[idxs], yerr_upper[idxs]
    yerr = [yerr_lower, yerr_upper]

    return x, y, yerr