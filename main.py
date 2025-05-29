from pipelines.o1storing_rawVideo import storeRawVideo
from pipelines.o2storing_rawChannel import storeRawChannel
from pipelines.o3cleanup_tables import cleanup_tables
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
        stored_channels = storeRawChannel(channels)
        if not stored_channels:
            print("❌ Error in storing raw channel Pipeline")
            exit(1)
        else:
            print("✅ Raw Channel Pipeline Completed")
            status_cleanup = cleanup_tables()
            if not status_cleanup:
                print("❌ Error in cleanup tables Pipeline")
                exit(1)
            else:
                print("✅ Cleanup Tables Pipeline Completed")

