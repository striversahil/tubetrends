INSERT INTO video (videoId, title, trending_id, publishedAt, channelId, channelName, thumbnail, tags, duration, viewCount, likeCount, commentCount) VALUES (
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s,
    %s
)
RETURNING videoId;