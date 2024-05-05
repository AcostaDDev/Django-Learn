from threading import Thread
from typing import List, Optional

import requests
from requests import RequestException
from concurrent.futures import ThreadPoolExecutor

from pokeapi.pokeapi_service.pokeapi_rest_service import PokeAPIRestService
from pokeapi.pokemon import Pokemon


class PokeAPIThreadedRestService(PokeAPIRestService):

    def get_by_names(self, names: List[str]) -> List[Pokemon]:
        pokemons = []

        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = [executor.submit(self._get_by_name, name) for name in names]
            for future in futures:
                pokemons.append(future.result())

        return pokemons

    def _get_by_name(self, name: str) -> Optional[Pokemon]:
        try:
            response = requests.get(self.BASE_API_URL + name)
            response.raise_for_status()
            pokemon_json = response.json()
        except RequestException:
            return None

        return Pokemon(id=pokemon_json['id'], name=pokemon_json['name'], height=pokemon_json['height'],
                       weight=pokemon_json['weight'])
