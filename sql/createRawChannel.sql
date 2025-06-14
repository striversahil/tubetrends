CREATE TABLE IF NOT EXISTS channel (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
      channelId VARCHAR,
      title VARCHAR,
      description TEXT,
      createdAt VARCHAR,
      profilePic VARCHAR,
      country VARCHAR,
      viewCount BIGINT,
      subscriberCount BIGINT,
      videoCount BIGINT,
      isKids BOOLEAN,
      timestamp TIMESTAMP DEFAULT now()
);