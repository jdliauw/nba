CREATE TABLE player_info(
  pid TEXT PRIMARY KEY, /* PRIMARY */
  first_name TEXT,
  last_name TEXT,
  feet INT,
  inches INT,
  lbs INT,
  birth_year INT,
  birth_month INT,
  birth_day INT,
  birth_city TEXT,
  birth_state TEXT,
  twitter TEXT,
  shoots TEXT,
  position INT,
  hs_city TEXT,
  hs_state TEXT,
  pick INT,
  draft_year INT
);

CREATE TABLE game_logs(
  pid TEXT,       /* PRIMARY */
  playoffs BOOLEAN,
  game_season INT,
  game_date DATE, /* PRIMARY */
  season INT,
  age_years INT,
  age_days INT,
  team_id TEXT,
  opp_id TEXT,
  won BOOLEAN,
  margin INT,
  starter BOOLEAN,
  minutes_played INT,
  seconds_played INT,
  fg INT,
  fga INT,
  fg_pct REAL,
  fg3 INT,
  fg3a INT,
  fg3_pct REAL,
  ft INT,
  fta INT,
  ft_pct REAL,
  orb INT,
  drb INT,
  trb INT,
  ast INT,
  stl INT,
  blk INT,
  tov INT,
  pf INT,
  pts INT,
  game_score REAL,
  plus_minus INT,
  reason TEXT,
  PRIMARY KEY (pid, game_date)
);

CREATE TABLE college_stats(
  pid TEXT,     /* PRIMARY */
  year INT,     /* PRIMARY */
  age INT,
  college TEXT, /* PRIMARY */
  g INT,
  mp INT,
  fg INT,
  fga INT,
  fg3 INT,
  fg3a INT,
  ft INT,
  fta INT,
  orb INT,
  trb INT,
  ast INT,
  stl INT,
  blk INT,
  tov INT,
  pf INT,
  pts INT,
  fg_pct REAL,
  fg3_pct REAL,
  ft_pct REAL,
  mp_per_g REAL,
  pts_per_g REAL,
  trb_per_g REAL,
  ast_per_g REAL,
  PRIMARY KEY (pid, year, college)
);