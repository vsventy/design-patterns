# -*- coding: utf-8 -*-
"""
The facade pattern is used to define a simplified interface to a more complex
subsystem.
"""


class SkiRentSystem(object):
    """A Ski Rental System."""

    def rent_boots(self, feet_size, skier_level):
        return 20

    def rent_ski(self, weight, skier_level):
        return 40

    def rent_pole(self, height):
        return 5


class SkiResortTicketSystem(object):
    """A Ski Ticket System."""

    def buy_one_day_ticket(self):
        return 115

    def buy_half_day_ticket(self):
        return 60


class HotelBookingSystem(object):
    """A Hotel Reservation System."""

    def book_room(self, room_quality):
        if room_quality == 3:
            return 250
        elif room_quality == 4:
            return 500
        elif room_quality == 5:
            return 900
        else:
            raise ValueError('room_quality should be in range {3, 4, 5}')


class SkiRentFacade(object):
    """A Facade which provides access to all the systems mentioned above."""

    def __init__(self):
        self.__ski_rent_system = SkiRentSystem()
        self.__ski_resort_ticket_system = SkiResortTicketSystem()
        self.__hotel_booking_system = HotelBookingSystem()

    def have_good_rest(self, height, weight, feet_size, skier_level,
                       room_quality):
        ski_price = self.__ski_rent_system.rent_ski(weight, skier_level)
        ski_boots_price = self.__ski_rent_system.rent_boots(feet_size, skier_level)
        ski_pole_price = self.__ski_rent_system.rent_pole(height)
        one_day_ticket_price = self.__ski_resort_ticket_system.buy_one_day_ticket()
        hotel_price = self.__hotel_booking_system.book_room(room_quality)

        return (ski_price + ski_boots_price + ski_pole_price + hotel_price +
                one_day_ticket_price)

    def have_rest_with_own_skis(self):
        one_day_ticket_price = self.__ski_resort_ticket_system.buy_one_day_ticket()
        return one_day_ticket_price


def main():
    facade = SkiRentFacade()
    print(facade.have_good_rest(170, 70, 42, 10, 5))
    print(facade.have_rest_with_own_skis())

if __name__ == '__main__':
    main()
