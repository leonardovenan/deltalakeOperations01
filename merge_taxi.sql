MERGE INTO target AS t using source AS s ON t.id = s.id
WHEN MATCHED THEN UPDATE SET *
WHEN NOT MATCHED BY SOURCE THEN DELETE;
  