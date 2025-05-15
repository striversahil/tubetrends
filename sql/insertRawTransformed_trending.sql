INSERT INTO trending (id, timestamp , trending_data) VALUES (
    gen_random_uuid(),
    now(),
    %s
)
RETURNING id;