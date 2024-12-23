from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import os
import time
from datacollect.constants import Roadids


def setup():
    # Set up Chrome options
    options = webdriver.ChromeOptions()

    # Specify the directory to save the downloaded file
    download_dir = os.path.join(os.getcwd(), "downloads")

    # Ensure the directory exists
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)

    # Add preferences to Chrome options
    prefs = {
        "download.default_directory": download_dir,  # Set default download directory
        "download.prompt_for_download": False,      # Disable download prompt
        "directory_upgrade": True,                  # Automatically overwrite files
        "safebrowsing.enabled": True                # Disable Chrome's safe browsing feature
    }
    options.add_experimental_option("prefs", prefs)

    # Initialize the WebDriver with webdriver-manager
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
    return driver, download_dir

def download_file(name,roadid, driver, download_dir, date_from, date_to):
    

    # Navigate to the webpage
    driver.get(f"https://trafikkdata.atlas.vegvesen.no/#/eksport?datatype=HOUR&from={date_from}&lat=59.93623700438067&lon=10.874669090206872&to={date_to}&trpids={roadid}&zoom=12")

    try:
        # Wait until the button is clickable
        wait = WebDriverWait(driver, 10)
        button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "knapp-liten")))

        # List files before clicking the button
        existing_files = set(os.listdir(download_dir))

        # Click the button to start downloading
        button.click()
        print("Download started...")

        # Wait briefly for the new file to appear
        time.sleep(5)  # Give the browser some time to create the new file

        # List files after clicking the button
        new_files = set(os.listdir(download_dir)) - existing_files
        if not new_files:
            raise Exception("No new file detected. Ensure the download directory is correct.")

        # Extract the base name (before `.csv.crdownload`)
        downloading_file = list(new_files)[0]
        base_file_name = downloading_file.split(".csv")[0] + ".csv"
        print(f"Detected base file name: {base_file_name}")

        # Wait for the file to complete downloading
        file_complete = False
        max_wait_time = 300  # Maximum wait time in seconds
        start_time = time.time()

        while not file_complete:
            files = os.listdir(download_dir)

            # Check if the file with the exact base name and `.csv` exists
            if base_file_name in files:
                file_complete = True
                print(f"Download complete: {base_file_name}")

                # Rename the file with the new name
                new_name = f"{name}_data_{date_from}_to_{date_to}.csv"
                os.rename(
                    os.path.join(download_dir, base_file_name),
                    os.path.join(download_dir, new_name)
                )
                print(f"File renamed to: {new_name}")
            else:
                if time.time() - start_time > max_wait_time:
                    raise TimeoutError("Download did not complete within the expected time.")
                print(f"File is still downloading... ({downloading_file})")
                time.sleep(2)  # Wait before rechecking

    except Exception as e:
        print(f"An error occurred: {e}")

