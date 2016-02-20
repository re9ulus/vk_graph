from bottle import route, run, template

@route('/test/<name>')
def index(name):
    return template('<i>Hello {{name}}</i>!', name=name)

run(host='localhost', port=8088)
