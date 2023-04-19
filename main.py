from extract_data_material import scrape_data

base_url = "https://www.indexmundi.com/commodities/?commodity="

df_aluminum = scrape_data(base_url + "aluminum")
print(df_aluminum)
df_cold_rolled_steel = scrape_data(base_url + "cold-rolled-steel")
print(df_cold_rolled_steel)


