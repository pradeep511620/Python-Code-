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
    drive_file1 = drive.CreateFile({'title': "data", 'parents': [{'id': parent_folder_id}], 'mimeType': 'application/vnd.google-apps.folder'})
    drive_file1.Upload()

    # Upload all files in the local folder to the Google Drive folder
    for filename in os.listdir(folder_path):
        print(filename)
        file_path = os.path.join(folder_path, filename)+"/" + "/"
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
folder_path = "E:/images"    # replace this with the path of the local folder you want to upload
upload_folder_to_drive(folder_path, folder_id)


# import os
#
# from pydrive.auth import GoogleAuth
# from pydrive.drive import GoogleDrive
#
# gauth = GoogleAuth()
# drive = GoogleDrive(gauth)
#
# # '1UqZbHUCfp4e_Na5ZwljOyrkCOWDogGbt' pk.s511620  # 14w25a__35hrD1xHeNLY14RTYXg4C8vB4 pk.s7723337
#
# folder = '1XXE2eF-In6UrLVtdukZA-di7mDMkhjxX'
#
#
# # Single files uploaded
#
#
# def single_files():
#     file1 = drive.CreateFile({'parents': [{'id': folder}], 'title': 'hello.txt'})
#     file1.SetContentString('Hello world!')
#     file1.Upload()
#     print("files uploaded successfully", file1)
#
#
# single_files()

