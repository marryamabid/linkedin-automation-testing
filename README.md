# linkedin-automation-testing
#LinkedIn Automation Testing
This project focuses on automating LinkedIn's login functionality and connection request process using Python and Selenium. It simulates human-like interactions such as typing and random delays to improve automation accuracy and reduce detection risks.


#Project Overview
#Objectives:
Automate the LinkedIn login process.
Navigate to the "My Network" section.
Identify and click the "Connect" button to send a connection request.
Tools & Technologies Used
Programming Language: Python
Libraries: Selenium, random, time
IDE: Visual Studio Code
Browser: Google Chrome
Operating System: Windows
Project Setup
Follow these steps to set up and run the project:

1. Clone the Repository

git clone https://github.com/marryamabid/linkedin-automation-testing.git
cd linkedin-automation-testing
2. Install Python
Ensure Python is installed. Verify by running:


python --version
If not installed, download it from python.org.

3. Set Up a Virtual Environment
Create a virtual environment to manage dependencies:


python -m venv venv
Activate the virtual environment:

Windows: venv\Scripts\activate
Mac/Linux: source venv/bin/activate


4. Install Dependencies
Install the required Python packages from requirements.txt:

pip install -r requirements.txt


5. ChromeDriver Setup
Download the appropriate version of ChromeDriver from ChromeDriver Download.
Place the ChromeDriver executable in the project folder and update the path in practice.py.

6. Running the Automation Script
Execute the script to automate LinkedIn actions:


python practice.py
Project Structure


Code Explanation
func.py: Contains helper functions:
random_delay(): Introduces random delays to mimic human behavior.
human_typing(): Simulates human-like typing.
practice.py:
Opens LinkedIn login page.
Automates login with credentials.
Navigates to "My Network" and sends a connection request.
Challenges Faced
Handling dynamic elements with XPath selectors.
Ensuring synchronization between page loading and script execution.
Future Improvements
Automating additional LinkedIn features like profile viewing and messaging.
Implementing logging and reporting features.
Security Note
Important: Never hard-code sensitive information like email and passwords in the script. Use environment variables instead.

Contributing
If you'd like to contribute, please feel free to fork the repository and submit pull requests.
