import asyncio


class BatchFetcher:
    # The `database` has an `async_fetch` method
    # that you should use in your code. This method
    # takes in a record id and returns a record.
    def __init__(self, database):
        self.database = database

    async def async_fetch(self, record_id):
        # A real database would take time to contact and fetch records from,
        # so we simulate that time by sleeping in here.
        await asyncio.sleep(0.1)
        return self.database.get(record_id)

    async def fetch_records(self, record_ids):
        records = []
        for record_id in record_ids:
            record = await self.async_fetch(record_id)
            records.append(record)


class MockDatabase(object):
    def __init__(self, records):
        self.records = records

    async def async_fetch(self, record_id):
        # A real database would take time to contact and fetch records from,
        # so we simulate that time by sleeping in here.
        await asyncio.sleep(0.1)
        return self.records.get(record_id)


async def main():
    records = {
        "a": {"data": 42},
    }
    db = MockDatabase(records)
    fetcher = BatchFetcher(db)
    results = await fetcher.fetch_records(["a"])
    print(results)

asyncio.run(main())
