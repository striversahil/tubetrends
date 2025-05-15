CREATE TABLE IF NOT EXIST trending (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(), 
      trending_data JSONB,
      timestamp timestamp,
);