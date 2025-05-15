INSERT INTO trending (id, timestamp , trending_data) VALUES (
    gen_random_uuid(),
    now(),
    $1
)