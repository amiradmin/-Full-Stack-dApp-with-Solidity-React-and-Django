from django.db import models

class Transaction(models.Model):
    """
    Represents a blockchain transaction stored in the database.

    Attributes:
        tx_hash (str): Unique transaction hash.
        sender (str): Address of the sender.
        value (float): Amount of Ether transferred.
        timestamp (datetime): Time when the transaction was recorded.
    """
    tx_hash: str = models.CharField(max_length=66, unique=True)
    sender: str = models.CharField(max_length=42)
    value: float = models.FloatField()
    timestamp: models.DateTimeField = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """
        Returns a string representation of the transaction.
        """
        return f"Transaction {self.tx_hash} from {self.sender}"
