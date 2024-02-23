from sympy import symbols, Eq, solve

class Support:
    def __init__(self, settlement, angular_displacement, equilibrium_equation, node_reaction):
        self.settlement = settlement
        self.angular_displacement = angular_displacement
        self.equilibrium_equation = equilibrium_equation
        self.node_reaction = node_reaction



class Span:
    def __init__(self, left_fem, right_fem, span_length, load, loading_condition, load_position, left_moment, right_moment, left_slope_deflection_equation, right_slope_deflection_equation, reaction_at_left_node_on_span, reaction_at_right_node_on_span, span_a_value, EI):
        self.left_fem = left_fem
        self.right_fem = right_fem
        self.span_length = span_length
        self.load = load
        self.loading_condition = loading_condition
        self.load_position = load_position
        self.left_moment = left_moment
        self.right_moment = right_moment
        self.left_slope_deflection_equation = left_slope_deflection_equation
        self.right_slope_deflection_equation = right_slope_deflection_equation
        self.reaction_at_left_node_on_span = reaction_at_left_node_on_span
        self.reaction_at_right_node_on_span = reaction_at_right_node_on_span
        self.span_a_value = span_a_value
        self.EI = EI

def calculate_fixed_end_moments(self):
    # """
    # Calculate the fixed-end moment for a simply supported beam with various loading conditions.

    # Parameters:
    # - span_length: Length of the beam.
    # - loading_condition: String indicating the loading condition.
    # - load_position: Position of the point load (required for some loading conditions).
    # - load: Magnitude of the point load (required for some loading conditions).

    # Returns:
    # - Fixed-end moment at the left and right ends.
    # """
    if self.loading_condition == "P_C":
        # Point load at the center
        self.left_fem = - (self.span_a_value * self.load)  / 8
        self.right_fem = (self.span_a_value * self.load) / 8
    elif self.loading_condition == "P_X":
        # Point load at a specified distance from the left end
        self.left_fem = - ((self.load * (self.span_length - self.load_position) ** 2) * self.load_position) / self.span_a_value ** 2
        self.right_fem = ((self.load * (self.load_position) ** 2) * (self.span_length - self.load_position)) / self.self.span_a_value ** 2
    elif self.loading_condition == "P_C_2":
        # Two equal point loads, spaced at 1/3 of the total length from each other
        self.left_fem = - (2 * self.load * self.span_a_value) / 9
        self.right_fem = (2 * self.load * self.span_a_value) / 9
    elif self.loading_condition == "P_C_3":
        # Three equal point loads, spaced at 1/4 of the total length from each other
        self.left_fem = - (15 * self.load * self.span_a_value) / 48
        self.right_fem = (15 * self.load * self.span_a_value) / 48
    elif self.loading_condition == "UDL":
        # Uniformly distributed load over the whole length
        self.left_fem = - (self.load * self.span_a_value ** 2) / 12
        self.right_fem = (self.load * self.span_a_value ** 2) / 12
    elif self.loading_condition == "UDL/2":
        # Uniformly distributed load over half the total length
        self.left_fem = - (11 * self.load * (self.span_a_value ** 2)) / 192
        self.right_fem = (5 * self.load * (self.span_a_value ** 2)) / 192
    elif self.loading_condition == "UVL":
        #Uniformly varying load
        self.left_fem = - (self.load * (self.span_a_value ** 2)) / 20
        self.right_fem = (self.load * (self.span_a_value ** 2)) / 30
    else:
        self.left_fem = 0
        self.right_fem = 0

    
    return self.left_fem, self.right_fem


def beam_analysis():
    supports = int(input("How many Supports: "))
    no_of_spans = supports - 1

    beam_support = []
    settlement_variable = 0
    angular_displacement_variable = 0
    equilibrium_equation_variable = ""
    node_reaction_variable = 0
    for i in range(supports):
        beam_support.append("")
        beam_support[i] = Support(settlement_variable, angular_displacement_variable, equilibrium_equation_variable,
                            node_reaction_variable)

    angular_displacements = []
    first_node = "A"
    for i in range(supports):
        if i != 0 and i != supports - 1:
            beam_support[i].angular_displacement = symbols(f"Theta_{first_node}")
            angular_displacements.append(beam_support[i].angular_displacement)
        else:
            beam_support[i].angular_displacement = symbols(f"Theta_{first_node}")
            beam_support[i].angular_displacement = 0

        first_node = chr(ord(first_node) + 1)





    left_fem_variable = 1
    right_fem_variable = 1
    load_variable = 1
    span_length_variable = 1
    loading_condition_variable = ""
    load_position = 1
    left_moment_variable = 1
    right_moment_variable = 1
    left_slope_deflection_equation_variable = 1
    right_slope_deflection_equation_variable = 1
    reaction_at_left_node_on_span_variable = 1
    reaction_at_right_node_on_span_variable = 1
    span_a_value_variable = 1
    EI_variable = 1
    

    beam_span = []
    for i in range(no_of_spans):
        beam_span.append("")
        beam_span[i] = Span(left_fem_variable, right_fem_variable, load_variable, span_length_variable, loading_condition_variable, load_position, left_moment_variable, right_moment_variable, left_slope_deflection_equation_variable, right_slope_deflection_equation_variable, reaction_at_left_node_on_span_variable, reaction_at_right_node_on_span_variable, span_a_value_variable, EI_variable)

    print("Key words for loading condition:"
      "\nNo loading on span (none)"
      "\nPoint load at center (P_C)"
      "\nPoint load at distance 'a' from left end and 'b' from the right end (P_X)"
      "\nTwo equal point loads, spaced at 1/3 of the total length from each other (P_C_2)"
      "\nThree equal point loads, spaced at 1/4 of the total length from each other (P_C_3)"
      "\nUniformly distributed load over the whole length (UDL)"
      "\nUniformly distributed load over half of the span on the left side (UDL/2_L)"
      "\nVariably distributed load, with highest point on the left end (VDL_L)")
    
    beam_length = 0

    for i in range(no_of_spans):
        beam_span[i].loading_condition = input(f"What is the nature of loading on span {i + 1}: ")
        beam_span[i].span_a_value = int(input(f"What is the length of span {i + 1}: "))
        beam_span[i].load = int(input(f"What is the magnitude of load on span {i + 1}: "))
        if beam_span[i].loading_condition == "P_X":
            beam_span[i].load_position = int(input(f"What is the distance to the load on span {i + 1}: "))
        else:
            beam_span[i].load_position = beam_span[i].span_length / 2

        
        beam_length += beam_span[i].span_length

        beam_span[i].left_fem, beam_span[i].right_fem = calculate_fixed_end_moments(beam_span[i])

    
    list_of_end_moments = []
    left_end = "a"
    right_end = "b"
    for i in range(no_of_spans):
        beam_span[i].left_moment, beam_span[i].right_moment = symbols(f"M{left_end}{right_end} M{right_end}{left_end}")
        left_end = chr(ord(left_end) + 1)
        right_end = chr(ord(right_end) + 1)
        list_of_end_moments.append(beam_span[i].left_moment)
        list_of_end_moments.append(beam_span[i].right_moment)

    slope_equations = []


    for i in range(no_of_spans):
        EI = "EI"
        beam_span[i].EI = symbols(f"{EI}")
        if i == 0:
            beam_span[i].left_slope_deflection_equation = Eq(beam_span[i].left_fem + ((2 * beam_span[i].EI) / beam_span[i].span_a_value) * (beam_support[i + 1].angular_displacement), beam_span[i].left_moment)
            beam_span[i].right_slope_deflection_equation = Eq(beam_span[i].right_fem + ((2 * beam_span[i].EI) / beam_span[i].span_a_value) * ((2 * beam_support[i + 1].angular_displacement)), beam_span[i].right_moment)
        elif i == no_of_spans - 1:
            beam_span[i].left_slope_deflection_equation = Eq(beam_span[i].left_fem + ((2 * beam_span[i].EI) / beam_span[i].span_a_value) * ((beam_support[i].angular_displacement * 2)), beam_span[i].left_moment)
            beam_span[i].right_slope_deflection_equation = Eq(beam_span[i].right_fem + ((2 * beam_span[i].EI) / beam_span[i].span_a_value) * (beam_support[i].angular_displacement), beam_span[i].right_moment)
        else:
            beam_span[i].left_slope_deflection_equation = Eq(beam_span[i].left_fem + ((2 * beam_span[i].EI) / beam_span[i].span_a_value) * ((beam_support[i].angular_displacement * 2) + beam_support[i + 1].angular_displacement), beam_span[i].left_moment)
            beam_span[i].right_slope_deflection_equation = Eq(beam_span[i].right_fem + ((2 * beam_span[i].EI) / beam_span[i].span_a_value) * (beam_support[i].angular_displacement +(2 * beam_support[i + 1].angular_displacement)), beam_span[i].right_moment)

        slope_equations.append(beam_span[i].left_slope_deflection_equation)
        slope_equations.append(beam_span[i].right_slope_deflection_equation)

    equilibrium_equations = []
    for i in range(supports):
        if i != 0 and i != supports - 1:
            beam_support[i].equilibrium_equation = Eq(beam_span[i - 1].right_moment + beam_span[i].left_moment, 0)
        else:
            beam_support[i].equilibrium_equation = 0

        equilibrium_equations.append(beam_support[i].equilibrium_equation)
    
        # store the equations and the unknowns in lists
    equations = slope_equations + equilibrium_equations
    unknowns = list_of_end_moments + angular_displacements

    # next is to solve all the equations for the unknown moments and angular displacement
    solution = solve(tuple(equations), tuple(unknowns))

    print(equations)
    print(solution)
    print(solution[beam_span[0].left_moment])
    print(list_of_end_moments)


    for i in range(no_of_spans):
        if beam_span[i].loading_condition == "P_C":
            beam_span[i].reaction_at_right_node_on_span = ((solution[beam_span[i].left_moment] + solution[beam_span[i].right_moment] + (
                    beam_span[i].load * (beam_span[i].span_length / 2))) / beam_span[i].span_length)
            beam_span[i].reaction_at_left_node_on_span = beam_span[i].load - beam_span[i].reaction_at_right_node_on_span

        elif beam_span[i].loading_condition == "P_X":
            a = beam_span[i].span_a_value
            beam_span[i].reaction_at_right_node_on_span = (
                    (solution[beam_span[i].left_moment] + solution[beam_span[i].right_moment] + (beam_span[i].load * a)) / beam_span[
                i].span_length)
            beam_span[i].reaction_at_left_node_on_span = beam_span[i].load - beam_span[i].reaction_at_right_node_on_span

        elif beam_span[i].loading_condition == "P_C_2":
            beam_span[i].reaction_at_right_node_on_span = ((solution[beam_span[i].left_moment] + solution[beam_span[i].right_moment] + (
                    beam_span[i].load * ((2 * beam_span[i].span_length) / 3)) + (beam_span[i].load * (
                    beam_span[i].span_length / 3))) / beam_span[i].span_length)
            beam_span[i].reaction_at_left_node_on_span = 2 * beam_span[i].load - beam_span[
                i].reaction_at_right_node_on_span

        elif beam_span[i].loading_condition == "P_C_3":
            beam_span[i].reaction_at_right_node_on_span = ((solution[beam_span[i].left_moment] + solution[beam_span[i].right_moment] + (
                    beam_span[i].load * ((3 * beam_span[i].span_length) / 4)) + (beam_span[i].load *
                                                                                ((2 * beam_span[
                                                                                    i].span_length) / 4)) + (
                                                                    beam_span[i].load * (
                                                                    beam_span[i].span_length / 4))) /
                                                            beam_span[i].span_length)
            beam_span[i].reaction_at_left_node_on_span = 3 * beam_span[i].load - beam_span[
                i].reaction_at_right_node_on_span

        elif beam_span[i].loading_condition == "UDL":
            beam_span[i].reaction_at_right_node_on_span = ((solution[beam_span[i].left_moment] + solution[beam_span[i].right_moment] + (
                    beam_span[i].load * ((beam_span[i].span_length * beam_span[i].span_length) / 2))) / beam_span[
                                                                i].span_length)
            beam_span[i].reaction_at_left_node_on_span = (beam_span[i].load * beam_span[i].span_length) - beam_span[
                i].reaction_at_right_node_on_span

        elif beam_span[i].loading_condition == "UDL/2_R":
            beam_span[i].reaction_at_right_node_on_span = ((solution[beam_span[i].left_moment] + solution[beam_span[i].right_moment] + (
                    beam_span[i].load * ((3 * beam_span[i].span_length * beam_span[i].span_length) / 8))) /
                                                            beam_span[i].span_length)
            beam_span[i].reaction_at_left_node_on_span = ((beam_span[i].load * beam_span[i].span_length) / 2) - \
                                                        beam_span[i].reaction_at_right_node_on_span

        elif beam_span[i].loading_condition == "UDL/2_L":
            beam_span[i].reaction_at_right_node_on_span = ((solution[beam_span[i].left_moment] + solution[beam_span[i].right_moment] + (
                    beam_span[i].load * ((beam_span[i].span_length * beam_span[i].span_length) / 8))) / beam_span[
                                                                i].span_length)
            beam_span[i].reaction_at_left_node_on_span = ((beam_span[i].load * beam_span[i].span_length) / 2) - \
                                                        beam_span[i].reaction_at_right_node_on_span

        elif beam_span[i].loading_condition == "VDL_R":
            beam_span[i].reaction_at_right_node_on_span = ((solution[beam_span[i].left_moment] + solution[beam_span[i].right_moment] + (
                    beam_span[i].load * ((2 * beam_span[i].span_length * beam_span[i].span_length) / 6))) /
                                                            beam_span[i].span_length)
            beam_span[i].reaction_at_left_node_on_span = ((beam_span[i].load * beam_span[i].span_length) / 2) - \
                                                        beam_span[i].reaction_at_right_node_on_span

        elif beam_span[i].loading_condition == "VDL_L":
            beam_span[i].reaction_at_right_node_on_span = ((solution[beam_span[i].left_moment] + solution[beam_span[i].right_moment] + (
                    beam_span[i].load * ((beam_span[i].span_length * beam_span[i].span_length) / 6))) / beam_span[
                                                                i].span_length)
            beam_span[i].reaction_at_left_node_on_span = ((beam_span[i].load * beam_span[i].span_length) / 2) - \
                                                        beam_span[i].reaction_at_right_node_on_span

    for i in range(no_of_spans):
        print(beam_span[i].reaction_at_left_node_on_span)
        print(beam_span[i].reaction_at_right_node_on_span)
        # print(f"{ans}")

    print(" ")

        # next is to get the reaction for each beam node
    for i in range(supports):
        if i == 0:
            beam_support[i].node_reaction = beam_span[i].reaction_at_left_node_on_span

        elif i == supports - 1:
            beam_support[i].node_reaction = beam_span[i - 1].reaction_at_right_node_on_span

        else:
            beam_support[i].node_reaction = beam_span[i-1].reaction_at_right_node_on_span + beam_span[i].reaction_at_left_node_on_span

   
    for i in range(supports):
        print(beam_support[i].node_reaction)
    

    # calculate_fixed_end_moments(beam_span)
    # calculate_reactions(beam_span)
    # position_along_beam, shear_forces = calculate_shear_forces(beam_span, beam_support)
    # # Uncomment the line below if you want to plot the shear forces
    # # plot_shear_forces(position_along_beam, shear_forces)


if __name__ == "__main__":
    beam_analysis()
