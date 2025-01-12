DROP VIEW ACTUAL_PLAYERS_AFFILIATIONS;

CREATE OR REPLACE VIEW ACTUAL_PLAYERS_AFFILIATIONS
    as
    select row_number() OVER () as id,
        p.id player_id, t.id team_id
    from players p,
         teams t,
         players_affilations pa
    where p.id = pa.player_id
    and t.id = pa.team_id
    and pa.end_date is null;