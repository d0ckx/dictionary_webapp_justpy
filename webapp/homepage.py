import justpy as jp

class Home:
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        layout = jp.QLayout(a=wp, view="hHh lpR fFf")
        header = jp.QHeader(a=layout)
        toolbar = jp.QToolbar(a=header)

        drawer = jp.QDrawer(a=layout, show_if_above=True, v_mode="left",
                            bordered=True)
        scroller = jp.QScrollArea(a=drawer, classes="fit")
        q_list = jp.QList(a=scroller)
        a_classes = "p-2 m-2 text-lg text-blue-400 hover:text-blue-700"
        jp.A(a=q_list, text="Home", href="/", classes=a_classes)
        jp.Br(a=q_list)
        jp.A(a=q_list, text="About", href="/about", classes=a_classes)
        jp.Br(a=q_list)
        jp.A(a=q_list, text="Dictionary", href="/dictionary", classes=a_classes)

        jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu",
                click=cls.move_drawer, drawer=drawer)
        jp.QToolbarTitle(a=toolbar, text="instant dictionary")

        container = jp.QPageContainer(a=layout)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen p-2")
        jp.Div(a=div, text="This is the home page.", classes="text-4xl m-2")
        jp.Div(a=div, text="""
        Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod 
        tempor incididunt ut labore et dolore magna aliqua. Molestie nunc non 
        blandit massa enim. Pretium lectus quam id leo in vitae turpis. Eget 
        egestas purus viverra accumsan in nisl nisi scelerisque eu. Gravida 
        cum sociis natoque penatibus et magnis dis. Velit euismod in pellentesque 
        massa placerat duis ultricies lacus sed. Integer eget aliquet nibh 
        praesent tristique magna sit amet purus. Neque vitae tempus quam 
        pellentesque nec nam. Tincidunt tortor aliquam nulla facilisi cras 
        fermentum. At in tellus integer feugiat scelerisque varius morbi enim. 
        Pretium quam vulputate dignissim suspendisse in est. Mauris commodo 
        quis imperdiet massa tincidunt nunc. Amet est placerat in egestas 
        erat imperdiet sed. Arcu bibendum at varius vel pharetra vel turpis nunc.
        """, classes="text-lg")
        return wp

    @staticmethod
    def move_drawer(widget, msg):
        if widget.drawer.value:
            widget.drawer.value = False
        else:
            widget.drawer.value = True


