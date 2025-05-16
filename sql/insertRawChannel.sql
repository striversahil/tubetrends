INSERT INTO channel (channelId, title, description, createdAt, profilePic, country, viewCount, subscriberCount, videoCount, isKids) VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
)
RETURNING id;