def calculate_macros(weight,goal):

    if goal.lower()=="fat loss":

        return {
            "Calories":1800,
            "Protein":"130g",
            "Carbs":"160g",
            "Fat":"50g"
        }

    return {
        "Calories":2200,
        "Protein":"140g",
        "Carbs":"250g",
        "Fat":"60g"
    }