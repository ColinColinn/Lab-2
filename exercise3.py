def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    user_input = input()
    string_list = user_input.split(",")

    float_list = []
    for item in string_list:
        float_list.append(float(item))

    return float_list

def calc_average(temperature_list):
    print("calc_average")

def find_min_max(temperature_list):
    print("find_min_max")

def sort_temperature(temperature_list):
    print("sort_temperature")

def calc_median_temperature(temperature_list):
    print("calc_median_temperature")

def main():
    display_main_menu()
    temperature_list = get_user_input()
    print(temperature_list)
    calc_average(temperature_list)
    find_min_max(temperature_list)
    sort_temperature(temperature_list)
    calc_median_temperature(temperature_list)

if __name__ == "__main__":
    main()