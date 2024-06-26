import time
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor
from typing import Dict, List, Tuple

from process_csv.data_income import DataIncome
from process_csv.income import Income
from process_csv.services.income_processor_service import IncomeProcessorService


class IncomeProcessorConcurrentService:

    def average_per_region(self, incomes: List[Income]) -> Dict[str, DataIncome]:
        region_incomes = defaultdict(list)
        for income in incomes:
            region_incomes[income.region].append(income.amount)

        with ProcessPoolExecutor() as executor:
            futures = [executor.submit(self._calculate_average, region=region, amounts=amounts) for region, amounts in region_incomes.items()]
            region_amount = {}
            for future in futures:
                result = future.result()
                region_amount[result[0]] = result[1]

        return region_amount

    def _calculate_average(self, region: str, amounts: List[float]) -> Tuple[str, DataIncome]:
        time.sleep(0.8)
        return region, DataIncome(
            average=sum(amounts) / len(amounts),
            min=min(amounts),
            max=max(amounts)
        )
