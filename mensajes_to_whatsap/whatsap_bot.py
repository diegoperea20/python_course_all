# Import the necessary libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Start the webdriver and navigate to WhatsApp web
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com/")

# Wait for the user to scan the QR code and log in
input("Press Enter once you have scanned the QR code and logged in to WhatsApp web")

# Find the search box and search for the desired contact
search_box = driver.find_element_by_xpath('//*[@id="side"]/div[1]/div/label/input')
search_box.send_keys("Contact Name")
search_box.send_keys(Keys.RETURN)
time.sleep(1)

# Find the chat history
chat_history = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div/div[1]/div/div/div[2]')

# Define the list of messages that the bot should respond to
responses = ["message 1", "message 2", "message 3"]

# Wait for new messages to arrive
while True:
    # Check for new messages
    new_messages = chat_history.find_elements_by_css_selector('div.message-in')

    # If there are new messages, process them
    if len(new_messages) > 0:
        for message in new_messages:
            # Get the text of the message
            text = message.find_element_by_css_selector('span.selectable-text').text

            # If the message is in the list of responses, send a response
            if text in responses:
                # Find the chat box and send a response
                chat_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
                chat_box.send_keys("Hello, this is a response from your WhatsApp bot!")
                chat_box.send_keys(Keys.RETURN)

    # Sleep for a few seconds before checking for new messages again
    time.sleep(3)
