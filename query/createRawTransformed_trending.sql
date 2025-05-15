CREATE TABLE IF NOT EXIST trending (
      id UUID PRIMARY KEY DEFAULT gen_random_uuid(), 
      timestamp timestamp,
);