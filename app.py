import csv
import re


class PyCsv:

    # Constructor
    def __init__(self, file_name):
        self.connection = re.sub('[.csv]', '', file_name) + ".csv"

    # Get values from CSV
    def get_values(self):
        try:
            with open(self.connection, "r") as f:
                if f.readable():
                    return list(csv.reader(f))[0]
                else:
                    return None
        except Exception as err:
            print(err)
        finally:
            f.close()

    # Append a value to CSV file
    def append_value(self, val):
        try:
            with open(self.connection, "a") as f:
                f.write(self.__prepend_comma(self.__remove_commas(val)))
        except Exception as err:
            print(err)
        finally:
            f.close()
            return self.get_values()

    # Bulk add values to CSV file
    def bulk_add(self, values):
        try:
            temp = ""
            for v in values:
                temp = temp + self.__prepend_comma(v)
            with open(self.connection, "a") as f:
                f.write(temp)
        except Exception as err:
            print(err)
        finally:
            f.close()
            return self.get_values()

    # Delete contents of CSV file
    def delete_values(self):
        try:
            with open(self.connection, "w") as f:
                f.write("")
        except Exception as err:
            print(err)
        finally:
            f.close()
            return []

    # Add comma to start of string
    @staticmethod
    def __prepend_comma(val):
        return "," + val

    # Remove user inputted commas
    @staticmethod
    def __remove_commas(val):
        return re.sub('[,]', '', val)

