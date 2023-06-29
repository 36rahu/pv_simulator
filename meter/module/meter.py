import random


class Meter:
    """
    A class representing a meter.

    Methods:
        generate_value: Generates a random consumption value.

    """

    def generate_value(self):
        """
        Generates a random consumption value.

        Returns:
            dict: A dictionary containing the generated consumption value.

        Example:
            {"consumption": 2.3456}
        """
        return {
            "consumption": round(random.uniform(0.0, 9.0), 4)
            }
