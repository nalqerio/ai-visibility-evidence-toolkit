# AI visibility evidence toolkit

Blank working templates and a small local calculator for reviewing brand mentions, citations and website findings. Maintained by [Nalqerio](https://nalqerio.com/), a commercial AI visibility software provider. You can use the toolkit without a Nalqerio account.

[Deutsche Anleitung](README.de.md)

## Start with one real decision

1. Choose a customer question and keep its wording, language and market fixed.
2. Save the original answer where you are permitted to do so. Record the interface, system, date and available model information.
3. Complete one row per answer in `templates/measurement.csv`. A failed response is `failed`, not a negative brand mention.
4. Review important claims with `templates/source-review.csv`. A linked page is evidence only for claims it actually supports.
5. Turn a supported finding into a task in `templates/website-audit.csv`. Record a completion criterion and a later review.

Keep the original evidence outside a public repository. The templates are blank; the worked example is entirely fictional.

## Files and related guides

| File | Purpose | Explanation |
| --- | --- | --- |
| `templates/measurement.csv` | One observation per question, system and run | [Measure AI visibility](https://nalqerio.com/knowledge/measure-ai-visibility) |
| `templates/source-review.csv` | Map a claim to a source passage | [Review Perplexity sources](https://nalqerio.com/knowledge/perplexity-seo) |
| `templates/website-audit.csv` | Separate technical checks from answer observations | [GEO audit](https://nalqerio.com/knowledge/geo-audit) |
| `examples/organization.json` | Fictional business JSON-LD to adapt | [Schema markup and validation](https://nalqerio.com/knowledge/schema-markup) |
| `examples/robots-search-vs-training.txt` | Illustrate two different fetching decisions | [AI crawler guide](https://nalqerio.com/knowledge/ai-crawlers) |
| `examples/llms.txt` | Fictional, curated documentation entry point | [llms.txt guide](https://nalqerio.com/knowledge/llms-txt) |

## Calculate the documented sample

Requires Python 3.9 or later; only the standard library is used. No network requests, API keys or external dependencies.

```sh
python3 scripts/summarize.py examples/fictional-measurement.csv
python3 scripts/summarize.py templates/measurement.csv
python3 -m unittest discover -s tests
```

Expected worked example: three evaluable answers, one brand mention, one failed response. Answer mention rate is 1/3. Question coverage is 1/1 because all three evaluable answers concern the same question. Citation data is available for two answers; one cites an owned page. Missing citation data is excluded from that denominator.

The calculator prints counts and denominators. It does not produce a universal ranking or establish that an edit caused a changed answer. Mixing manual chat observations with API results, languages or question revisions produces a mixed sample; split such comparisons into separate files.

## Field conventions

- `response_status`: `completed`, `failed` or `missing`.
- `brand_mention`: `yes`, `no` or `unknown`. Unknown observations are excluded from the mention-rate denominator even if an answer was returned.
- `citation_status`: `available` or `unavailable`. An available empty source list is `available` with an empty `own_citation_url`.
- `own_citation_url`: a directly observed owned-page URL, or blank. Use one representative owned citation for this answer; record all sources in the source-review sheet.
- `interface`: describe the actual environment, such as `manual-chat` or `api`.
- `recommendation_context`: describe favourable, critical or passing context in words; do not infer it from the mention alone.
- `evidence_file`: a reference to privately stored, permitted evidence. Never upload private customer answers or access tokens here.

## Technical examples

All `example.com` values and the ExamplePlan business are fictional. JSON validity is separate from Schema.org vocabulary validity and eligibility for a particular Google feature. Use the [Schema Markup Validator](https://validator.schema.org/) and, when relevant, the [Rich Results Test](https://search.google.com/test/rich-results); compare the result with visible business facts.

The robots example is a fragment, not a replacement for an existing file. Read current [OpenAI bot documentation](https://developers.openai.com/api/docs/bots) before changing rules. Robots rules communicate fetching preferences; they do not secure private content. An llms.txt file is a documentation proposal, not a mechanism for guaranteeing citations.

## Contributions and scope

Suggestions should include a reproducible example, accurate sources and no confidential information. Please do not add promotional link lists or fabricated customer results. This material was created with AI assistance; technical examples were checked locally for the validation described in this repository. No live website deployment or independent customer study is implied.

Prepared 11 October 2026. Provider behaviour and documentation can change.
