from app.people.customer import Customer


class CinemaBar:
    def __init__(self):
        pass

    @staticmethod
    def sell_product(customer: Customer, product: str) -> str:
        print(f"Cinema bar sold {product} to {customer.name}")
