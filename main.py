from pipelines.o2mongo_raw_pipeline import StoreTrending
from pipelines.o1storing_rawVideo import StoreRawVideo
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":

    if data is not None:
        #                      +++++++++++++++++++++++++++++ Pipeline Started ++++++++++++++++++++++++++++
        # Storing Raw Data in Mongo DB in fixed interval
        res = StoreTrending(data)
        if res:
            StoreRawVideo(res, data=data)
