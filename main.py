from pipelines.o2storing_rawVideo import storeRawVideo
from pipelines.o3storing_rawChannel import storeRawChannel
from pipelines.o1cleanup_tables import cleanup_tables
from dotenv import load_dotenv

regions = ["IN", "US", "GB", "CA", "AU", "DE", "FR", "JP", "KR", "BR"]


if __name__ == "__main__":

    load_dotenv()

    #                      +++++++++++++++++++++++++++++ Pipeline Started ++++++++++++++++++++++++++++

    status_cleanup = cleanup_tables()
    if not status_cleanup:
        print("❌ Error in cleanup tables Pipeline")
        exit(1)
    else:
        print("✅ Cleanup Tables Pipeline Completed")
    # Storing Raw Data in Mongo DB in fixed interval

    for region in regions:
        print(f"Starting Raw Video Pipeline for region: {region}")
        channels = storeRawVideo(region)
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

    #                      +++++++++++++++++++++++++++++ Pipeline Completed ++++++++++++++++++++++++++++
