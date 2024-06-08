
import dropbox
import os

# Replace 'YOUR_ACCESS_TOKEN' with your actual Dropbox API access token.
ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
# Replace 'DROPBOX_FOLDER_PATH' with the path of the folder you want to download files from.
DROPBOX_FOLDER_PATH = '/dropboxFolder'
# Replace 'LOCAL_FOLDER_PATH' with the path of the local folder you want to save files to.
LOCAL_FOLDER_PATH = 'downloadTemp'

# Initialize a Dropbox object using the access token
dbx = dropbox.Dropbox(ACCESS_TOKEN)


def download_files(dropbox_folder, local_folder):
    # Ensure the local folder exists
    if not os.path.exists(local_folder):
        os.makedirs(local_folder)

    try:
        # List files and folders in the specified Dropbox folder
        for entry in dbx.files_list_folder(dropbox_folder).entries:
            local_path = os.path.join(local_folder, entry.name)
            dropbox_path = f'{dropbox_folder}/{entry.name}'

            if isinstance(entry, dropbox.files.FileMetadata):
                # If it's a file, download it
                print(f'Downloading {dropbox_path} to {local_path}')
                with open(local_path, 'wb') as f:
                    metadata, res = dbx.files_download(path=dropbox_path)
                    f.write(res.content)
            elif isinstance(entry, dropbox.files.FolderMetadata):
                # If it's a folder, recursively download its contents
                download_files(dropbox_path, local_path)
    except dropbox.exceptions.ApiError as err:
        print(f'Failed to list folder contents: {err}')
    except Exception as e:
        print(f'Error: {e}')


# Start the download process
download_files(DROPBOX_FOLDER_PATH, LOCAL_FOLDER_PATH)
