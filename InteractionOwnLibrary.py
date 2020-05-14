import random
from bokeh.io import show
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, CustomJS, Slider
from bokeh.plotting import figure
from IPython.display import Image, display, clear_output, HTML
from ipywidgets import widgets


class VariableDescription:
    def __init__(self, name, description: str, min_value: float, max_value: float, step_size: float, init_value: float):
        self.name = name
        self.description = description
        self.min_value = min_value
        self.max_value = max_value
        self.step_size = step_size
        self.init_value = init_value
        self.slider = None


class GraphDescription:
    def __init__(self, variables: [VariableDescription], js_formula,
                 first_graph_values, x_range, y_range,
                 description: str, height: int, width: int,
                 x_label: str, y_label: str):
        self.variables = variables
        self.jsFormula = js_formula
        self.first_graph_values = first_graph_values
        self.x_range = x_range
        self.y_range = y_range
        self.description = description
        self.height = height
        self.width = width
        self.x_label = x_label
        self.y_label = y_label


def create_simulation_from_description(gd: GraphDescription):
    args_dict = {}
    slider_list = []
    for v in gd.variables:
        v.slider = Slider(title=v.description, value=v.init_value, start=v.min_value,
                          end=v.max_value, step=v.step_size)
        args_dict[v.name] = v.slider
        slider_list.append(v.slider)
    # Set up the plot
    x, y = gd.first_graph_values
    source = ColumnDataSource(data=dict(x=x, y=y))
    args_dict["source"] = source
    plot = figure(plot_height=400, plot_width=600, title=gd.description,
                  tools="pan,wheel_zoom",
                  x_range=gd.x_range, y_range=gd.y_range
                  )

    plot.xaxis.axis_label = gd.x_label
    plot.yaxis.axis_label = gd.y_label

    plot.line("x", "y", source=source, line_width=3, line_alpha=0.6)

    # Set the js update function
    update_curve = CustomJS(args=args_dict, code=gd.jsFormula)

    # Set Listeners on the sliders
    for w in slider_list:
        w.js_on_change('value', update_curve)

    # Set up layouts and add to document
    inputs = column(slider_list)
    layout = row(plot, inputs)
    show(layout)


def MCQ(question: str, choices: [str], correct: str):
    random.shuffle(choices)
    buttons = []
    display(HTML("<h3>"+question+"</h3>"))
    for choice in choices:
        buttons.append(widgets.Button(description=choice))
    container = widgets.HBox(children=buttons)

    def on_button_clicked(b):
        container.close()
        clear_output()
        if b.description == correct:
            print("Hourray, you found the right answer!")
        else:
            print("Well, that actually wasn't the right answer")
    for b in buttons:
        b.on_click(on_button_clicked)
    display(container)
