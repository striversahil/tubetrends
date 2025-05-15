CREATE TABLE IF NOT EXISTS trending (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(), 
      trending_data JSONB,
      timestamp TIMESTAMP DEFAULT now()
);