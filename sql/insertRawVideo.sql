INSERT INTO video (region , rankScore, videoId, title, trending_id, publishedAt,category, channelId, channelName, thumbnail, tags, duration, viewCount, likeCount, commentCount) VALUES (
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
    %s,
    %s,
    %s,
    %s
)
RETURNING videoId;