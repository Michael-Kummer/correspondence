CREATE TABLE files (
    id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    s3_key varchar(255) NOT NULL,
    subreddit varchar(30) NULL,
    created_at timestamp with time zone NOT NULL
);

CREATE TABLE conversations (
    id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    p1_elo int NULL,
    p2_elo int NULL
);

CREATE TABLE conversation_files (
    conversation_id int NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
    file_id int NOT NULL REFERENCES files(id) ON DELETE CASCADE,
    file_order int NOT NULL,
    PRIMARY KEY (conversation_id, file_id)
);

CREATE TYPE move_rating AS ENUM (
    'brilliant', 'great', 'best', 'excellent',
    'good', 'book', 'inaccuracy', 'mistake',
    'blunder', 'miss'
);

CREATE TABLE messages (
    id int GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    conversation_id int NOT NULL REFERENCES conversations(id) ON DELETE CASCADE,
    player smallint NOT NULL CHECK (player IN (1, 2)),
    body text NOT NULL,
    position int NOT NULL,
    rating move_rating NULL
);

CREATE INDEX idx_messages_conversation ON messages(conversation_id);
