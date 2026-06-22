from bmi_tool import calculate_bmi
from macro_tool import calculate_macros

def fitness_agent(weight,height,goal):

    bmi = calculate_bmi(weight,height)

    macros = calculate_macros(weight,goal)

    return {
        "BMI": bmi,
        "Macros": macros
    }