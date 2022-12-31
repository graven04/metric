import pandas
import wbdata
import datetime

def get_gdp(country, time):

    """ This gets the GDP of "country" in year "time" through the
    World Bank database. It gets GDP in constant
    international dollars, Indicator code: NY.GDP.MKTP.PP.CD"""
    data = wbdata.api.get_dataframe({"NY.GDP.MKTP.PP.CD": "GDP"}, country=country, data_date=time)
    return data._get_value(0, 0, takeable=True)


def get_gini(country, time):
    """ This gets the GDP of "country" in year "time"
    through the World Bank database. Indicator code: SI.POV.GINI"""
    data = wbdata.api.get_dataframe({"SI.POV.GINI": "GINI"}, country=country, data_date=time)
    return data._get_value(0, 0, takeable=True)

country = "GBR"
time = datetime.datetime(2017, 1, 1), datetime.datetime(2017, 1, 1)
  
# gdp_uk = get_gdp(country, time)
gdp_uk = "{:,}".format(get_gdp(country, time))

gini_uk = get_gini(country, time)

print(f"In the UK GDP at 2017 was ${gdp_uk}, and the GINI coefficent at 2017 was: {gini_uk}")

metric = float(get_gdp(country, time)) * ((100 - gini_uk)/100)
printable_metric =  "{:,}".format(metric)

print(f"Metric for UK in 2017 was: £{printable_metric}")
