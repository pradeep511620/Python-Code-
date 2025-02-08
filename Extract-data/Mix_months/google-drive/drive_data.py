import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # this will open a web page in your default browser to authenticate

drive = GoogleDrive(gauth)

folder_id = '1XXE2eF-In6UrLVtdukZA-di7mDMkhjxX' # ID of the folder in Google Drive where you want to upload your local folder


def upload_folder_to_drive(folder_path, parent_folder_id):
    # Create a new folder in Google Drive with the name of the local folder
    print(folder_path)
    drive_file1 = drive.CreateFile({'title': "raptor_data", 'parents': [{'id': parent_folder_id}], 'mimeType': 'application/vnd.google-apps.folder'})
    drive_file1.Upload()

    # Upload all files in the local folder to the Google Drive folder
    for filename in os.listdir(folder_path):
        print(filename)
        file_path = os.path.join(folder_path, filename)+"/"
        print(file_path)
        print(os.path.isfile(file_path+"/"))
        if os.path.isfile(file_path) is False:
            print(filename)
            drive_file = drive.CreateFile({'title': filename, 'parents': [{'id': drive_file1['id']}], 'mimeType': 'application/vnd.google-apps.folder'})
            drive_file.Upload()
            print(f'File "{filename}" uploaded successfully to Google Drive')
        for fi in os.listdir(file_path):
            print(fi)
            file = os.path.join(file_path, fi)
            drive_file = drive.CreateFile({'title': fi, 'parents': [{'id': drive_file['id']}]})
            drive_file.SetContentFile(file)
            drive_file.Upload()




# Call the function with the path of the local folder you want to upload and the ID of the parent folder in Google Drive
folder_path = "/var/www/html/mage/rfq/data" # replace this with the path of the local folder you want to upload

# Local directory to upload
local_dir = '/var/www/html/mage/rfq/data/'

# ID of the parent folder in Google Drive to upload the files and folders to
parent_folder_id = '1XXE2eF-In6UrLVtdukZA-di7mDMkhjxX'

# Function to upload all files and folders in a local directory recursively
def upload_folder_to_drive(local_dir, parent_folder):
    # List all items in the local directory
    items = os.listdir(local_dir)

    for item in items:
        item_path = os.path.join(local_dir, item)

        # If item is a file, upload it to Google Drive
        if os.path.isfile(item_path):
            file = drive.CreateFile({'title': item, 'parents': [{'id': parent_folder.get('id')}]})
            file.Upload()
            print('Uploaded file: %s' % item)

        # If item is a directory, create a new folder in Google Drive and upload its contents recursively
        elif os.path.isdir(item_path):
            folder = drive.CreateFile({'title': item, 'mimeType': 'application/vnd.google-apps.folder', 'parents': [{'id': parent_folder.get('id')}]})
            folder.Upload()
            print('Created folder: %s' % item)
            upload_folder_to_drive(item_path, folder)

# Upload all files and folders in the local directory to Google Drive
parent_folder = drive.CreateFile({'id': parent_folder_id})
upload_folder_to_drive(local_dir, parent_folder)

#upload_folder_to_drive(folder_path, folder_id)