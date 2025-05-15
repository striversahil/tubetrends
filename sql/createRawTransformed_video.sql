CREATE TABLE IF NOT EXISTS video (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  videoId VARCHAR,
  title VARCHAR,
  trending_id UUID REFERENCES trending(id), 
  publishedAt TIMESTAMP,
  -- channelId UUID REFERENCES channel(id), -- Uncomment when channel table is ready
  channelId VARCHAR,
  channelName VARCHAR,
  thumbnail VARCHAR,
  tags JSONB DEFAULT '[]', -- Nice use of JSONB for flexible tags!
  duration VARCHAR,
  viewCount VARCHAR,
  likeCount VARCHAR,
  commentCount VARCHAR,
  timestamp TIMESTAMP DEFAULT now()
);
