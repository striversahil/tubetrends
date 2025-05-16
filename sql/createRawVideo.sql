CREATE TABLE IF NOT EXISTS video (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  videoId VARCHAR,
  title VARCHAR,
  trending_id VARCHAR, 
  publishedAt TIMESTAMP,
  category VARCHAR,
  -- channelId UUID REFERENCES channel(id), -- Uncomment when channel table is ready
  channelId VARCHAR,
  channelName VARCHAR,
  thumbnail VARCHAR,
  tags JSONB DEFAULT '[]', 
  duration NUMBER,
  viewCount NUMBER,
  likeCount NUMBER,
  commentCount NUMBER,
  timestamp TIMESTAMP DEFAULT now()
);
