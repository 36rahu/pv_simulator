from datetime import datetime


class PVSimulator:
    """
    PVSimulator class for simulating PV values.

    Attributes:
        hour_vs_pv_value (dict): A dictionary mapping each hour to its corresponding PV value.

    Methods:
        pv_value_and_ts(): Calculates the PV value and timestamp based on the current time.

    """
    hour_vs_pv_value = {
                    4: 0.1, 5: 0.15, 6: 0.2, 7: 0.3, 8: 0.5, 9: 1.0,
                    10: 2.0, 11: 2.5, 12: 3.0, 13: 3.5, 14: 3.5, 15: 3.2,
                    16: 3.0, 17: 2.5, 18: 2.0, 19: 1.0, 20: 0.2, 21: 0.1,
                    }

    def pv_value_and_ts(self):
        """
        Calculates the PV value and timestamp based on the current time.

        Returns:
            tuple: A tuple containing the PV value and the corresponding timestamp.

        """
        current_time = datetime.now()
        ts = datetime.timestamp(current_time)
        pv_base = self.hour_vs_pv_value.get(current_time.hour, 0)
        if pv_base > 0:
            if pv_base > 14:
                return round(pv_base + (datetime.now().minute * 0.01), 4), ts
            else:
                return round(pv_base - (datetime.now().minute * 0.01), 4), ts
        return pv_base, ts