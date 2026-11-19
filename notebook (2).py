import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium", auto_download=["html"])


@app.cell
def _():
    import marimo as mo
    import statistics as stats
    ###Start of notebook 1 (notebooks)

    #asks for help
    help(sorted)
    i = 0
    list = [5, 2, 8, 6, 7, 21, 1, 9]
    sorted(list)

    #random function to test while
    while i<8:
        print(list[i])
        i=i+1
    reverse_list=sorted(list, reverse=True)

    print(reverse_list)

    #prints uppercase
    mo.md("""**Hello world**"""
         """* how is it going?*""")

    ##mean, median and mode of list

    mean_val = stats.mean(list)
    median_val = stats.median(list)
    mode_val = stats.mode(list)
    print(mean_val, median_val, mode_val)

    ###Start of notebook 2 (Variables)

    #First name + year
    first_name = "Your Name"

    year = 2026

    #Finding time in min
    _time_seconds = 120

    _time_minutes = _time_seconds / 60

    print(f"The time is {_time_minutes} min.")

    #Min to sec
    _time_minutes = 42

    _time_seconds = _time_minutes * 60

    print(f"The other time is {_time_seconds} s.")
    #Energy calc through E = m c^2
    _mass = 1.6

    _light_speed = 3.0e8

    _energy = _mass * _light_speed ** 2

    print(f"Energy is {_energy}.")

    #String
    answer = "5"

    print(f"Multiplying a string: {answer * 2}")
    print(f"Converting to float: {float(answer)*2}")

    #Difference of coordinates
    coords1 = [1, 1, 1]

    coords2 = [3, 4, 5]

    dx = coords1[0] - coords2[0]

    dy = coords1[1] - coords2[1]

    dz = coords1[2] - coords2[2]

    ###Start of notebook 3 (Functions)

    ###Start of notebook 4 (Flow)
    return


if __name__ == "__main__":
    app.run()
