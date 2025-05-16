CREATE TABLE IF NOT EXISTS video (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  videoId VARCHAR,
  title VARCHAR,
  trending_id VARCHAR, 
  publishedAt TIMESTAMP,
  -- channelId UUID REFERENCES channel(id), -- Uncomment when channel table is ready
  channelId VARCHAR,
  channelName VARCHAR,
  thumbnail VARCHAR,
  tags JSONB DEFAULT '[]', 
  duration VARCHAR,
  viewCount VARCHAR,
  likeCount VARCHAR,
  commentCount VARCHAR,
  timestamp TIMESTAMP DEFAULT now()
);
