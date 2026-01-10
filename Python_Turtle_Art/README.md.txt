# Turtle Art (Python)

A small Python project that creates colorful generative art using the built-in **turtle** module.  
Includes a simple **square spiral** (great for learning) and a more advanced **mandala/spirograph** style drawing.

## What’s inside
- **Square Spiral**: a growing spiral made from repeated forward + turn steps, cycling through colors.
- **Mandala/Spirograph**: a more complex pattern using math + smooth rainbow gradients.

## Requirements
- Python 3.x  
- No extra installs needed (uses Python’s built-in `turtle`)

> Note: On some Linux setups you may need Tkinter installed (because `turtle` uses it).

## How to run
1. Clone or download this repo
2. Run a script:

```bash
python spiral.py
or

bash
Copiar código
python mandala.py
(Use python3 instead of python if needed.)

Customize (easy tweaks)
Spiral
Change how many steps it draws:

range(300) → bigger/smaller drawing

Change the turning angle:

t.right(90) = square feel

t.right(89) or t.right(91) = drifting spiral / rosette

Change how fast the spiral grows:

distance += 3

Mandala / Spirograph
Try different parameters in:

draw_spiro(R, r, d, steps, ...)

Increase steps for smoother curves (slower)

Screenshots
Add a screenshot here (optional but recommended):

Create a folder called images/

Save a screenshot as images/preview.png

Then add this line:

markdown
Copiar código
![Preview](images/preview.png)