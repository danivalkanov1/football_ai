PRAGMA foreign_keys = ON;

-- Clubs
INSERT INTO clubs(name, city) VALUES
('Левски София','София'),
('Лудогорец','Разград'),
('Ботев Пловдив','Пловдив'),
('ЦСКА София','София');

-- League
INSERT INTO leagues(name, season) VALUES
('Първа лига','2025/2026');

-- League teams
INSERT INTO league_teams(league_id, club_id)
SELECT l.id, c.id
FROM leagues l, clubs c
WHERE l.name='Първа лига' AND l.season='2025/2026'
  AND c.name IN ('Левски София','Лудогорец','Ботев Пловдив','ЦСКА София');

-- Players (минимум по 2-3)
INSERT INTO players(full_name, birth_date, nationality, position, shirt_number, club_id, status)
SELECT 'Иван Петров','2004-02-12','BG','FW',9,c.id,'ACTIVE' FROM clubs c WHERE c.name='Левски София';
INSERT INTO players(full_name, birth_date, nationality, position, shirt_number, club_id, status)
SELECT 'Георги Димитров','2003-07-01','BG','MF',8,c.id,'ACTIVE' FROM clubs c WHERE c.name='Левски София';

INSERT INTO players(full_name, birth_date, nationality, position, shirt_number, club_id, status)
SELECT 'Марселиньо Силва','1999-03-10','BR','MF',10,c.id,'ACTIVE' FROM clubs c WHERE c.name='Лудогорец';
INSERT INTO players(full_name, birth_date, nationality, position, shirt_number, club_id, status)
SELECT 'Никола Стоянов','2002-11-21','BG','DF',4,c.id,'ACTIVE' FROM clubs c WHERE c.name='Лудогорец';

INSERT INTO players(full_name, birth_date, nationality, position, shirt_number, club_id, status)
SELECT 'Петър Иванов','2001-05-05','BG','FW',11,c.id,'ACTIVE' FROM clubs c WHERE c.name='Ботев Пловдив';

INSERT INTO players(full_name, birth_date, nationality, position, shirt_number, club_id, status)
SELECT 'Александър Колев','2000-09-09','BG','FW',7,c.id,'ACTIVE' FROM clubs c WHERE c.name='ЦСКА София';

-- Matches (няколко завършени за форма/AI)
INSERT INTO matches(league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status)
SELECT l.id, 1, '2025-07-20', h.id, a.id, 2, 1, 'FINISHED'
FROM leagues l, clubs h, clubs a
WHERE l.name='Първа лига' AND l.season='2025/2026'
  AND h.name='Левски София' AND a.name='Ботев Пловдив';

INSERT INTO matches(league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status)
SELECT l.id, 1, '2025-07-21', h.id, a.id, 1, 1, 'FINISHED'
FROM leagues l, clubs h, clubs a
WHERE l.name='Първа лига' AND l.season='2025/2026'
  AND h.name='ЦСКА София' AND a.name='Лудогорец';

INSERT INTO matches(league_id, round_no, match_date, home_club_id, away_goals, home_goals, away_club_id, status)
SELECT 1,2,'2025-07-28', h.id, 0, 3, a.id, 'FINISHED'
FROM clubs h, clubs a
WHERE h.name='Лудогорец' AND a.name='Ботев Пловдив';

-- Goals (примерни)
INSERT INTO goals(match_id, player_id, club_id, minute)
SELECT m.id, p.id, c.id, 23
FROM matches m, players p, clubs c
WHERE m.match_date='2025-07-20' AND p.full_name='Иван Петров' AND c.name='Левски София';

INSERT INTO goals(match_id, player_id, club_id, minute)
SELECT m.id, p.id, c.id, 77
FROM matches m, players p, clubs c
WHERE m.match_date='2025-07-21' AND p.full_name='Марселиньо Силва' AND c.name='Лудогорец';

-- Cards (примерни)
INSERT INTO cards(match_id, player_id, club_id, minute, card_type)
SELECT m.id, p.id, c.id, 55, 'Y'
FROM matches m, players p, clubs c
WHERE m.match_date='2025-07-20' AND p.full_name='Георги Димитров' AND c.name='Левски София';

-- PLAYERS (sample)
INSERT INTO players(full_name, birth_date, nationality, position, shirt_number, club_id, status)
SELECT 'Иван Петров','2004-02-12','BG','FW',9,c.id,'ACTIVE' FROM clubs c WHERE c.name='Левски София';

INSERT INTO players(full_name, birth_date, nationality, position, shirt_number, club_id, status)
SELECT 'Георги Димитров','2003-07-01','BG','MF',8,c.id,'ACTIVE' FROM clubs c WHERE c.name='Левски София';

INSERT INTO players(full_name, birth_date, nationality, position, shirt_number, club_id, status)
SELECT 'Марселиньо Силва','1999-03-10','BR','MF',10,c.id,'ACTIVE' FROM clubs c WHERE c.name='Лудогорец';

INSERT INTO players(full_name, birth_date, nationality, position, shirt_number, club_id, status)
SELECT 'Никола Стоянов','2002-11-21','BG','DF',4,c.id,'ACTIVE' FROM clubs c WHERE c.name='Лудогорец';

INSERT INTO matches (league_id, round_no, match_date, home_club_id, away_club_id)
VALUES
(1, 1, '2026-03-20', 1, 2),
(1, 1, '2026-03-20', 3, 4),
(1, 1, '2026-03-20', 5, 6);