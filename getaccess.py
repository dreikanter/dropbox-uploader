import sys
import os.path
from dropbox.session import DropboxSession


if len(sys.argv) < 2:
    print("usage: %s <dropbox-api-key> <dropbox-api-secret> <output-file-name>\n" % os.path.basename(__file__))
    exit('not enough arguments')

app_key = sys.argv[1]
app_secret = sys.argv[2]
# should be 'dropbox' or 'app_folder' as configured for your app
access_type = 'app_folder'

file_name = sys.argv[3]

session = DropboxSession(app_key, app_secret, access_type)
request_token = session.obtain_request_token()
url = session.build_authorize_url(request_token)
print "url:", url
print "Please visit this website and press the 'Allow' button, then hit 'Enter' here."
raw_input()
access_token = session.obtain_access_token(request_token)

lines = [app_key, app_secret, access_token.key, access_token.secret]
with open(file_name, 'w') as f:
    f.write("\n".join(lines))

print('done')
