CREATE TABLE IF NOT EXIST video (
      id UUID PRIMARY KEY,
      title VARCHAR,
      trending_id UUID references trending(id), 
      publishedAt timestamp,
      -- channelId UUID references channel(id),
      channelId VARCHAR,
      channelName VARCHAR,
      thumbnail VARCHAR,
      tags JSONB DEFAULT '[]',
      duration VARCHAR,
      viewCount VARCHAR,
      likeCount VARCHAR,
      commentCount VARCHAR,
      timestamp timestamp default now()
)