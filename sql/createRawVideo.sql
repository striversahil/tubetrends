CREATE TABLE IF NOT EXISTS video (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  ranking INTEGER,
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
  region VARCHAR,
  duration INTEGER,
  viewCount BIGINT,
  likeCount BIGINT,
  commentCount BIGINT,
  timestamp TIMESTAMP DEFAULT now()
);
