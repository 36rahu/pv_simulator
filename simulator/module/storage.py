from datetime import datetime
import csv


class Storage:
    """
    Storage class for writing data to a CSV file.

    Methods:
        write_file(data): Writes the given data to the CSV file.

    """

    def write_file(self, data):
        """
        Writes the given data to the CSV file.

        Args:
            data (list): The data to be written to the CSV file.

        """
        with open('output.csv', 'a') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(data)
