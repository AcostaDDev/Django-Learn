from django.urls import path

from accounts.infrastructure.endpoints.accounts import AccountAPI
from accounts.application.retrieve_account_use_case import RetrieveAccountUseCase
from accounts.infrastructure.repositories.account_repository_django import AccountRepositoryDjango

account_api = AccountAPI(RetrieveAccountUseCase(AccountRepositoryDjango()))

routes = [
    path('<int:id>', account_api.retrieve),
    # path('<int:account_id>/deposit', account_api.deposit),

]