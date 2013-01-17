import datetime
import os
import os.path
import sys
import zipfile
from dropbox import client, session

ACCESS_TYPE = 'app_folder'


if len(sys.argv) < 3:
    exit('not enough arguments')

if not os.path.exists(sys.argv[1]):
    exit('token file does not exists: ' + sys.argv[1])

print('reading tokens...')
with open(sys.argv[1]) as f:
    lines = f.readlines()
lines = [item.strip() for item in lines[:4]]
app_key, app_secret, token_key, token_secret = lines

if not os.path.isdir(sys.argv[2]):
    exit('source path is not a directory: ' + sys.argv[2])

src_dir = sys.argv[2].strip(os.path.sep + os.path.altsep)
ts = datetime.datetime.now().strftime("%Y%m%d%H%M")
zip_file = "%s_%s.zip" % (ts, os.path.basename(src_dir))

print("archiving '%s' to '%s'..." % (src_dir, zip_file))
with zipfile.ZipFile(zip_file, 'w') as z:
    for root, dirs, files in os.walk(sys.argv[2]):
        for file_name in files:
            full_path = os.path.join(root, file_name)
            print('  ' + full_path)
            z.write(full_path)

print('uploading to dropbox...')
sess = session.DropboxSession(app_key, app_secret, ACCESS_TYPE)
sess.set_token(token_key, token_secret)
client = client.DropboxClient(sess)
response = client.put_file('/' + zip_file, open(zip_file).read(),
                           overwrite=True, parent_rev=None)

os.unlink(zip_file)
print('done')
