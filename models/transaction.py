class Transaction:
    def __init__(self, id, user_id, date, category, type_, amount, description):
        self.id = id
        self.user_id = user_id
        self.date = date
        self.category = category
        self.type = type_
        self.amount = amount
        self.description = description

    def to_dict(self):
        """Convert transaction object to dictionary format for DataFrame."""
        return {
            "ID": self.id,
            "User ID": self.user_id,
            "Date": self.date,
            "Category": self.category,
            "Type": self.type,
            "Amount": self.amount,
            "Description": self.description
        }
