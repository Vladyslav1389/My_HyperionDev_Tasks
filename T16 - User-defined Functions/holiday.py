"""
This program calculates a user’s total holiday cost, which includes the
plane cost, hotel cost, and car-rental cost.
"""
import os


def clear_screen():
    """Clear the console screen"""
    os.system("cls||clear")


def list_of_available_cities() -> None:
    """
    The function prints a list of available cities for a holiday.
    """
    title = "===Available cities for your holiday==="
    print(title)
    line_print(symbol='-', length=len(title))
    print("1. Paris")
    print("2. Rome")
    print("3. Berlin")
    print("4. New York")
    line_print()


def get_user_city_choice() -> str:
    """
    The function prompts the user to enter a number from 1 to 4 representing a
    city choice for a flight, validates the input, and returns number of the
    chosen city as a string.
    :return: a string representing the user's choice of city to fly to.
    :rtype: str
    """
    try:
        city_flight = input("Please enter the city you will be flying to. Enter"
                            " number from 1 to 4: ")
        city_flight_int = int(city_flight)
        if 1 <= city_flight_int <= 4:
            return str(city_flight)
        else:
            raise ValueError("Invalid choice. Try again:")
    except ValueError as error_msg:
        print(f"Error: {error_msg}")
        line_print(symbol='-')
        return get_user_city_choice()


def get_user_input_int(message: str) -> int:
    """
    The function `get_user_input_int` prompts the user for an integer input,
    validates that the input is a non-negative integer, and recursively calls
    itself if the input is invalid.
    
    :param message: The `message` parameter is a string that represents the
    prompt or message that will be displayed to the user when asking for input.
    :type message: str
    :return: The function returns an integer value that the user inputs.
    :rtype: int
    """
    try:
        user_input = int(input(message))
        if user_input >= 0:
            return user_input
        else:
            raise ValueError("Sorry, but the number can not be negative.")
    except ValueError as error_msg:
        print(f"Invalid input! Error: {error_msg}")
        line_print(symbol='-')
        return get_user_input_int(message)


def get_car_rental_days(car_rent_message:  str, num_nights: int) -> int:
    """
    The function takes a car rental message and the number of nights in a hotel
    stay as input, prompts the user for the number of days to rent a car, and
    returns the number of car rental days as long as it is not greater than the
    number of hotel nights.
    
    :param car_rent_message: A string that prompts the user to enter the number
    of days they want to rent a car
    :type car_rent_message: str
    :param num_nights: The number of nights the user will be staying at the hotel.
    :type num_nights: int
    :return: value, which represents the number of days to rent a car.
    :rtype: int
    """
    car_rent_days = get_user_input_int(car_rent_message)
    if car_rent_days > num_nights:
        print("The number of days to rent a car can not be more than the number"
              " of nights in the hotel. Please enter a valid number.")
        return get_car_rental_days(car_rent_message, num_nights)
    return car_rent_days


def hotel_cost(num_nights_parametr: int, city: str) -> int:
    """
    The function calculates the total cost of a hotel stay based on the number
    of nights and the price per night cost.
    
    :param num_nights_parametr: The number of nights the person will be staying
    at the hotel.
    :type num_nights_parametr: int
    :param city: Represents the choosen city. Represented by the numbers 1 to 4.
    :type city: str
    :return: the total cost of the hotel stay.
    :rtype: int
    """
    if city == '1':
        price_per_night = 60
    elif city == '2':
        price_per_night = 80
    elif city == '3':
        price_per_night = 70
    elif city == '4':
        price_per_night = 90

    total_hotel_cost = num_nights_parametr * price_per_night
    return total_hotel_cost


def plane_cost(city_flight_in_plane_cost: str) -> int:
    """
    Takes a string representing a city flight option and returns the
    corresponding cost of the flight.
    
    :param city_flight_in_plane_cost: Represents the cost of a flight in a 
    plane for a specific city.
    :type city_flight_in_plane_cost: str
    :return: the price for the flight based on the input.
    :rtype: int
    """
    if city_flight_in_plane_cost == '1':
        price_for_flight = 40
    elif city_flight_in_plane_cost == '2':
        price_for_flight = 60
    elif city_flight_in_plane_cost == '3':
        price_for_flight = 50
    elif city_flight_in_plane_cost == '4':
        price_for_flight = 300
    return price_for_flight


def car_rental(rental_days: int) -> int:
    """
    The function calculates the total cost of renting a car based on the number
    of rental days.
    
    :param rental_days: The number of days the car is rented.
    :type rental_days: int
    :return: the total rental cost, which is an integer value.
    :rtype: int
    """
    daily_rental_cost = 13
    total_rental_cost = daily_rental_cost * rental_days
    return total_rental_cost


def holiday_cost(hotel_cost: int, plane_cost: int, car_rent: int) -> int:
    """
    The function calculates the total cost of a holiday by adding the costs of 
    a hotel, plane, and car rental.
    
    :param hotel_cost: The cost of the hotel for the holiday
    :type hotel_cost: int
    :param plane_cost: The cost of the plane ticket for the holiday
    :type plane_cost: int
    :param car_rent: The cost of renting a car for the holiday
    :type car_rent: int
    :return: the total cost of the holiday, which is the sum of the hotel cost,
    plane cost, and car rent cost.
    """
    holiday_total_cost = hotel_cost + plane_cost + car_rent
    return holiday_total_cost


def line_print(symbol='=', length=79) -> None:
    """
    Prints a line of a specified length using a specified symbol.
    
    :param symbol: The symbol parameter is a string that represents the character
    that will be repeated to create the line. By default, it is set to '=',
    defaults to = (optional)
    :type symbol: str
    :param length: The length parameter determines the number of times the symbol
    character will be printed in the line, defaults to 79 (optional)
    :type length: int
    """
    print(symbol*length)


def main():
    """
    The main function calculates and displays the total cost of a holiday,
    including flight, hotel, and car rental expenses.
    """
    clear_screen()
    list_of_available_cities()

    # User input.
    city_flight = get_user_city_choice()
    message_for_num_nights = ("Please enter the number of nights you will stay"
                            " at the hotel: ")
    num_nights = get_user_input_int(message_for_num_nights)
    car_rental_days_message = ("Please enter the number of days for which you"
                            " will hire a car: ")
    car_rental_days = get_car_rental_days(car_rental_days_message, num_nights)

    # Calculating the total cost of the hotel, plane, and car rental for the
    # user's holiday.
    total_hotel_cost = hotel_cost(num_nights, city_flight)
    cost_flight = plane_cost(city_flight)
    total_car_rental_cost = car_rental(car_rental_days)

    # Calculating the total cost of the user's holiday.
    total_holiday_cost = holiday_cost(total_hotel_cost, cost_flight,
                                total_car_rental_cost)

    # Displaying the result on the screen.
    clear_screen()
    line_print()
    print(f"In total you will spend on your holiday {total_holiday_cost} pounds"
          f" for {num_nights} nights.")
    line_print()
    print("This includes:")
    print(f"flight costs: {cost_flight} pounds,")
    print(f"hotel cost: {total_hotel_cost} pounds for {num_nights} nights,")
    print(f"car rent: {total_car_rental_cost} pounds for {car_rental_days} days.")
    line_print()
    line_print(symbol='-')
    print("We wish you a pleasant holiday!")
    line_print(symbol='-')


main()
