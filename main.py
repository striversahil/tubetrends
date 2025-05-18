from pipelines.o1storing_rawVideo import storeRawVideo
from pipelines.o2storing_rawChannel import storeRawChannel
from dotenv import load_dotenv


if __name__ == "__main__":

    load_dotenv()

    #                      +++++++++++++++++++++++++++++ Pipeline Started ++++++++++++++++++++++++++++
    # Storing Raw Data in Mongo DB in fixed interval
    channels = storeRawVideo()
    if not channels:
        print("❌ Error in storing raw video Pipeline")
        exit(1)
    else:
        print("✅ Raw Video Pipeline Completed")
        storeRawChannel(channels)
