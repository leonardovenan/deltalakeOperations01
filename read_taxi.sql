SELECT * FROM table_changes('taxi', 3, 7);

SELECT * FROM table_changes_by_path(
  '/tmp/taxi', '2023-04-09', '2023-04-10'
)