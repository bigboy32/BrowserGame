import xml.etree.ElementTree as ET


class Webpage(object):
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


class Shape(object):
    def __init__(self, color, mainPageFileName, add_line_num, Style, shape, class_name):
        self.style = Style
        self.color = color
        self.mainPageFile = open(mainPageFileName, "r+")
        self.mpfc = self.mainPageFile.readlines()
        self.add_line_num = add_line_num + 1
        self.shape = shape
        self.class_name = class_name

    def _add(self, data, extra_whitespace=0):

        last_tag = self.mpfc[self.add_line_num - 2]
        whitespace = 0

        if "<div" in last_tag:
            whitespace += 4
        for item in last_tag:
            if item == " ":
                whitespace += 1

        return " " * (whitespace + extra_whitespace) + data

    def render(self):
        div_open = self._add("<div class='Shape'>")

        if self.style != None:
            content = self._add(
                f"<img src='Images/{self.shape}/{self.color}.png' class='{self.class_name}' style='{self.style}'>", 2)
        else:
            content = self._add(
                f"<img src='Images/{self.shape}/{self.color}.png' class='{self.class_name}'>", 2)

        div_close = self._add("<\div>")

        self.mpfc.insert(self.add_line_num, div_open)
        self.mpfc.insert(self.add_line_num + 1, content)
        self.mpfc.insert(self.add_line_num + 2, div_close)

        self.mainPageFile.writelines(self.mpfc)

    def display(self):
        return self.mainPageFile.readlines()


class Square(Shape):
    def __init__(self, filename, render_template, color, add_line_num, style=None, class_name="Square"):

        super(Square, self).__init__(color, filename, add_line_num,
                                     style, 'Square', class_name)

        self.filename = filename
        self.render_template = render_template
        self.color = color

        self.add_line_num = add_line_num
        self.class_name = class_name
        self.style = style

    # @override
    def display(self):
        super.render()

        return self.render_template(self.filename)


class Circle(Shape):
    def __init__(self, filename, render_template, color, add_line_num, style=None, class_name="Circle"):

        super(Circle, self).__init__(color, filename, add_line_num,
                                     style, 'Circle', class_name)

        self.filename = filename
        self.render_template = render_template
        self.color = color
        self.add_line_num = add_line_num
        self.class_name = class_name
        self.style = style

    # @override
    def display(self):
        super.render()

        return self.render_template(self.filename)


