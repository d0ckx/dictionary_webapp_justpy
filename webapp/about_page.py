import justpy as jp
from webapp import layout, page


class About(page.Page):
    path = "/about"

    def serve(self):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the about page.", classes="text-4xl m-2")
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

