from bottle import route, run, template, static_file


@route('/api/master/<action>', method='post')
def master_switch(action):
    print "opening the file"
    f = open('mastervalve', 'w')   
    
    #open the files
    try:
         
        if 'on' == action:
            print "Writing a 1 to the file"
            #turn on
            f.write("1\n")
            
        elif 'off' == action:
            print "Writing a zero to the file"
            f.write("\n")
        else:
            raise RuntimeError("Unrecognised action: {action}".format(action=action))
    except:
        raise
    finally: #everything in a finally runs, whether the above succeeds or not
        print "closing the file"
        f.close()

@route('/')
def index():
    return static_file('index.html', root='static')



@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')

run(host='localhost', port=8080, devmode=True)