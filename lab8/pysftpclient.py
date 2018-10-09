import pysftp, sys
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
cinfo = {'cnopts':cnopts, 'host':'oz-ist-linux-fa18-411', 'username':'ChristopherValko', 'password':'Lkjhlkjh12', 'port':103}
try:
    with pysftp.Connection(**cinfo) as sftp:
        print("Connection made")
        try:
            print("getting payload.json file")
            sftp.get('/home/ftpuser/payload.json')
            sftp.remove('/home/ftpuser/payload.json')
        except:
            print("Log excpetion 1: ", sys.exc_info()[0])
except:
    print("Log exception 2: ", sys.exc_info()[0])
