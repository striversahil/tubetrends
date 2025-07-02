from connection.postgres import cur
from connection.mongoDb import Db
from datetime import datetime, timedelta
import traceback


def postgresCleanup():
    """
    Function to clean up old rows in the Video and Channel tables
    that are older than 30 days.
    """
    try:
        print("Starting cleanup of old rows in Video and Channel tables...")
        # Clean up Video table
        cur.execute(
            """
            DELETE FROM video
            WHERE timestamp < NOW() - INTERVAL '30 days'
            """
        )
        print("Cleaned up old rows from Video table.")

        # Clean up Channel table
        cur.execute(
            """
            DELETE FROM channel
            WHERE timestamp < NOW() - INTERVAL '30 days'
            """
        )
        print("Cleaned up old rows from Channel table.")

    except Exception as e:
        print("Error during cleanup of tables: \n", e)


def cleanup_tables():
    """
    Cleans up rows in Video and Channlel tables that are older than 30 days.
    """

    try:
        postgresCleanup()
        mongoCleanup()
        print("Cleanup of old rows in Video and Channel tables completed successfully.")
        return True

    except Exception as e:
        print("Error during cleanup of tables: \n", e)
        traceback.print_exc()
        return False


def mongoCleanup():
    """
    Function to clean up old rows in the MongoDB collections
    that are older than 30 days.
    """
    try:
        print("Starting cleanup of old rows in MongoDB collections...")
        # Clean up RawVideo collection by less than 30 days old

        Db.rawVideo.delete_many(
            {"createdAt": {"$lt": datetime.now() - timedelta(days=30)}}
        )
        print("Cleaned up old rows from RawVideo collection.")

        # Clean up RawChannel collection
        Db.rawChannel.delete_many(
            {"createdAt": {"$lt": datetime.now() - timedelta(days=30)}}
        )
        print("Cleaned up old rows from RawChannel collection.")

    except Exception as e:
        print("Error during cleanup of MongoDB collections: \n", e)
