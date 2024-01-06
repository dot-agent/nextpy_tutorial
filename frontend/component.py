# Nextpy Frontend 
## Styling in Nextpy
### Put this code to your blank template main page.

import nextpy as xt

def another_component() -> xt.Component:
    return xt.hstack(
        xt.box(
            bg = 'green',
            height = '30vh',
            width = '30vh'
        ),
        xt.box(
            bg = 'red',
            height = '30vh',
            width = '30vh'
        )
    )

def index() -> xt.Component:
    return xt.fragment(
        xt.box(
            xt.text(
                'Text in box',
                color = 'white'
            ),
            bg = 'black',
            height = '40vh',
            width = '40vh'
        ),
        another_component(),
        xt.center(
            xt.text('Center'),
            bg = 'yellow',
            height = '50vh',
            width = '50vh'
        )
    )

app = xt.App()
app.add_page(index)
