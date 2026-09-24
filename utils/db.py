# A fake db class

class FakeDB:
    def __init__(self):
        self.admins = {}

    def add_admin(self, admin_data):
        self.admins[admin_data.email] = admin_data

    def get_admin(self, email):
        return self.admins.get(email)

    def remove_admin(self, email):
        if email in self.admins:
            del self.admins[email]
        else:
            raise ValueError("Admin not found.")


db = FakeDB()


def get_db():
    return db