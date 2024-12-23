README
Traffic Congestion Prediction Using Fuzzy Logic
This project involves predicting traffic congestion levels using fuzzy logic systems. To demonstrate the fuzzy logic model, a test script is provided that can be run without the need for extensive data extraction.
Running the Fuzzy Logic Test Script Script: fuzzysystemtest.py
Purpose: The fuzzysystemtest.py script contains the implementation of the fuzzy logic system for predicting traffic congestion. It uses predefined test cases to simulate and display the output of the model.
Running the Test Script
The fuzzysytemtest.py script demonstrates the fuzzy logic system's capabilities using predefined test cases. Follow the steps below to execute the script:
1. Ensure All Necessary Files Are Present: ○ fuzzysytemtest.py
○ constants.py
2. Both files should reside in the same directory to ensure proper import and execution.
○ Install Required Libraries:
If you haven't installed the necessary Python libraries yet, do so using the following command:
bash
Copy code
pip install numpy scikit-fuzzy matplotlib
3.
○ Execute the Script:
Open a terminal or command prompt in the project directory and run the following command:
bash
 
Copy code
python fuzzysytemtest.py 4. View the Results:
○ Console Output: The script will display the predicted congestion levels for each test case directly in the terminal.
○ Result File: A text file named test_case_result.txt will be generated, containing detailed results of each test case.
○ Visualizations: For each test case, a corresponding image file (e.g., test_case_1_output.png) will be saved in the current directory, illustrating the congestion level output.
Understanding the Output
Upon running the fuzzysystemtest.py script, you will receive both textual and visual outputs that detail the predicted traffic congestion levels based on the predefined test cases.
1. Console Output:
Each test case will display:
○ Test Case Number and Description: Provides context about the scenario being tested.
○ Inputs: Shows the values of total_cars, rush_hour, heavy_vehicle_percentage, and weather_category used for the prediction.
○ Predicted Congestion Level (V/C Ratio): Numerical value representing the congestion level.
○ Congestion Status: Categorical interpretation of the V/C Ratio (e.g., Free Flow, Moderate, Heavy, Severe).
○ Example: yaml
Copy code
---
○ Test Case 1: High total cars, rush hour, low heavy vehicles, clear weather
○ Predicted Congestion Level (V/C Ratio): 0.65
○ Congestion Status: Moderate
2.
3. Result File (test_case_result.txt):
Contains detailed logs of each test case, mirroring the console output for record-
keeping and further analysis.
4. Visualizations (test_case_X_output.png):
Graphical representations of the fuzzy logic system's interpretation of congestion levels for each test case. These plots illustrate how input variables are mapped to congestion levels based on the defined fuzzy rules and membership functions.
○
 
 Notes
● Data Extraction:
○ The other scripts in the project are designed to download, process, and analyze
large datasets of traffic and weather information.
○ This data extraction process can be time-consuming and may require
significant computational resources.
○ To simplify the demonstration, the fuzzonday.py script uses predefined test
cases and does not require external data. ● Dependencies:
○ Ensure all required Python packages are installed before running the script.
○ If you encounter any issues with missing packages, you can install them
individually using pip. ● Mistakes:
○ We are aware upon checking the code that we have left some codeparts with norwegian comments.
