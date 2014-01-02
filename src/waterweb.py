from bottle import route, run, template, static_file


@route('/api/master/<action>', method='post')
def master_switch(action):
    if 'on' == action:
        #turn on
        pass
    elif 'off' == action:
        #turn off
        pass
    else:
        raise RuntimeError("Unrecognised action: {action}".format(action=action))
        
    return []

@route('/')
def index():
    return static_file('index.html', root='static')



@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='static')

run(host='localhost', port=8080, devmode=True)