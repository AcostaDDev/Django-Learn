import abc

from accounts.domain.account import Account


class AccountRepository(abc.ABC):

    @abc.abstractmethod
    def get_by_id(self, id: int) -> Account:
        pass

    @abc.abstractmethod
    def save(self, account: Account):
        pass
