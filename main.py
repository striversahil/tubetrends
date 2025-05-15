from data.index import getTrending
from pipelines.mongo_raw_pipeline import StoreTrending
from pipelines.storing_rawTransformed import StoreRawTransformed
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":

    data = getTrending("IN")
    if data is not None:
        #                      +++++++++++++++++++++++++++++ Pipeline Started ++++++++++++++++++++++++++++
        # Storing Raw Data in Mongo DB in fixed interval
        res = StoreTrending(data)
        if res:
            StoreRawTransformed(data=data)
