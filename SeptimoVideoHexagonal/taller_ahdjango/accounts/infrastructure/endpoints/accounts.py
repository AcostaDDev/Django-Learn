from typing import Any, Dict

from django.core.handlers.wsgi import WSGIRequest
from pydantic import ValidationError

from accounts.domain.account import Account
from accounts.infrastructure.serializers.account import AccountSerializer
from accounts.application.retrieve_account_use_case import RetrieveAccountUseCase
from accounts.application.retrieve_account_dto import RetrieveAccountDTO


class AccountAPI:
    
    def __init__(self, retrieve_account_use_case: RetrieveAccountUseCase, id: int):
        self.retrieve_account_use_case = retrieve_account_use_case

    def retrieve(self, request: WSGIRequest, account_id: int) -> Dict[str, Any]:
        
        
        retrieve_account = RetrieveAccountDTO(id=account_id)
        account = self.retrieve_account_use_case.execute(retrieve_account)

        return AccountSerializer(owner=account.owner, amount=account.amount).dict()

        