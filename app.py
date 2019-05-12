import csv
import re


class PyCsv:

    # This list is updated after each change and can be used for quick access to CSV values
    cached_values = []

    # Constructor
    def __init__(self, file_name):
        self.connection = re.sub('[.csv]', '', file_name) + ".csv"
        self.get_values()

    # Get values from CSV
    def get_values(self):
        try:
            with open(self.connection, "r") as f:
                if f.readable():
                    self.cached_values = list(csv.reader(f))[0]
                else:
                    self.cached_values = None
        except Exception as err:
            print(err)
        finally:
            f.close()
            return self.cached_values

    # Append a value to CSV file
    def append_value(self, val):
        try:
            with open(self.connection, "a") as f:
                if self.cached_values is None:
                    f.write(self.__remove_commas(val))
                else:
                    f.write(self.__prepend_comma(self.__remove_commas(val)))
        except Exception as err:
            print(err)
        finally:
            f.close()
            self.cached_values = self.get_values()
            return self.cached_values

    # Bulk add values to CSV file
    def bulk_add(self, values):
        try:
            temp = ""
            for index, v in enumerate(values):
                if index is 0 and self.cached_values is None:
                    temp = temp + v
                else:
                    temp = temp + self.__prepend_comma(v)
            with open(self.connection, "a") as f:
                f.write(temp)
        except Exception as err:
            print(err)
        finally:
            f.close()
            self.cached_values = self.get_values()
            return self.cached_values

    # Removes a value from the CSV file by index
    def remove_value(self, index):
        try:
            temp = self.cached_values
            del temp[index]
            self.delete_values()
            self.cached_values = self.bulk_add(temp)
        except Exception as err:
            print(err)
        finally:
            return self.cached_values

    # Delete contents of CSV file
    def delete_values(self):
        try:
            with open(self.connection, "w") as f:
                if self.cached_values is not None:
                    f.write("")
        except Exception as err:
            print(err)
        finally:
            f.close()
            self.cached_values = None
            return self.cached_values

    # Rewrites the contents of CSV file into one line
    def rewrite_file(self):
        temp = []
        try:
            with open(self.connection, "r") as f:
                if f.readable():
                    self.cached_values = list(csv.reader(f))
            for row in self.cached_values:
                for val in row:
                    if val is not '':
                        temp.append(val)
            self.delete_values()
            self.bulk_add(temp)
        except Exception as err:
            print(err)
        finally:
            f.close()
            return self.cached_values

    # Add comma to start of string
    @staticmethod
    def __prepend_comma(val):
        return "," + val

    # Remove user inputted commas
    @staticmethod
    def __remove_commas(val):
        return re.sub('[,]', '', val)
