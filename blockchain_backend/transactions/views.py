from django.http import JsonResponse
from django.views import View
from .models import Transaction
import json

class TransactionView(View):
    """
    Handles HTTP requests for blockchain transactions.
    """

    def get(self, request) -> JsonResponse:
        """
        Retrieves all transactions stored in the database.

        Args:
            request: Django HTTP request object.

        Returns:
            JsonResponse: A list of transactions in JSON format.
        """
        transactions = list(Transaction.objects.values())
        return JsonResponse({"transactions": transactions}, safe=False)

    def post(self, request) -> JsonResponse:
        """
        Stores a new transaction in the database.

        Args:
            request: Django HTTP request object containing transaction data.

        Returns:
            JsonResponse: Success message or error response.
        """
        try:
            data = json.loads(request.body)
            transaction = Transaction.objects.create(
                tx_hash=data["tx_hash"],
                sender=data["sender"],
                value=data["value"]
            )
            return JsonResponse({"message": "Transaction saved!", "tx_id": transaction.id})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
