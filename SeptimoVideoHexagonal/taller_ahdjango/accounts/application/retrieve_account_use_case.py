

from accounts.application.retrieve_account_dto import RetrieveAccountDTO
from accounts.domain.account import Account
from accounts.domain.repositories.account_repository import AccountRepository


class RetrieveAccountUseCase:

    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def execute(self, retrieve_account_dto: RetrieveAccountDTO) -> Account:
        account= self.account_repository.get_by_id(retrieve_account_dto.id)
        return account
