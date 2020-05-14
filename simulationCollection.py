from InteractionOwnLibrary import GraphDescription, VariableDescription

#######################################################################################################################
###################################### Heat flux graph description creation ###########################################
#######################################################################################################################


def heat_flux_graph_inital_values(A1=1, A2=10, e1=0.4, T1=275, T2=280, emissivity_step_nb=500):
    points = []
    x_axis = []
    sigma = 5.6704 * pow(10, -8)
    for epsilon2 in range(emissivity_step_nb):
        e2 = (epsilon2 + 1) / emissivity_step_nb
        x_axis.append(e2)
        if A1 < A2:
            points.append((A1 * sigma * (pow(T1, 4) - pow(T2, 4))) / (1 / e1 + (A1 / A2 * (1 / e2 - 1))))
        else:
            points.append(-1)
    return x_axis, points


heat_flux_graph_variables = [VariableDescription("temperature1", "Outer temperature [K]", 275, 350, 0.1, 275),
                             VariableDescription("temperature2", "Inner temperature [K]", 275, 350, 0.1, 280),
                             VariableDescription("emissivity1", "Inner ε", 0, 1, 0.002, 0.4),
                             VariableDescription("area1", "Inner area1 [m²]", 1, 10, 0.1, 1),
                             VariableDescription("area2", "Outer area [m²]", 1, 10, 0.1, 10)]

heat_flux_graph_formula = """
        var data = source.data;
        var A1 = area1.value;
        var A2 = area2.value;
        area1.end=A2-area2.step
        if(A1 >= A2){ A1 = A2-area2.step; area1.value = A2-area2.step;}
        var e1 = emissivity1.value;
        var T1 = temperature1.value;
        var T2 = temperature2.value;
        var sigma = 5.6704*Math.pow(10, -8);
        var x = data['x'];
        var y = data['y'];
        for (var i = 0; i < 500; i++) {
            var e2 = (i+1)/500;
            if (A1 < A2){
                y[i] = (A1 * sigma * (Math.pow(T1, 4) - Math.pow(T2, 4)))/(1/e1 + (A1/A2 * (1/e2 - 1)));
            }else{
                y[i] = -1
            }
        }

        // necessary becasue we mutated source.data in-place
        source.change.emit();
    """

heat_flux_graph_description = GraphDescription(heat_flux_graph_variables, heat_flux_graph_formula,
                                               heat_flux_graph_inital_values(), [0, 1], [-10, 0],
                                               "Heat flux value graph", 400, 600, "Outer ε", "Heat flux value []")
