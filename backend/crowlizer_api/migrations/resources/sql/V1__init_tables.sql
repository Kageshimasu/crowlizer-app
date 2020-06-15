CREATE TABLE category (
    id SERIAL NOT NULL,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by CHAR(36) NOT NULL DEFAULT 'system',
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by CHAR(36) NOT NULL DEFAULT 'system',
    version bigint NOT NULL DEFAULT 0,
    PRIMARY KEY (id)
);

INSERT INTO category (name) VALUES
('アート'),
('音楽'),
('開発'),
('フード'),
('ファッション'),
('書籍'),
('アニメ・漫画'),
('スポーツ'),
('映像'),
('テクノロジー'),
('ビジネス'),
('地域活性化');
