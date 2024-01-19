-- create index on names table for the first letter of the name

CREATE INDEX idx_name_first_score ON names (name(1), score);