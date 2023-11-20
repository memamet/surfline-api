import pysurfline


def fetch_surf_data(spot_id):
    # Use pysurfline to get the data
    # This is where you'd handle any exceptions or retries as needed
    return pysurfline.get_spot_forecasts(spot_id)
