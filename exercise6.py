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
    average=sum(temperature_list)/len(temperature_list)
    return average

def find_min_max(temperature_list):
    min_temp=min(temperature_list)
    max_temp=max(temperature_list)
    return[min_temp,max_temp]

def sort_temperature(temperature_list):
    return sorted(temperature_list)

def calc_median_temperature(temperature_list):
    sorted_list = sort_temperature(temperature_list)
    n = len(sorted_list)
    middle = n // 2

    if n % 2 == 1:      # odd count
        median = sorted_list[middle]
    else:               # even count
        median = (sorted_list[middle - 1] + sorted_list[middle]) / 2

    return median

def main():
    display_main_menu()
    temperature_list = get_user_input()
    print(temperature_list)
    
    average=calc_average(temperature_list)
    print("Average ="+str(average))
    
    min_max=find_min_max(temperature_list)
    print("Min ="+str(min_max[0]))
    print("Max ="+str(min_max[1]))
    
    sorted_list = sort_temperature(temperature_list)
    print("Sorted = " + str(sorted_list))

    median = calc_median_temperature(temperature_list)
    print("Median = " + str(median))

if __name__ == "__main__":
    main()