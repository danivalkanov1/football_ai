PRAGMA foreign_keys = ON;

-- CLUBS

INSERT INTO clubs (name, city) VALUES
('Левски София', 'София'),
('ЦСКА София', 'София'),
('Лудогорец', 'Разград'),
('Ботев Пловдив', 'Пловдив'),
('Черно море', 'Варна'),
('Берое', 'Стара Загора'),
('Локомотив Пловдив', 'Пловдив'),
('Славия София', 'София'),
('Марек', 'Дупница'),
('Монтана', 'Монтана'),
('Струмска слава', 'Радомир'),
('Спортист Своге', 'Своге'),
('Дунав', 'Русе'),
('Етър', 'Велико Търново'),
('Фратрия', 'Бенковски'),
('Бдин', 'Видин');

-- LEAGUES

INSERT INTO leagues (id, name, season) VALUES (1, 'Първа лига', '2025/2026');
INSERT INTO leagues (id, name, season) VALUES (2, 'Втора лига', '2025/2026');
-- LEAGUE TEAMS

INSERT INTO league_teams (league_id, club_id) VALUES (1, 1);
INSERT INTO league_teams (league_id, club_id) VALUES (1, 2);
INSERT INTO league_teams (league_id, club_id) VALUES (1, 3);
INSERT INTO league_teams (league_id, club_id) VALUES (1, 4);
INSERT INTO league_teams (league_id, club_id) VALUES (1, 5);
INSERT INTO league_teams (league_id, club_id) VALUES (1, 6);
INSERT INTO league_teams (league_id, club_id) VALUES (1, 7);
INSERT INTO league_teams (league_id, club_id) VALUES (1, 8);
INSERT INTO league_teams (league_id, club_id) VALUES (2, 9);
INSERT INTO league_teams (league_id, club_id) VALUES (2, 10);
INSERT INTO league_teams (league_id, club_id) VALUES (2, 11);
INSERT INTO league_teams (league_id, club_id) VALUES (2, 12);
INSERT INTO league_teams (league_id, club_id) VALUES (2, 13);
INSERT INTO league_teams (league_id, club_id) VALUES (2, 14);
INSERT INTO league_teams (league_id, club_id) VALUES (2, 15);
INSERT INTO league_teams (league_id, club_id) VALUES (2, 16);
-- PLAYERS

-- Левски София
INSERT INTO players (full_name, position, shirt_number, nationality, club_id, status) VALUES
('Ognyan Vladimirov', 'GK', 1, 'Bulgaria', 1, 'ACTIVE'),
('Kristian Dimitrov', 'DF', 50, 'Bulgaria', 1, 'ACTIVE'),
('Oliver Kamdem', 'DF', 71, 'Cameroon', 1, 'ACTIVE'),
('Christian Makoun', 'DF', 4, 'Venezuela', 1, 'ACTIVE'),
('Stipe Vulikić', 'DF', 6, 'Croatia', 1, 'ACTIVE'),
('Asen Mitkov', 'MF', 10, 'Bulgaria', 1, 'ACTIVE'),
('Gašper Trdin', 'MF', 18, 'Slovenia', 1, 'ACTIVE'),
('Akram Bouras', 'MF', 47, 'Algeria', 1, 'ACTIVE'),
('Mazire Soula', 'MF', 22, 'France', 1, 'ACTIVE'),
('Reinaldo', 'FW', 7, 'Brazil', 1, 'ACTIVE'),
('Juan Perea', 'FW', 9, 'Colombia', 1, 'ACTIVE');

-- ЦСКА София
INSERT INTO players (full_name, position, shirt_number, nationality, club_id, status) VALUES
('Dimitar Evtimov', 'GK', 25, 'Bulgaria', 2, 'ACTIVE'),
('Adrián Lapeña', 'DF', 4, 'Spain', 2, 'ACTIVE'),
('Lumbardh Dellova', 'DF', 5, 'Kosovo', 2, 'ACTIVE'),
('Martin Stoychev', 'DF', 20, 'Bulgaria', 2, 'ACTIVE'),
('Facundo Rodríguez', 'DF', 32, 'Argentina', 2, 'ACTIVE'),
('Bruno Jordão', 'MF', 6, 'Portugal', 2, 'ACTIVE'),
('Max Ebong', 'MF', 10, 'Belarus', 2, 'ACTIVE'),
('Mohamed Brahimi', 'MF', 11, 'France', 2, 'ACTIVE'),
('Alejandro Piedrahita', 'MF', 77, 'Colombia', 2, 'ACTIVE'),
('Ioannis Pittas', 'FW', 28, 'Cyprus', 2, 'ACTIVE'),
('Léo Pereira', 'FW', 38, 'Brazil', 2, 'ACTIVE');

-- Лудогорец
INSERT INTO players (full_name, position, shirt_number, nationality, club_id, status) VALUES
('Sergio Padt', 'GK', 1, 'Netherlands', 3, 'ACTIVE'),
('Joel Andersson', 'DF', 2, 'Sweden', 3, 'ACTIVE'),
('Anton Nedyalkov', 'DF', 3, 'Bulgaria', 3, 'ACTIVE'),
('Son', 'DF', 17, 'Spain', 3, 'ACTIVE'),
('Idan Nachmias', 'DF', 55, 'Israel', 3, 'ACTIVE'),
('Ivaylo Chochev', 'MF', 18, 'Bulgaria', 3, 'ACTIVE'),
('Aguibou Camara', 'MF', 20, 'Guinea', 3, 'ACTIVE'),
('Deroy Duarte', 'MF', 23, 'Cape Verde', 3, 'ACTIVE'),
('Stanislav Ivanov', 'FW', 30, 'Bulgaria', 3, 'ACTIVE'),
('Kwadwo Duah', 'FW', 9, 'Switzerland', 3, 'ACTIVE'),
('Bernard Tekpetey', 'FW', 37, 'Ghana', 3, 'ACTIVE');

-- Ботев Пловдив
INSERT INTO players (full_name, position, shirt_number, nationality, club_id, status) VALUES
('Daniel Naumov', 'GK', 29, 'Bulgaria', 4, 'ACTIVE'),
('Enock Kwateng', 'DF', 22, 'France', 4, 'ACTIVE'),
('Timothy Awany', 'DF', 20, 'Uganda', 4, 'ACTIVE'),
('Nikola Soldo', 'DF', 4, 'Croatia', 4, 'ACTIVE'),
('Simeon Petrov', 'DF', 87, 'Bulgaria', 4, 'ACTIVE'),
('Todor Nedelev', 'MF', 8, 'Bulgaria', 4, 'ACTIVE'),
('Asen Chandarov', 'MF', 10, 'Bulgaria', 4, 'ACTIVE'),
('Lucas Araújo', 'MF', 77, 'Brazil', 4, 'ACTIVE'),
('Henrique Jocú', 'MF', 28, 'Portugal', 4, 'ACTIVE'),
('Pedro Martins', 'FW', 11, 'Brazil', 4, 'ACTIVE'),
('Samuel Kalu', 'FW', 90, 'Nigeria', 4, 'ACTIVE');

-- Черно море
INSERT INTO players (full_name, position, shirt_number, nationality, club_id, status) VALUES
('Antoan Manasiev', 'GK', 70, 'Bulgaria', 5, 'ACTIVE'),
('Zhivko Atanasov', 'DF', 3, 'Bulgaria', 5, 'ACTIVE'),
('Asen Donchev', 'DF', 8, 'Bulgaria', 5, 'ACTIVE'),
('Ertan Tombak', 'DF', 50, 'Bulgaria', 5, 'ACTIVE'),
('João Bandaró', 'DF', 26, 'Brazil', 5, 'ACTIVE'),
('David Teles', 'MF', 24, 'Portugal', 5, 'ACTIVE'),
('Berk Beyhan', 'MF', 29, 'Bulgaria', 5, 'ACTIVE'),
('Celso Sidney', 'MF', 77, 'Portugal', 5, 'ACTIVE'),
('Nikolay Zlatev', 'FW', 39, 'Bulgaria', 5, 'ACTIVE'),
('Jorge Padilla', 'FW', 9, 'Spain', 5, 'ACTIVE'),
('Georgi Lazarov', 'FW', 19, 'Bulgaria', 5, 'ACTIVE');

-- Берое
INSERT INTO players (full_name, position, shirt_number, nationality, club_id, status) VALUES
('Arthur Motta', 'GK', 1, 'Brazil', 6, 'ACTIVE'),
('Ivaylo Mitev', 'DF', 6, 'Bulgaria', 6, 'ACTIVE'),
('Viktorio Valkov', 'DF', 14, 'Bulgaria', 6, 'ACTIVE'),
('Tijan Sonha', 'DF', 23, 'Gambia', 6, 'ACTIVE'),
('João Milheirão', 'DF', 25, 'Portugal', 6, 'ACTIVE'),
('Wesley Dual', 'MF', 17, 'Spain', 6, 'ACTIVE'),
('Stilyan Rusenov', 'MF', 18, 'Bulgaria', 6, 'ACTIVE'),
('Simeon Veshev', 'MF', 8, 'Bulgaria', 6, 'ACTIVE'),
('Stanislav Yovkov', 'MF', 16, 'Bulgaria', 6, 'ACTIVE'),
('Ismael Ferrer', 'FW', 11, 'Spain', 6, 'ACTIVE'),
('Miroslav Georgiev', 'FW', 22, 'Bulgaria', 6, 'ACTIVE');

-- Локомотив Пловдив
INSERT INTO players (full_name, position, shirt_number, nationality, club_id, status) VALUES
('Bojan Milosavljević', 'GK', 1, 'Serbia', 7, 'ACTIVE'),
('Denis Kirashki', 'DF', 44, 'Bulgaria', 7, 'ACTIVE'),
('Todor Pavlov', 'DF', 5, 'Bulgaria', 7, 'ACTIVE'),
('Andrei Chindriș', 'DF', 4, 'Romania', 7, 'ACTIVE'),
('Martin Ruskov', 'DF', 23, 'Bulgaria', 7, 'ACTIVE'),
('Francisco Politino', 'MF', 10, 'Argentina', 7, 'ACTIVE'),
('Miha Trdan', 'MF', 3, 'Slovenia', 7, 'ACTIVE'),
('Martin Atanasov', 'MF', 33, 'Bulgaria', 7, 'ACTIVE'),
('Parvizdzhon Umarbayev', 'MF', 39, 'Tajikistan', 7, 'ACTIVE'),
('Dimitar Iliev', 'FW', 14, 'Bulgaria', 7, 'ACTIVE'),
('Julien Lamy', 'FW', 99, 'France', 7, 'ACTIVE');

-- Славия София
INSERT INTO players (full_name, position, shirt_number, nationality, club_id, status) VALUES
('Georgi Petkov', 'GK', 1, 'Bulgaria', 8, 'ACTIVE'),
('David Malembana', 'DF', 15, 'Mozambique', 8, 'ACTIVE'),
('Nikola Savić', 'DF', 4, 'Serbia', 8, 'ACTIVE'),
('Lazar Marin', 'DF', 24, 'Bulgaria', 8, 'ACTIVE'),
('Maksimilian Lazarov', 'DF', 22, 'Bulgaria', 8, 'ACTIVE'),
('Georgi Shopov', 'MF', 5, 'Bulgaria', 8, 'ACTIVE'),
('Valentin Yotov', 'MF', 8, 'Bulgaria', 8, 'ACTIVE'),
('Mouhamed Dosso', 'MF', 11, 'France', 8, 'ACTIVE'),
('Emil Stoev', 'MF', 77, 'Bulgaria', 8, 'ACTIVE'),
('Roberto Raychev', 'FW', 9, 'Bulgaria', 8, 'ACTIVE'),
('Yanis Guermouche', 'FW', 10, 'Algeria', 8, 'ACTIVE');

-- Марек
INSERT INTO players (full_name, position, shirt_number, nationality, club_id, status) VALUES
('Yanislav Yankov', 'GK', 1, 'Bulgaria', 9, 'ACTIVE'),
('Matthias Eiba', 'DF', 5, 'Germany', 9, 'ACTIVE'),
('Aleksandar Dyulgerov', 'DF', 23, 'Bulgaria', 9, 'ACTIVE'),
('Daniel Kirilov', 'DF', 33, 'Bulgaria', 9, 'ACTIVE'),
('Hristo Kaymakanski', 'DF', 44, 'Bulgaria', 9, 'ACTIVE'),
('Kiril Kaninski', 'MF', 2, 'Bulgaria', 9, 'ACTIVE'),
('Valeri Yordanov', 'MF', 8, 'Bulgaria', 9, 'ACTIVE'),
('Veselin Lyubomirov', 'MF', 13, 'Bulgaria', 9, 'ACTIVE'),
('Emmanuel Ajoku', 'MF', 88, 'Nigeria', 9, 'ACTIVE'),
('Rosen Yordanov', 'FW', 18, 'Bulgaria', 9, 'ACTIVE'),
('Dimitar Goranov', 'FW', 19, 'Bulgaria', 9, 'ACTIVE');

-- Монтана
INSERT INTO players (full_name, position, shirt_number, nationality, club_id, status) VALUES
('Vasil Simeonov', 'GK', 30, 'Bulgaria', 10, 'ACTIVE'),
('Petar Atanasov', 'DF', 8, 'Bulgaria', 10, 'ACTIVE'),
('Albin Linnér', 'DF', 3, 'Sweden', 10, 'ACTIVE'),
('Christopher Acheampong', 'DF', 15, 'Ghana', 10, 'ACTIVE'),
('Solomon James', 'DF', 25, 'Nigeria', 10, 'ACTIVE'),
('Ibrahim Muhammad', 'MF', 2, 'Nigeria', 10, 'ACTIVE'),
('Tomás Azevedo', 'MF', 27, 'Portugal', 10, 'ACTIVE'),
('Boris Dimitrov', 'MF', 11, 'Bulgaria', 10, 'ACTIVE'),
('Vladislav Tsekov', 'FW', 19, 'Bulgaria', 10, 'ACTIVE'),
('Matthew Kingsley', 'FW', 22, 'Nigeria', 10, 'ACTIVE'),
('Vladislav Mirchev', 'FW', 9, 'Bulgaria', 10, 'ACTIVE');

-- Струмска слава
INSERT INTO players (full_name, position, shirt_number, nationality, club_id, status) VALUES
('Sergey Mitkov', 'GK', 1, 'Bulgaria', 11, 'ACTIVE'),
('Rumen Sandev', 'DF', 3, 'Bulgaria', 11, 'ACTIVE'),
('Martin Kostov', 'DF', 5, 'Bulgaria', 11, 'ACTIVE'),
('Aleksandar Aleksandrov', 'DF', 17, 'Bulgaria', 11, 'ACTIVE'),
('Denislav Mitsakov', 'DF', 22, 'Bulgaria', 11, 'ACTIVE'),
('Borislav Nikolov', 'MF', 2, 'Bulgaria', 11, 'ACTIVE'),
('Lazar Stoychev', 'MF', 6, 'Bulgaria', 11, 'ACTIVE'),
('Georgi Yanev', 'MF', 8, 'Bulgaria', 11, 'ACTIVE'),
('Arnel Kadric', 'MF', 18, 'Croatia', 11, 'ACTIVE'),
('Tsvetomir Vachev', 'FW', 9, 'Bulgaria', 11, 'ACTIVE'),
('Eugene Okwudima', 'FW', 11, 'Nigeria', 11, 'ACTIVE');

-- Спортист Своге
INSERT INTO players (full_name, position, shirt_number, nationality, club_id, status) VALUES
('Nikola Zlatinov', 'GK', 1, 'Bulgaria', 12, 'ACTIVE'),
('Lionel Samba', 'DF', 88, 'Congo', 12, 'ACTIVE'),
('Kristiyan Ivanov', 'DF', 8, 'Bulgaria', 12, 'ACTIVE'),
('José Neto', 'MF', 23, 'Brazil', 12, 'ACTIVE'),
('Vladimir Gogov', 'MF', 18, 'Bulgaria', 12, 'ACTIVE'),
('Yoan Velinov', 'MF', 6, 'Bulgaria', 12, 'ACTIVE'),
('Adriyan Todorov', 'MF', 22, 'Bulgaria', 12, 'ACTIVE'),
('Kevin Monteiro', 'FW', 73, 'Portugal', 12, 'ACTIVE'),
('Yuri Pinheiro', 'FW', 11, 'Brazil', 12, 'ACTIVE'),
('Dimitar Nikolov', 'FW', 14, 'Bulgaria', 12, 'ACTIVE'),
('Pavel Ivanov', 'FW', 20, 'Bulgaria', 12, 'ACTIVE');

-- Дунав
INSERT INTO players (full_name, position, shirt_number, nationality, club_id, status) VALUES
('Mario Mladenov', 'GK', 1, 'Bulgaria', 13, 'ACTIVE'),
('Áquila Monteiro', 'DF', 13, 'Brazil', 13, 'ACTIVE'),
('Preslav Petrov', 'DF', 3, 'Bulgaria', 13, 'ACTIVE'),
('Stoyan Predev', 'DF', 22, 'Bulgaria', 13, 'ACTIVE'),
('Mario Dilchovski', 'DF', 81, 'Bulgaria', 13, 'ACTIVE'),
('Viktor Vasilev', 'MF', 6, 'Bulgaria', 13, 'ACTIVE'),
('Kristiyan Boychev', 'MF', 10, 'Bulgaria', 13, 'ACTIVE'),
('Radoslav Apostolov', 'MF', 14, 'Bulgaria', 13, 'ACTIVE'),
('Eliseé Sou', 'MF', 78, 'Burkina Faso', 13, 'ACTIVE'),
('Preslav Bachev', 'FW', 9, 'Bulgaria', 13, 'ACTIVE'),
('Denislav Minchev', 'FW', 11, 'Bulgaria', 13, 'ACTIVE');

-- Етър
INSERT INTO players (full_name, position, shirt_number, nationality, club_id, status) VALUES
('Angel Martinov', 'GK', 1, 'Bulgaria', 14, 'ACTIVE'),
('Georgi Aleksandrov', 'DF', 4, 'Bulgaria', 14, 'ACTIVE'),
('Rosen Varbishki', 'DF', 5, 'Bulgaria', 14, 'ACTIVE'),
('Nikola Borisov', 'DF', 15, 'Bulgaria', 14, 'ACTIVE'),
('Petar Zografov', 'DF', 2, 'Bulgaria', 14, 'ACTIVE'),
('Georgi Ivanov', 'MF', 6, 'Bulgaria', 14, 'ACTIVE'),
('Rosen Ivanov', 'MF', 7, 'Bulgaria', 14, 'ACTIVE'),
('Viktor Vasilev', 'MF', 8, 'Bulgaria', 14, 'ACTIVE'),
('Chavdar Ivaylov', 'MF', 10, 'Bulgaria', 14, 'ACTIVE'),
('Toma Ushagelov', 'FW', 9, 'Bulgaria', 14, 'ACTIVE'),
('Kristiyan Velichkov', 'FW', 19, 'Bulgaria', 14, 'ACTIVE');

-- Фратрия
INSERT INTO players (full_name, position, shirt_number, nationality, club_id, status) VALUES
('Vladyslav Ukrainskyi', 'GK', 1, 'Ukraine', 15, 'ACTIVE'),
('Arhan Isuf', 'DF', 13, 'Bulgaria', 15, 'ACTIVE'),
('Martin Kostadinov', 'DF', 17, 'Bulgaria', 15, 'ACTIVE'),
('Rosen Stefanov', 'DF', 44, 'Bulgaria', 15, 'ACTIVE'),
('Ibryam Ibryam', 'DF', 71, 'Bulgaria', 15, 'ACTIVE'),
('Aleksandar Tsvetkov', 'MF', 6, 'Bulgaria', 15, 'ACTIVE'),
('Rumen Rumenov', 'MF', 8, 'Bulgaria', 15, 'ACTIVE'),
('Maksim Marinov', 'MF', 20, 'Bulgaria', 15, 'ACTIVE'),
('Tymur Korablin', 'MF', 77, 'Ukraine', 15, 'ACTIVE'),
('Denis Kadir', 'MF', 9, 'Bulgaria', 15, 'ACTIVE'),
('Miroslav Marinov', 'FW', 15, 'Bulgaria', 15, 'ACTIVE');

-- Бдин
INSERT INTO players (full_name, position, shirt_number, nationality, club_id, status) VALUES
('Vasil Asenov', 'GK', 1, 'Bulgaria', 16, 'ACTIVE'),
('Venelin Todorov', 'DF', 4, 'Bulgaria', 16, 'ACTIVE'),
('Denis Nikolov', 'DF', 71, 'Bulgaria', 16, 'ACTIVE'),
('Martin Nikolov', 'DF', 11, 'Bulgaria', 16, 'ACTIVE'),
('Aleks Georgiev', 'DF', 30, 'Bulgaria', 16, 'ACTIVE'),
('Nikolay Tsvetkov', 'MF', 10, 'Bulgaria', 16, 'ACTIVE'),
('Stocco', 'MF', 6, 'Brazil', 16, 'ACTIVE'),
('Kaloyan Tsvetkov', 'MF', 8, 'Bulgaria', 16, 'ACTIVE'),
('Kristiyan Kotsov', 'MF', 88, 'Bulgaria', 16, 'ACTIVE'),
('Georgi Stoyanov', 'FW', 7, 'Bulgaria', 16, 'ACTIVE'),
('Radoslav Zahariev', 'FW', 9, 'Bulgaria', 16, 'ACTIVE');

-- MATCHES

INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (1, 1, 1, '2025-08-10', 1, 8, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (2, 1, 1, '2025-08-10', 2, 7, 2, 3, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (3, 1, 1, '2025-08-10', 3, 6, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (4, 1, 1, '2025-08-10', 4, 5, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (5, 2, 1, '2025-08-10', 9, 16, 1, 3, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (6, 2, 1, '2025-08-10', 10, 15, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (7, 2, 1, '2025-08-10', 11, 14, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (8, 2, 1, '2025-08-10', 12, 13, 3, 0, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (9, 1, 2, '2025-08-11', 1, 7, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (10, 1, 2, '2025-08-11', 8, 6, 4, 3, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (11, 1, 2, '2025-08-11', 2, 5, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (12, 1, 2, '2025-08-11', 3, 4, 3, 2, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (13, 2, 2, '2025-08-11', 9, 15, 4, 3, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (14, 2, 2, '2025-08-11', 16, 14, 1, 1, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (15, 2, 2, '2025-08-11', 10, 13, 1, 0, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (16, 2, 2, '2025-08-11', 11, 12, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (17, 1, 3, '2025-08-12', 1, 6, 3, 2, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (18, 1, 3, '2025-08-12', 7, 5, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (19, 1, 3, '2025-08-12', 8, 4, 4, 3, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (20, 1, 3, '2025-08-12', 2, 3, 2, 0, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (21, 2, 3, '2025-08-12', 9, 14, 4, 0, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (22, 2, 3, '2025-08-12', 15, 13, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (23, 2, 3, '2025-08-12', 16, 12, 1, 0, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (24, 2, 3, '2025-08-12', 10, 11, 4, 2, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (25, 1, 4, '2025-08-13', 1, 5, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (26, 1, 4, '2025-08-13', 6, 4, 2, 3, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (27, 1, 4, '2025-08-13', 7, 3, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (28, 1, 4, '2025-08-13', 8, 2, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (29, 2, 4, '2025-08-13', 9, 13, 1, 0, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (30, 2, 4, '2025-08-13', 14, 12, 3, 3, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (31, 2, 4, '2025-08-13', 15, 11, 2, 2, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (32, 2, 4, '2025-08-13', 16, 10, 4, 3, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (33, 1, 5, '2025-08-14', 1, 4, 0, 1, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (34, 1, 5, '2025-08-14', 5, 3, 2, 0, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (35, 1, 5, '2025-08-14', 6, 2, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (36, 1, 5, '2025-08-14', 7, 8, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (37, 2, 5, '2025-08-14', 9, 12, 1, 3, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (38, 2, 5, '2025-08-14', 13, 11, 1, 0, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (39, 2, 5, '2025-08-14', 14, 10, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (40, 2, 5, '2025-08-14', 15, 16, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (41, 1, 6, '2025-08-15', 1, 3, 2, 3, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (42, 1, 6, '2025-08-15', 4, 2, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (43, 1, 6, '2025-08-15', 5, 8, 3, 0, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (44, 1, 6, '2025-08-15', 6, 7, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (45, 2, 6, '2025-08-15', 9, 11, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (46, 2, 6, '2025-08-15', 12, 10, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (47, 2, 6, '2025-08-15', 13, 16, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (48, 2, 6, '2025-08-15', 14, 15, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (49, 1, 7, '2025-08-16', 1, 2, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (50, 1, 7, '2025-08-16', 3, 8, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (51, 1, 7, '2025-08-16', 4, 7, 2, 1, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (52, 1, 7, '2025-08-16', 5, 6, 0, 3, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (53, 2, 7, '2025-08-16', 9, 10, 1, 2, 'FINISHED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (54, 2, 7, '2025-08-16', 11, 16, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (55, 2, 7, '2025-08-16', 12, 15, 0, 0, 'SCHEDULED');
INSERT INTO matches (id, league_id, round_no, match_date, home_club_id, away_club_id, home_goals, away_goals, status) VALUES (56, 2, 7, '2025-08-16', 13, 14, 0, 0, 'SCHEDULED');
-- GOALS

INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (2, 14, 2, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (2, 19, 2, 17);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (2, 76, 7, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (2, 69, 7, 32);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (2, 74, 7, 54);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (5, 98, 9, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (5, 173, 16, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (5, 167, 16, 31);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (5, 169, 16, 56);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (8, 125, 12, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (8, 126, 12, 26);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (8, 123, 12, 33);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (10, 83, 8, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (10, 84, 8, 27);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (10, 87, 8, 36);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (10, 87, 8, 51);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (10, 59, 6, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (10, 63, 6, 38);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (10, 57, 6, 56);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (12, 31, 3, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (12, 28, 3, 29);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (12, 24, 3, 47);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (12, 43, 4, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (12, 43, 4, 30);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (13, 99, 9, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (13, 91, 9, 25);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (13, 98, 9, 38);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (13, 93, 9, 50);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (13, 160, 15, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (13, 156, 15, 32);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (13, 157, 15, 53);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (14, 176, 16, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (14, 146, 14, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (15, 107, 10, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (17, 8, 1, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (17, 10, 1, 22);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (17, 11, 1, 31);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (17, 57, 6, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (17, 66, 6, 39);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (19, 84, 8, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (19, 84, 8, 29);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (19, 84, 8, 47);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (19, 82, 8, 63);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (19, 40, 4, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (19, 37, 4, 26);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (19, 35, 4, 43);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (20, 21, 2, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (20, 18, 2, 27);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (21, 99, 9, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (21, 90, 9, 25);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (21, 90, 9, 42);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (21, 96, 9, 65);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (23, 174, 16, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (24, 104, 10, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (24, 109, 10, 29);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (24, 105, 10, 52);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (24, 101, 10, 67);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (24, 113, 11, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (24, 118, 11, 20);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (26, 59, 6, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (26, 62, 6, 25);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (26, 44, 4, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (26, 42, 4, 21);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (26, 44, 4, 42);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (29, 94, 9, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (30, 151, 14, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (30, 151, 14, 26);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (30, 154, 14, 32);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (30, 130, 12, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (30, 126, 12, 25);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (30, 127, 12, 31);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (31, 164, 15, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (31, 160, 15, 21);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (31, 119, 11, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (31, 116, 11, 27);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (32, 168, 16, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (32, 176, 16, 29);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (32, 175, 16, 51);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (32, 170, 16, 64);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (32, 102, 10, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (32, 107, 10, 40);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (32, 108, 10, 58);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (33, 44, 4, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (34, 49, 5, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (34, 46, 5, 22);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (37, 91, 9, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (37, 123, 12, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (37, 129, 12, 20);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (37, 128, 12, 45);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (38, 134, 13, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (41, 7, 1, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (41, 10, 1, 21);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (41, 29, 3, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (41, 31, 3, 24);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (41, 30, 3, 36);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (43, 47, 5, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (43, 46, 5, 30);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (43, 48, 5, 44);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (51, 44, 4, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (51, 42, 4, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (51, 73, 7, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (52, 58, 6, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (52, 58, 6, 36);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (52, 62, 6, 59);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (53, 92, 9, 10);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (53, 103, 10, 15);
INSERT INTO goals (match_id, player_id, club_id, minute) VALUES (53, 106, 10, 22);
-- CARDS

INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (2, 20, 2, 24, 'R');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (8, 139, 13, 38, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (10, 66, 6, 64, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (12, 27, 3, 84, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (12, 26, 3, 48, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (13, 95, 9, 44, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (13, 97, 9, 30, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (14, 150, 14, 88, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (14, 170, 16, 83, 'R');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (15, 140, 13, 63, 'R');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (17, 63, 6, 26, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (19, 39, 4, 42, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (20, 15, 2, 84, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (23, 176, 16, 77, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (23, 174, 16, 64, 'R');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (24, 104, 10, 88, 'R');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (24, 101, 10, 89, 'R');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (26, 41, 4, 61, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (26, 35, 4, 28, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (33, 36, 4, 39, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (33, 38, 4, 44, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (38, 113, 11, 43, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (38, 142, 13, 56, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (41, 33, 3, 70, 'R');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (41, 29, 3, 69, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (43, 48, 5, 35, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (43, 81, 8, 90, 'Y');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (51, 40, 4, 26, 'R');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (52, 51, 5, 43, 'R');
INSERT INTO cards (match_id, player_id, club_id, minute, card_type) VALUES (52, 58, 6, 80, 'Y');
-- TRANSFERS

INSERT INTO transfers (player_id, from_club_id, to_club_id, transfer_date, fee) VALUES (1, NULL, 4, '2025-01-10', 50000);
INSERT INTO transfers (player_id, from_club_id, to_club_id, transfer_date, fee) VALUES (2, 2, 5, '2025-06-15', 200000);