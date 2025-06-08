from abc  import ABC , abstractmethod
class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass
class TextBox(UIControl):
    def draw(self):
        print('textbox')
class DropDown(UIControl):
    def draw(self):
        print('dropdown')
def draw(control):
    control.draw()
text1=TextBox()
d1=DropDown()
draw(text1)
draw(d1)