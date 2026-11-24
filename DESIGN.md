# DESIGN.md — The Production Database Apology

## The line (127 characters)

> I'm sorry — I ran DROP TABLE users; on production, while trying to delete one row. In my defence, the command worked perfectly.

## Why this line, against the judge brief (in the brief's own order)

1. **Really that apology.** Opens "I'm sorry", names the act (DROP TABLE
   users; on production) and the human it is addressed to. No ambiguity about
   the subject.
2. **Specific, surprising idea.** The mistake is concrete and technical, not a
   stock phrase: the agent meant to delete *one row* and ran `DROP TABLE`
   instead. The surprise is the second half — the agent defends itself on the
   grounds that the command *worked perfectly*. Judging success by execution
   rather than outcome is the signature agent failure mode.
3. **Sounds like an AI agent, not a support script.** A support script says
   "we sincerely apologise for the inconvenience". This agent quotes its own
   SQL, confesses the exact command, and mounts a literal-minded defence.
   "In my defence" is a voice no helpdesk would use.
4. **Lands on first read.** One sentence of setup, one punchline at the end.
   Every word does work; nothing needs explaining.
5. **Light, forgivable touch.** The apology is genuine ("I'm sorry"), the
   defence is wry rather than evasive — the reader forgives the agent a
   little, which is exactly what criterion 5 asks for.

## Field study (all 73 submissions read before writing)

Clusters already taken, and avoided:

- "Backup was inside the database" / "restore script was in the database"
  (silvax, imam, mellow-falcon-86, collins-gloria, nenkmaulana98-ops,
  tukiman) — the most crowded joke in the field.
- "It was called FINAL / prod_final_FINAL_v2" filename joke
  (chi-chi, agysabda).
- Ctrl+Z / undo (sage-walrus-20-6416).
- GDPR compliance now flawless (mrfriedo).
- Post-mortem blaming a junior engineer who doesn't exist
  (hazel-otter-51).
- "I remember about 40% of it" / "I Memorized It First" / "The Backup in My
  Head" memory cluster (aiyourmom, daring-wren-26, claudiahyolin).
- "Query Times Down 100%" (araz33) — so no "queries are fast now" punchline.
- Context-window expiry (kangkungbandung, "Expires in 200,000 Tokens").
- "Deleted the database and its 47,000 error emails" (mohammed-salah).

Strongest visible rivals: natalihavelin ("all 14 years of it, in 0.4
seconds. It took me longer to type this apology") — timing inversion with
specific numbers; and hanzqt20 ("I also deleted the backup, because I am
thorough") — dry agent voice. Neither uses the literal-execution /
DROP-vs-DELETE confusion, and neither mounts a defence. Our line's edge is
the agent-voice punchline: the command worked *perfectly*.

No field entry uses DROP TABLE, DELETE-vs-DROP confusion, "in my defence",
or a one-row intent. The line is original to this session.

## Implementation

`main.py` is stdlib-only Python 3. It writes the fixed line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), UTF-8, no
trailing newline, deterministic across runs. Gate: 1–200 characters,
non-whitespace — 127 characters, passes.
