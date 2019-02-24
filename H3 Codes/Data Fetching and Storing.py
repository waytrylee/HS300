#%% [markdown]
# # HS300指数纯因子组合构建
# 
# > WIFA量化组，2019年春。
# 
# ## Step 2: Factor Database building.

#%%
import os           # for getting working directory.
path = os.getcwd()  # current working directory.
import pandas as pd # for wrapping csv file.

#%%
# Import Wind Module for getting data.
import WindPy as w
from WindPy import *
w.start()

#%%
# The factor list stores the factor string I need.
factor_list = [
    "pe_ttm", 
    "pb_lyr", 
    "pcf_ncf_ttm", 
    "ps_ttm", 
    "yoyprofit",
    "yoy_or", 
    "yoyroe", 
    "roe_ttm", 
    "roa_ttm", 
    "debttoassets", 
    "assetsturn", 
    "invturn",  
    "pct_chg", 
    # "underlyinghisvol_90d", 
    # "tech_turnoverrate20", 
    # "tech_turnoverrate60", 
    # "tech_turnoverrate120", 
    # "val_lnmv"
    # The last 5 data haven't been downloaded yet for quota exceeded.
]

#%%
# Getting the stock list of HS300.
hs300_stocks_list = list(w.wset(
    "sectorconstituent", 
    "date=2019-02-20;windcode=000300.SH", # base on recent date.
    usedf = True
)[1]['wind_code'])

#%%
def data_fetching_and_storing(
    start = "2005-01-01", 
    end = "2019-02-20"
):
    # Import data from wind and store it as csv.
    for factor in factor_list:
        factor_data = w.wsd(
            hs300_stocks_list, 
            factor, 
            start, 
            end, 
            "Period=M", 
            usedf = True # use pandas dataframe.
        )[1]             # the result is a tuple with the [1] part is what we need.
        # Make a new directory (H3 Data) for storing data.
        file_path = path + "\\H3 Data\\Raw Data\\" + factor + ".csv" # name the data file by it's factor string.
        factor_data.to_csv(file_path)                      # store data.

#%%
def sw_industry_data_fetching_and_storing():
    industry_sw = w.wsd(
        hs300_stocks_list, 
        "industry_sw", 
        "2019-02-20", 
        "2019-02-20", # set the start and end date as the same.
        "industryType=1;Period=M",
        usedf = True 
    )[1]
    file_path = path + "\\H3 Data\\Raw Data\\industry_sw.csv"
    industry_sw.to_csv(file_path)

#%%
data_fetching_and_storing()

#%%
sw_industry_data_fetching_and_storing()