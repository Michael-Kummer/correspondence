
CREATE TABLE files (
    id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    subreddit varchar(30) NULL,
    created_at timestamp with time zone NOT NULL,
);

CREATE TABLE image(
    id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    parent_file int NOT NULL REFERENCES files(id) ON DELETE CASCADE,
    p1_ELO int NULL,
    p2_ELO int NULL,
    data jsonb NOT NULL
);

CREATE INDEX idx_image_parent_file ON image(parent_file);
