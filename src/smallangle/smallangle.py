import click
import numpy as np
from numpy import pi
import pandas as pd

# creates group
@click.group()
def cmd_group():
    pass

# creates the sin command
@cmd_group.command()
# lets user pick how many steps it takes from 0 to 2pi with 10 as default
@click.option(
    "-n",
    "--number",
    default=10,
    help="number of steps from 0 to 2pi",
    show_default=True, #show default in help
)
# function that plots the results
def sin(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return

# code is an analogy of above
@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=10,
    help="number of steps from 0 to 2pi",
    show_default=True, #show default in help
)
def tan(number):
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return

if __name__ == "__main__":
    cmd_group()


