import pandas as pd
from datacollect.scraper import download_file, setup
from datacollect.constants import Roadids

# Set date range
date_from = "2023-10-31"
date_to = "2024-11-01"

# Set up WebDriver and download directory
driver, download_dir = setup()

# Iterate through Roadids and download files
for location, road_id in Roadids.items():
    if isinstance(road_id, dict):  # If the value is a dictionary, iterate through its items
        for sub_location, sub_road_id in road_id.items():
            download_file(
                name=f"{location} - {sub_location}",
                roadid=sub_road_id,
                driver=driver,
                download_dir=download_dir,
                date_from=date_from,
                date_to=date_to
            )
    else:  # Single road ID
        download_file(
            name=location,
            roadid=road_id,
            driver=driver,
            download_dir=download_dir,
            date_from=date_from,
            date_to=date_to
        )

# Quit the driver after all downloads are complete
driver.quit()
