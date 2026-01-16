from app.cinema.hall import CinemaHall
from app.cinema.bar import CinemaBar
from app.people.customer import Customer
from app.people.cinema_staff import Cleaner


def cinema_visit(movie: str, customers: list, hall: int, cleaner: str) -> None:
    customers_list = []
    for customer in customers:
        new_customer = Customer(customer["name"], customer["food"])
        customers_list.append(new_customer)
        CinemaBar.sell_product(customer["food"], new_customer)
    cinema_hall = CinemaHall(hall)
    clean_staff = Cleaner(cleaner)
    cinema_hall.movie_session(movie, customers_list, clean_staff)
