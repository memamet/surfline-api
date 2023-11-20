import pysurfline

# spotId = "5842041f4e65fad6a7708cfd" # Anchor Point
# spotId = "5842041f4e65fad6a7708890" # Pipeline
spotId = "5842041f4e65fad6a7708bca" # La Grande Plage à Biarritz

spotforecasts = pysurfline.get_spot_forecasts(spotId)

print(spotforecasts)