import asyncio
import random
import time


class BatchFetcher:
    # The `database` has an `async_fetch` method
    # that you should use in your code. This method
    # takes in a record id and returns a record.
    def __init__(self, database):
        self.database = database

    async def fetch_records(self, record_ids):
        records = await asyncio.gather(
            *[self.database.async_fetch(record_id) for record_id in record_ids]
        )
        return records


class MockDatabase(object):
    def __init__(self, records):
        self.records = records

    async def async_fetch(self, record_id):
        # A real database would take time to contact and fetch records from,
        # so we simulate that time by sleeping in here.
        await asyncio.sleep(0.1)
        return self.records.get(record_id)


async def main():
    keys = [f"{i}" for i in range(20)]
    records = {k: {"data": random.randint(1, 100)} for k in keys}
    db = MockDatabase(records)
    fetcher = BatchFetcher(db)

    start = time.time()
    results = await fetcher.fetch_records(keys)
    end = time.time()
    print('Time taken:', end - start)
    print(results)

asyncio.run(main())
