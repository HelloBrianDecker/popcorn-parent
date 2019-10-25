class Flags:
    def __init__(self):
        self.delete_column = False
        self.delete_rows = False

    def get_delete_column(self):
        return self.delete_column

    def set_delete_column(self, boolean):
        self.delete_column = boolean

    def get_delete_rows(self):
        return self.delete_rows

    def set_delete_rows(self, boolean):
        self.delete_rows = boolean


