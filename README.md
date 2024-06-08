# dbxDownloader
Simple Python code to download all files in a specified directory (and sub-directories) on Dropbox.

# Instructions:
## Install necessary libraries
`pip install dropbox`

## Set Up Your Dropbox App:

1. Go to the Dropbox App Console and create a new app.
2. Ensure the application has `files.metadata.read` and `files.content.read`
3. Generate an access token from the app console.

## Update the Script:

1. Replace YOUR_ACCESS_TOKEN with your actual Dropbox API access token.
2. Replace DROPBOX_FOLDER_PATH with the path of the folder in your Dropbox.
3. Replace LOCAL_FOLDER_PATH with the local path where you want to save the downloaded files.
4. Run the Script
