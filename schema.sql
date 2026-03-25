PRAGMA foreign_keys = ON;

-- =========================
-- TABLE: clubs
-- =========================
CREATE TABLE IF NOT EXISTS clubs (
  id        INTEGER PRIMARY KEY AUTOINCREMENT,
  name      TEXT NOT NULL UNIQUE,
  city      TEXT
);

-- =========================
-- TABLE: players
-- =========================
CREATE TABLE IF NOT EXISTS players (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  full_name     TEXT NOT NULL,
  birth_date    TEXT,
  nationality   TEXT,
  position      TEXT NOT NULL CHECK (position IN ('GK','DF','MF','FW')),
  shirt_number  INTEGER CHECK (shirt_number BETWEEN 1 AND 99),
  club_id       INTEGER,
  status        TEXT NOT NULL DEFAULT 'ACTIVE'
                CHECK (status IN ('ACTIVE','INJURED','SUSPENDED','RETIRED','FREE_AGENT')),

  CONSTRAINT fk_players_club
    FOREIGN KEY (club_id) REFERENCES clubs(id)
    ON UPDATE CASCADE
    ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_players_club_id ON players(club_id);

-- =========================
-- TABLE: transfers
-- =========================
CREATE TABLE IF NOT EXISTS transfers (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  player_id     INTEGER NOT NULL,
  from_club_id  INTEGER,
  to_club_id    INTEGER NOT NULL,
  transfer_date TEXT NOT NULL,
  fee           INTEGER CHECK (fee >= 0),

  CONSTRAINT fk_transfers_player
    FOREIGN KEY (player_id) REFERENCES players(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,

  CONSTRAINT fk_transfers_from_club
    FOREIGN KEY (from_club_id) REFERENCES clubs(id)
    ON UPDATE CASCADE
    ON DELETE SET NULL,

  CONSTRAINT fk_transfers_to_club
    FOREIGN KEY (to_club_id) REFERENCES clubs(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,

  CONSTRAINT chk_transfer_diff CHECK (to_club_id != from_club_id)
);

CREATE INDEX IF NOT EXISTS idx_transfers_player_id ON transfers(player_id);

-- =========================
-- TABLE: leagues
-- =========================
CREATE TABLE IF NOT EXISTS leagues (
  id      INTEGER PRIMARY KEY AUTOINCREMENT,
  name    TEXT NOT NULL,
  season  TEXT NOT NULL,
  UNIQUE (name, season)
);

-- =========================
-- TABLE: league_teams
-- =========================
CREATE TABLE IF NOT EXISTS league_teams (
  league_id INTEGER NOT NULL,
  club_id   INTEGER NOT NULL,
  PRIMARY KEY (league_id, club_id),

  CONSTRAINT fk_league_teams_league
    FOREIGN KEY (league_id) REFERENCES leagues(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,

  CONSTRAINT fk_league_teams_club
    FOREIGN KEY (club_id) REFERENCES clubs(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE
);

-- =========================
-- TABLE: matches
-- =========================
CREATE TABLE IF NOT EXISTS matches (
  id            INTEGER PRIMARY KEY AUTOINCREMENT,
  league_id     INTEGER NOT NULL,
  round_no      INTEGER NOT NULL CHECK (round_no >= 1),
  match_date    TEXT NOT NULL,
  home_club_id  INTEGER NOT NULL,
  away_club_id  INTEGER NOT NULL,
  home_goals    INTEGER NOT NULL DEFAULT 0 CHECK (home_goals >= 0),
  away_goals    INTEGER NOT NULL DEFAULT 0 CHECK (away_goals >= 0),
  status        TEXT NOT NULL DEFAULT 'SCHEDULED'
                CHECK (status IN ('SCHEDULED','FINISHED')),

  CONSTRAINT fk_matches_league
    FOREIGN KEY (league_id) REFERENCES leagues(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,

  CONSTRAINT fk_matches_home_club
    FOREIGN KEY (home_club_id) REFERENCES clubs(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,

  CONSTRAINT fk_matches_away_club
    FOREIGN KEY (away_club_id) REFERENCES clubs(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,

  CONSTRAINT chk_home_away_diff CHECK (home_club_id <> away_club_id),

  UNIQUE (league_id, round_no, home_club_id, away_club_id, match_date)
);

CREATE INDEX IF NOT EXISTS idx_matches_league_round ON matches(league_id, round_no);
CREATE INDEX IF NOT EXISTS idx_matches_home ON matches(home_club_id);
CREATE INDEX IF NOT EXISTS idx_matches_away ON matches(away_club_id);

-- =========================
-- TABLE: goals
-- =========================
CREATE TABLE IF NOT EXISTS goals (
  id        INTEGER PRIMARY KEY AUTOINCREMENT,
  match_id  INTEGER NOT NULL,
  player_id INTEGER NOT NULL,
  club_id   INTEGER NOT NULL,
  minute    INTEGER NOT NULL CHECK (minute BETWEEN 1 AND 130),

  CONSTRAINT fk_goals_match
    FOREIGN KEY (match_id) REFERENCES matches(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,

  CONSTRAINT fk_goals_player
    FOREIGN KEY (player_id) REFERENCES players(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,

  CONSTRAINT fk_goals_club
    FOREIGN KEY (club_id) REFERENCES clubs(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_goals_match_id ON goals(match_id);
CREATE INDEX IF NOT EXISTS idx_goals_player_id ON goals(player_id);

-- =========================
-- TABLE: cards
-- =========================
CREATE TABLE IF NOT EXISTS cards (
  id        INTEGER PRIMARY KEY AUTOINCREMENT,
  match_id  INTEGER NOT NULL,
  player_id INTEGER NOT NULL,
  club_id   INTEGER NOT NULL,
  minute    INTEGER NOT NULL CHECK (minute BETWEEN 1 AND 130),
  card_type TEXT NOT NULL CHECK (card_type IN ('Y','R')),

  CONSTRAINT fk_cards_match
    FOREIGN KEY (match_id) REFERENCES matches(id)
    ON UPDATE CASCADE
    ON DELETE CASCADE,

  CONSTRAINT fk_cards_player
    FOREIGN KEY (player_id) REFERENCES players(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT,

  CONSTRAINT fk_cards_club
    FOREIGN KEY (club_id) REFERENCES clubs(id)
    ON UPDATE CASCADE
    ON DELETE RESTRICT
);

CREATE INDEX IF NOT EXISTS idx_cards_match_id ON cards(match_id);
CREATE INDEX IF NOT EXISTS idx_cards_player_id ON cards(player_id);