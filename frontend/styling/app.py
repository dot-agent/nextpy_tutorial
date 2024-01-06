# Nextpy Frontend 
## Styling in Nextpy

### Put this code to your blank template main page.

import nextpy as xt
from . import styles

def index() -> xt.Component:
    return xt.hstack(
        xt.box(
            xt.text(
                'Text Box 1',
                # Tailwind css 
                class_name='text-white font-bold'     
            ),
            # Inline css
            bg = 'black',                             
            style = styles.dimension                  
        ),
        xt.box(
            xt.text(
                'Text Box 2',
                color = 'white'
            ),
            bg = 'black',
            style=styles.dimension
        ),
        xt.center(
            xt.text('Center'),
            bg = 'yellow',
            style=styles.dimension
        ),
    )

# Passsing Global Style 
app = xt.App(style = styles.base_style) 
app.add_page(index)
