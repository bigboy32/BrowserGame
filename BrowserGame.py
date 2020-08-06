import xml.etree.ElementTree as ET


class Webpage:
    def __init__(self, filename, render_template):
        self.filename = filename
        self.render_template = render_template

    def render(self):
        return self.render_template(self.filename)


class LoginScreen(Webpage):
    def __init__(self, filename, render_template, is_valid_func, session, nextScreen):

        super.__init__(filename, render_template)

        self.filename = filename
        self.render_template = render_template
        self.is_valid_func = is_valid_func
        self.session = session
        self.nextScreen = Webpage(nextScreen, self.render_template)

    def login(self, uname, password, hashfunc=None):

        if hashfunc != None:
            password = hashfunc(password)

        if self.is_valid_func(uname, password):
            self.session["LogedIn"] = True
            self.session["UserName"] = uname

            self.nextScreen.render()


class Shape:
    def __init__(self, color, location, mainPageFileName, Style=None):
        self.color = color
        self.location = location
        self.style = Style
        self.mainPageFile = open(mainPageFileName "r")
        self.mpfc = self.mainPageFile.read()
