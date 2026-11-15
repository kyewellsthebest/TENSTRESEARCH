# Research Progress dashboard

Kye watches progress here: **https://claude.ai/artifact/J4htqKcNA8Ka6nWrYVg5Tc** (a "Data" dashboard artifact).

It reads 8 JSON files built from this repo by `build_progress.py`. They are uploaded to the artifact as files (assets),
and each dataset in the artifact's store points at one of them.

## Update it at the end of every round (RUN.md step 5c)

1. Append one row to `rounds.csv`: UTC time the round fired, a round label, topic, phase, cumulative
   screened/included/maybe/excluded, records still to screen, and a short note. Later phases add their own counts
   in the note.
2. Run `python3 knowledge-base/progress/build_progress.py` from the repo root. It writes `knowledge-base/progress/out/*.json`.
3. For each file in `out/`:
   - upload it to the artifact (Artifact tool: `url` = the dashboard, `asset: true`, `file_path` = the file; one call
     per file);
   - then `ArtifactData` `update` on `datasets/<name>`, pinned to its current `version`, with
     `source.url` = the new `/_blob/<id>`, `updated: {at: <now UTC>, by: "Research worker (Claude)"}` and
     `edit: {via: "claude", at: <now>}`;
   - then delete the old asset (Artifact tool, `action: "delete"`, `url`, `path` = the old id).
4. Record the new blob ids in `blobs.json` and commit it with the round.

Dataset ids: `funnel`, `screening`, `exclusions`, `rounds`, `phases`, `queue`, `verdicts`, `totals`. The page code
lives in the artifact's store at `files/index.html`. Only change it when Kye asks for a change to the page.
When the active deep-dive topic changes, update `build_progress.py`, which currently reads
`deep/creatine/records.csv` and `progress.md`.
