import dropbox
import os
class TransferData :
    def __init__(self,access_token):
        self.access_token = access_token
    def upload_files(self,file_to,file_from):
        dbx = dropbox.Dropbox(self.access_token)
        for root,dirs,files in os.walk(file_from)
        relative_path = os.path.relpath(local_path,file_from,'rb')
        dropbox_path = os.path.join(file_to,relative_path,'rb')
        with open(local_path,'rb') as f:
            dbx.files_upload(f.read(),dropbox_path,mode = WriteMode('overwrite'))
def main ():
    access_token = 'sl.BJv111HGbAQR8_4y01X3teonFHioFqA60bz7J2PSjcTExnDyUEzuIYC2h3K-uDqRmQarGtTbsfeA6P5E2vttHLtzoscTyWihKnqag8RlomuEz_GC6_Mkfw6jNtYtWVtakkc0toI'
    transferdata = Transferdata(access_token)
    file_from = input('Please enter file path to transfer: ')
    file_to = input('Please enter the full path to upload to dropbox')
    transferdata.upload_files(file_from,file_to)

    print('file has been moved')
main()
