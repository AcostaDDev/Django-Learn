from accounts.domain.repositories.account_repository import AccountRepository
from accounts.domain.account import Account
from accounts.infrastructure.models.account import AccountDjango


class AccountRepositoryDjango(AccountRepository):

    def get_by_id(self, id: int) -> Account:
        return AccountDjango.objects.get(id=id).to_domain()
    
    def save(self, account: Account):
        return AccountDjango(owner=account.owner, amount=account.amount).save()