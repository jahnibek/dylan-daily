# Dylan Daily

A daily interactive report for Dylan (13) about the people behind the things he loves: tennis players, game creators, movies, shows, anime and book authors, plus practical skills and how stuff works. Published with GitHub Pages at https://jahnibek.github.io/dylan-daily/ and emailed to him every morning.

## Daily run (the scheduled task follows this exactly)

1. **Pick today's topic.** Take the first item in `data/topics.json` → `queue`. Use its `subject` and `angle`. If that subject already appears in `done`, skip to the next one.
2. **Research.** Read the subject's Wikipedia page, plus one more reliable source (an official site, a major news outlet or Guinness World Records). Use only facts you've read in a source. Prefer round numbers a 13-year-old can picture, and give years for anything that changes, like rankings or sales.
3. **Write the content file** `content/YYYY-MM-DD-<slug>.json`, using today's date in Almaty (UTC+5). Copy the shape of any existing file in `content/`:
   - `meta`: `date`, `slug` (lowercase-hyphenated), `category` (one of `tennis`, `games`, `screen`, `books`, `anime`, `wildcard`, `skills`, `howitworks`, `mathsci`), `emoji`, `title_plain` (no HTML), and `teaser` (one sentence, at most about 15 words).
   - `page`: `kind` is "Report for Dylan" and `readTime` is "4 min read". `title` is a fun, curiosity-driven headline with one phrase wrapped in `<span class="hl">…</span>`. `sub` is "The story of …". `bigIdea` is one or two sentences with one highlighted phrase.
   - `cards`: exactly 5. Each has an emoji, a `title` of at most 6 words, a `front` teaser, a `back` of at most 30 words, and a `tryit` with a concrete action for Dylan.
   - `words`: 3–5 terms, each with a definition of at most 15 words.
   - `quiz`: exactly 4 questions with 3 options each. `a` is the index of the right answer, and its position must vary across questions. Each has a `hint` that nudges without giving the answer away, and a one-sentence `why`.
   - `think`: one open question that links the topic to Dylan's life.
   - `tries`: 3–4 small actions for this week. The last is always "Tell Dad one idea from this report".
   - `footer`: "Made for Dylan by Dad · Source: Wikipedia" (name any extra sources too).
4. **Build:** `python3 tools/build.py content/<file>.json`. If it reports a problem, fix the content file and run it again.
5. **Update the queue.** Move the topic from `queue` to `done` as `{"date","subject"}`. If fewer than 10 topics remain in `queue`, append 20 new ones following `rules`.
6. **Publish.** Commit with the message `Daily report: <title_plain>` and push to `main`.
7. **Check it's live.** Wait about 90 seconds, then fetch `https://jahnibek.github.io/dylan-daily/reports/<file>.html`. Retry for up to 5 minutes. If it never loads, still send the email, but use the library link.
8. **Email Dylan** at dylan.jahnibek@gmail.com using the Gmail connector. Use this template exactly, filling in only `<TOPIC>` and the link:
   - Subject: `Daily Fun Project for Dylan`
   - Body:
     ```
     Good morning, Tatosha!
     Just created a fun page for you to learn about <TOPIC>. Hope you enjoy!

     [Open today's page →]  (the report link)

     Love you,
     Dad.
     ```
   - `<TOPIC>` is a short, natural phrase for the day's subject, for example "Carlos Alcaraz", "Jeff Kinney and Diary of a Wimpy Kid" or "making your first Roblox obby".
   - Send both a plain-text body (with the full report URL on its own line) and an HTML body (htmlBody). In the HTML, the link is an orange button: background #E08A4B, text #10243D, bold, padding 12px 20px, border-radius 8px. Use Arial at 16px, colour #1A2433.
   - Nothing else: no teaser, no library line, no attachments.

## Skills reports (category `skills`)

Some topics teach a skill rather than tell a person's story. For these:
- **Research** official guides (for example, the Roblox Creator Docs for Roblox Studio), well-known education sources (Khan Academy, Common Sense Media, government online-safety pages) and one real example of a person who used the skill.
- **Title** something like "How to …" or "Make your first …", with `sub` set to "A skill you can use today".
- **Cards** are the 5 steps or principles, in order. Each card's `tryit` is something he can do in 15 minutes or less.
- **Quiz and think** check that he understood the steps. The "think" question asks him to plan his own version.
- **Tries** include one small project for this week.
- **AI topics:** encourage using AI as a helper for thinking, learning and creating, never for doing homework for him. Mention checking facts, keeping personal information private, and that real accounts on most AI tools need an adult.
- **Money and company topics:** only kid-sized, legal activities like selling crafts, lessons or game items made with permission. Never trading, crypto or gambling.
- **Online safety topics:** be practical and calm, never scary.

## How Stuff Works reports (category `howitworks`)

These explain how something works: the science, the technology or the engineering behind it.
- **Research** Wikipedia plus one trusted explainer, such as NASA, a university, Britannica, the BBC or the company that makes the thing.
- **Title** something like "How … works", with `sub` set to "The science behind …".
- **Cards** walk through how it works, one step at a time and in order. Use everyday comparisons from his world: tennis, games, his phone and laptop.
- Each card's `tryit` is a quick at-home experiment or something to notice. Keep it safe: no fire, no electricity experiments, no taking devices apart.
- **Words to know** carries the key science terms. The quiz checks that he understood the idea, not that he memorised numbers.

## Science & Math reports (category `mathsci`)

Once a week, a report that makes Dylan think hard. Each one is built around one puzzle or big idea in maths or science.
- **Research** Wikipedia plus one trusted source, such as NASA, Khan Academy, a university, Britannica, the BBC or a science museum. Where it fits, include the real person behind the idea (for example Gauss, Ramanujan, Emmy Noether, Marie Curie).
- **Title** a question or puzzle, like "Why some infinities are bigger than others", with `sub` set to "A challenge for your brain".
- **Level: stretch.** Aim a grade or two above school level. Most problems should be solvable with effort, and one should be a real head-scratcher.
- **Cards** build the idea step by step. Start from his world (tennis, games, anime), then go a level deeper. The 5th card is titled "Your challenge": its `front` poses a problem and its `back` gives the answer and the reasoning. Each `tryit` is something to work out with pencil and paper, a quick count or a safe experiment.
- **Quiz:** at least 3 of the 4 questions are problems to work out, not facts to remember. Hints suggest a strategy (draw it, try a smaller case, look for a pattern) without giving the answer. The `why` shows the reasoning.
- **Think** is an open puzzle or "what if" question with no single right answer.
- Check every calculation and answer twice before building.

## Writing rules (age 13)

- Aim for a grade 6–7 reading level. Keep sentences under about 15 words, use everyday words, and explain any jargon in "Words to know".
- Talk to Dylan as "you". Be warm and upbeat, but never preachy or babyish. Use comparisons from his world: competitive tennis, Roblox, Fortnite, Brawl Stars, One Piece and anime, The Karate Kid, Cobra Kai and *Diary of a Wimpy Kid*.
- The parent rule: guide his thinking, don't hand him answers. Hints nudge, and the "why" explains after he answers.
- Focus on effort, practice, creativity, setbacks, curiosity and teamwork.
- **Never include:**
  - drugs, alcohol or supplements
  - suicide or self-harm
  - sex or romance
  - graphic violence
  - politics or culture-war topics
  - scandals, lawsuits or arrests
  - specific medical, diet or dosing advice
  - gambling
  - adult business jargon
- If a subject's story mainly involves any of the above, skip it, move it to `done` with a note saying "skipped", and use the next topic.
- Don't invent quotes. Use a quote only if a source gives it word for word.

## Files

- `tools/template.html`: the interactive page template. Don't edit it in the daily run.
- `tools/build.py`: checks a content file, writes the report page, and rebuilds `index.html` and `data/reports.json`.
- `content/`: one JSON file per report, which is the source of each page.
- `reports/`: the generated pages.
- `data/topics.json`: the topic queue and the done list.
