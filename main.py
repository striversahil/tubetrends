from pipelines.o1storing_rawVideo import StoreRawVideo
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":

    #                      +++++++++++++++++++++++++++++ Pipeline Started ++++++++++++++++++++++++++++
    # Storing Raw Data in Mongo DB in fixed interval
    StoreRawVideo()
