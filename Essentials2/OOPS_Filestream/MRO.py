"""
single inheritance
"""
class Top:
    def m_top(self):
        print("top")

class Middle(Top):
    def m_middle(self):
        print("middle")

class Bottom(Middle):
    def m_bottom(self):
        print("bottom")

object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()
###################################
"""
multiple inheritance
class Bottom(Middle, Top):
if we change order as 
class Bottom(Top, Middle):
python will throw error...order needs to be followed
"""
class Top:
    def m_top(self):
        print("top")

class Middle(Top):
    def m_middle(self):
        print("middle")

class Bottom(Middle, Top):
    def m_bottom(self):
        print("bottom")

object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()

#######################################
"""
class Bottom(Middle_Right, Middle_Left):
swapping 
class Bottom(Middle_Left,Middle_Right):
will have diff output for
object.m_middle()
"""
class Top:
    def m_top(self):
        print("top")

class Middle_Left(Top):
    def m_middle(self):
        print("middle_left")

class Middle_Right(Top):
    def m_middle(self):
        print("middle right")

class Bottom(Middle_Right, Middle_Left):
    def m_bottom(self):
        print("bottom")

object = Bottom()
object.m_bottom()
object.m_middle()
object.m_top()
